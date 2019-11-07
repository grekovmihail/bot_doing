# КНопочки главного меню
from handlers.exchange_coin import to_exchange_coin
from handlers.exchange_rates import get_exchange_rates
from handlers.history_of_exchanges import history_of_exchanges
from handlers.informations import get_informations
from handlers.settings import change_settings
from reddis_settings import *
from telegram_api import bot
from utils.keyboard import BotKeyboard

if __name__ == '__main__':

  def text_command(message):
    if message.text == 'Произвести обмен':
        to_exchange_coin(message)

    elif message.text == 'История операций':
        bot.send_message(message.chat.id, ' История операций ')
        history_of_exchanges(message)
    elif message.text == 'Настройки':
        change_settings(message)

    elif message.text == 'Информация':
        bot.send_message(message.chat.id, ' Информация ')
        get_informations(message)

    elif message.text == 'Курсы обмена':
        get_exchange_rates(message)


  try:
    dict_with_state = conn.hgetall("pythonDict")  # redis
  except:
    print("no dict")


  @bot.message_handler(commands=['start', 'menu'])
  def start_message(message):
    rows = {'Произвести обмен', 'История операций', 'Настройки', 'Информация', 'Курсы обмена', '/menu'}
    keyboardMain = BotKeyboard()
    key = keyboardMain.gef_native(rows, resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграм бот botname', reply_markup=key)
    dict_with_state[message.from_user.id] = ''

  # -----------------Обмен-------------
  @bot.message_handler(regexp='^\/(Buy)[0-9]+$')
  def call_from_to_exchange_coin(message):
    choice_crypto_sale(message)
  # -----------------------------------


  bot.polling()
