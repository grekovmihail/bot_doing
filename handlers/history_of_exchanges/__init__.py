from db.bot_deal import BotDeals
from db.settings_db import *
from telegram_api import bot

__all__ = (
    'history_of_exchanges',
)


def history_of_exchanges(message):
    bot.send_message(message.chat.id, ' История операций ')

    for count_coins, sum_deal, telephone, id_telegram in session.query(BotDeals.count_coins, BotDeals.sum_deal,
                                                                    BotDeals.telephone, BotDeals.id_telegram,
                                                                    ).filter(
        BotDeals.id_telegram == message.from_user.id):
        bot.send_message(message.chat.id, " Купили " + str(count_coins) + " в количеcтве " + str(
            count_coins) + " за  " + str(sum_deal) + " рублей  " + " у  " + str(telephone))
