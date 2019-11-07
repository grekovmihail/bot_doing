import json
import time

import requests

from telegram_api import bot


# Перевод на QIWI Кошелек
def send_p2p(api_access_token, to_qw, comment, sum_p2p, message):
    bot.send_message(message.chat.id, ' send_p2p ')

    s = requests.Session()
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['User-Agent'] = 'Android v3.2.0 MKT'
    s.headers['Accept'] = 'application/json'
    postjson = json.loads(
        '{"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"},"comment":"' + comment + '","fields":{"account":""}}')
    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = sum_p2p
    postjson['sum']['currency'] = '643'
    postjson['fields']['account'] = to_qw
    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments', json=postjson)

    if "Accepted" in res.text:
        bot.send_message(message.chat.id, 'All OK')
        status = 'ok'
    else:
        status = 'false'
        bot.send_message(message.chat.id, res.text)

    return status
