# TODO!!!

from telegram_api import bot

__all__ = (
    'get_exchange_rates',
)


def get_exchange_rates(message):
    bot.send_message(message.chat.id, 'Курсы обмена:   ')
