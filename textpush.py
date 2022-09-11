# coding=<utf-8>
import json

import requests


def send_message(message):
    userid = 'FanCaiSheng'  # userid
    agentid = '1000004'  # 应用ID
    corpsecret = '9Y-Yk_AySfcYQaJdn1lgj8eS1XR2b7P5gQQwiEcEfXw'  # Secret
    corpid = 'ww7c7fa044e0fd4516'  # 企业ID

    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    access_token = res.json()['access_token']

    json_dict = {
        "touser": userid,
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": message
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
    lt = dic['data']['news']
    for new in lt:
        new += '\n'
        lt[i] = new
        i += 1
    s = "".join(lt)
    return s


def main():
    print(send_message(news()))


if __name__ == '__main__':
    main()
