from db.bot_deal import BotDeals
from db.crypto_sale import CryptoSale
from db.settings_db import *
from db.user_bot_info import UserBotInfo
from utils.qiwi_api import send_p2p
from reddis_settings import *
from telegram_api import bot


def request_to_qiwi(message):
    global dict_with_state
    id_deal = dict_with_state[message.from_user.id].replace("/Buy", "")
    for id, count_coins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.count_coins, CryptoSale.price,
                                                                CryptoSale.text, CryptoSale.telephone,
                                                                ).filter(CryptoSale.id == str(id_deal)):
        count_coin_available = count_coins

    for keyqiwi, id_telegram in session.query(UserBotInfo.keyqiwi, UserBotInfo.id_telegram,

                                              ).filter(UserBotInfo.id_telegram == str(message.from_user.id)):
        api_access_token = keyqiwi

    count_coin = message.text

    '''
    update_info_bot = session.query(CryptoSale).filter(CryptoSale.id == int(id_deal)).first()
    update_info_bot.count_coins = int(count_coin_available) - int(count_coin)
    session.commit()

    result = db.session.query(User.money).with_for_update().filter_by(id=userid).first()
    money = result[0]
    user.money = money - 0.1
    '''

    update_info_bot = session.query(CryptoSale).with_for_update(of=CryptoSale).filter(
        CryptoSale.id == int(id_deal)).first()
    update_info_bot.count_coins = int(count_coin_available) - int(count_coin)
    session.commit()

    # ---------------------------------------------------

    status = ''
    if (int(count_coin) <= int(count_coin_available)):
        sum_p2p = int(count_coin) * int(price)
        print(" sum_p2p " + str(sum_p2p))
        # status = 'ok'
        send_p2p(api_access_token, telephone, 'comment', sum_p2p, message)
        print(" status " + str(status))

        if (status == 'ok'):
            newDeal = BotDeals(int(count_coin), int(sum_p2p), str(telephone), str(id_telegram), str(text))
            session.add(newDeal)
            session.commit()

            bot.send_message(message.chat.id, 'Деньги были переведены на счет продавца')
        else:
            bot.send_message(message.chat.id, 'Qiwi failed')
    else:
        print("all wrong")
        bot.send_message(message.chat.id, 'All failed')

    if (status != 'ok'):
        update_info_bot = session.query(CryptoSale).with_for_update(of=CryptoSale).filter(
            CryptoSale.id == int(id_deal)).first()
        update_info_bot.count_coins = update_info_bot.count_coins + int(count_coin)
        session.commit()

    dict_with_state[message.from_user.id] = ''
    conn.hmset("pythonDict", dict_with_state)  # redis
