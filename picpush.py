# coding=<utf-8>
import json

import requests


def send_message(message):
    userid = 'xxx'  # userid
    agentid = 'xxx'  # 应用ID
    corpsecret = 'xxx'  # Secret
    corpid = 'xxx'  # 企业ID

    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    access_token = res.json()['access_token']

    json_dict = {
        "touser": userid,
        "msgtype": "news",
        "agentid": agentid,
        "news": {
            "articles": [
                {
                    "title": "睁眼看世界",
                    "description": news()[1],
                    "url": getpicture_url()[1],
                    "picurl": getpicture_url()[0],
                }
            ]
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    json_str = json.dumps(json_dict, separators=(',', ':'))
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}", data=json_str)
    return res.json()['errmsg'] == 'ok'


def news():
    i = 0
    url = 'http://excerpt.rubaoo.com/toolman/getMiniNews'
    r = requests.get(url)
    dic = json.loads(r.text)
    des = dic["data"]["weiyu"]
    lt = dic['data']['news']
    for new in lt:
        new += '\n'
        lt[i] = new
        i += 1
    s = "".join(lt)
    return s, des[4:]


def getpicture_url():
    url = 'http://hc.baozi66.top:99/xjj.php?type=json'
    r = requests.get(url)
    dic = json.loads(r.text)
    return dic["video_png"], dic["video_url"]


def main():
    print(send_message(news()[0]))


if __name__ == '__main__':
    main()
