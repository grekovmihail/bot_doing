# купи продай и тд
from db.crypto_sale import CryptoSale
from db.settings_db import *
# from db.bot_deal import BotDeal

from reddis_settings import *
from telegram_api import bot

__all__ = (
    'to_exchange_coin',
    'choice_crypto_sale'
)


def to_exchange_coin(message):
    bot.send_message(message.chat.id, ' Обмен валюты ')

    for id, count_coins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.count_coins, CryptoSale.price,
                                                                CryptoSale.text, CryptoSale.telephone):
        print("nothing")
        print(count_coins, price, text, telephone)

        command = "/Buy" + str(id)
        bot.send_message(message.chat.id,
                         " В количеcтве " + str(count_coins) + " по цене за монету " + str(price) + " Монета -" + str(
                             text) + " Номер для покупки:  " + str(telephone) + " " + command,
                         )


def choice_crypto_sale(message):
    global dict_with_state
    bot.send_message(message.chat.id, 'Введите количество монет')
    dict_with_state[message.from_user.id] = message.text
    conn.hmset("pythonDict", dict_with_state)  # redis
    # Добавить выбор платежной системы для покупки, qiwi в отдельный модуль и другие систмеы платежные(уточнить какие)  (вывод в клаве будет, наверное)
