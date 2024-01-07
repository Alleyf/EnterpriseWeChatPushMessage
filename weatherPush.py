# coding=<utf-8>
import json
import os
import requests
import datetime
from bs4 import BeautifulSoup


userId =  os.environ.get("USER_ID")  # userId
agentId =  os.environ.get("AGENT_ID")  # 应用ID
corpSecret =  os.environ.get("CORP_SECRET")  # Secret
corpId =  os.environ.get("CORP_ID")  # 企业ID
weather_template_id = os.environ.get("TEMPLATE_ID") # 天气预报模板ID
city = os.environ.get("CITY") # 城市

def send_weather_message(my_city):

    today = datetime.date.today()
    today_str = today.strftime("%Y年%m月%d日")
    access_token = get_access_token()
    weather = get_weather(my_city)

    # markdown消息
    json_dict = markdown_message(today_str,weather)
    json_str = json.dumps(json_dict, separators=(',', ':'))
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}", data=json_str)
    # print(res.text)
    if res.json()['errmsg'] == 'ok':
        print(f"{my_city}天气日报发送成功")
    else:
        print(f"{my_city}天气日报发送失败")


def markdown_message(today_str,weather):
    # markdown消息
    json_dict = {
      "touser" : userId,
      "agentid" : agentId,
      "msgtype": "markdown",
      "markdown": {
            "content": """### 天气日报温馨提示
            
> - 🦄 **来源** [csFan](https://alleyf.github.io)
> - 🕐 **日期** {}
> - 🏰 **区域** {}
> - 🌈 **天气** {}
> -  🌡️ **气温** {}
> - 💨 **风向** {}
> - 💕 **我想对你说** {}""".format(today_str, weather[0], weather[2], weather[1], weather[3], get_daily_love())
      },
      "enable_duplicate_check": 0,
      "duplicate_check_interval": 1800
    }
    return json_dict


def template_message(today_str,weather):
    # 模板消息
    json_dict = {
        "touser" : userId,
        "agentid" : agentId,
        "msgtype" : "template_msg",
        "template_msg" : {
                "template_id": weather_template_id,
                "url": "https://github.com/Alleyf",
                "content_item": [
                    {
                        "key": "🕐日期",
                        "value": today_str
                    },
                    {
                        "key": "🏰区域",
                        "value": weather[0]
                    },
                    {
                        "key": "🌈天气",
                        "value": weather[2]
                    },
                    {
                        "key": "💧气温 | 💨风向",
                        "value": weather[1] + "\n" + weather[3]
                    },
                    {
                        "key": "💕我想对你说",
                        "value": get_daily_love()
                    }
                ]
            }
        }
    return json_dict



def get_access_token():
    # 获取access token的url
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpId={corpId}&corpSecret={corpSecret}")
    access_token = res.json()['access_token']
    return access_token

def get_daily_love():
    # 每日一句情话
    url = "https://api.lovelive.tools/api/SweetNothings/Serialization/Json"
    r = requests.get(url)
    all_dict = json.loads(r.text)
    sentence = all_dict['returnObj'][0]
    daily_love = sentence
    return daily_love

def get_weather(my_city):
    urls = ["http://www.weather.com.cn/textFC/hb.shtml",
            "http://www.weather.com.cn/textFC/db.shtml",
            "http://www.weather.com.cn/textFC/hd.shtml",
            "http://www.weather.com.cn/textFC/hz.shtml",
            "http://www.weather.com.cn/textFC/hn.shtml",
            "http://www.weather.com.cn/textFC/xb.shtml",
            "http://www.weather.com.cn/textFC/xn.shtml"
            ]
    for url in urls:
        resp = requests.get(url)
        text = resp.content.decode("utf-8")
        soup = BeautifulSoup(text, 'html5lib')
        div_conMidtab = soup.find("div", class_="conMidtab")
        tables = div_conMidtab.find_all("table")
        for table in tables:
            trs = table.find_all("tr")[2:]
            for index, tr in enumerate(trs):
                tds = tr.find_all("td")
                # 这里倒着数，因为每个省会的td结构跟其他不一样
                city_td = tds[-8]
                this_city = list(city_td.stripped_strings)[0]
                if this_city == my_city:

                    high_temp_td = tds[-5]
                    low_temp_td = tds[-2]
                    weather_type_day_td = tds[-7]
                    weather_type_night_td = tds[-4]
                    wind_td_day = tds[-6]
                    wind_td_day_night = tds[-3]

                    high_temp = list(high_temp_td.stripped_strings)[0]
                    low_temp = list(low_temp_td.stripped_strings)[0]
                    weather_typ_day = list(weather_type_day_td.stripped_strings)[0]
                    weather_type_night = list(weather_type_night_td.stripped_strings)[0]

                    wind_day = list(wind_td_day.stripped_strings)[0] + list(wind_td_day.stripped_strings)[1]
                    wind_night = list(wind_td_day_night.stripped_strings)[0] + list(wind_td_day_night.stripped_strings)[1]

                    # 如果没有白天的数据就使用夜间的
                    temp = f"{low_temp}——{high_temp}摄氏度" if high_temp != "-" else f"{low_temp}摄氏度"
                    weather_typ = weather_typ_day if weather_typ_day != "-" else weather_type_night
                    wind = f"{wind_day}" if wind_day != "--" else f"{wind_night}"
                    return this_city, temp, weather_typ, wind

def main(city):
    cityLs = city.split("|")
    # print(cityLs)
    for city in cityLs:
        send_weather_message(city)

if __name__ == '__main__':
    main(city)
