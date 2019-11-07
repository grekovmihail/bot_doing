# Тащим из БД нужную инфу TODO!!!
from telegram_api import bot

__all__ = (
    'get_informations',
)


def get_informations(message):
    bot.send_message(message.chat.id, ' Поддержка ')
