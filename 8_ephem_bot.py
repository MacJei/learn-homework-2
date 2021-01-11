"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import random
import ephem
import settings
from datetime import datetime, date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = settings.PROXY

cities_list = ['Москва', 'Архангельск', 'Норильск', 'Кострома']
game_list = []
user_cities_list = []


def greet_user(update, context): 
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_position(update, context):
    current_dt = date.today()
    user_text = update.message.text
    text = user_text.split()[1]
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn','Uran','Neptune', 'Pluto']

    if text.lower().strip().capitalize() == 'Earth':
      update.message.reply_text("Информации о Земле нет")
    elif text.lower().strip().capitalize() in planets:
      planet_cls = getattr(ephem, text)
      planet = planet_cls(current_dt)
      constellation = ephem.constellation(planet)[-1]
      update.message.reply_text(f'Планета *{text.title()}* сегодня в созвездии *{constellation}*.', parse_mode='MARKDOWN')
    else:
      update.message.reply_text(f'Планета *{text.title()}* не нашлась, просьба проверить корректность ввода.')


def wordcount(update, context):
  user_words = update.message.text.replace(',', '').split()[1:]
  user_words_len = len(user_words)
  update.message.reply_text('Количество слов: {}'.format(user_words_len))


def next_full_moon(update, context):
  user_date = update.message.text.split()[1]
  print(user_date)
  user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
  update.message.reply_text('Дата следующего полнолуния : {}'.format(ephem.next_full_moon(user_date)))

def cities(update, context):
  user_city = update.message.text.split()[1].capitalize()

  if user_city not in cities_list:
    update.message.reply_text(f'Города "{user_city}" нет в моем списке городов, попробуйте другой город')
  else:
    cities_list.remove(user_city)
    answer_list = []
    for city in cities_list:
      if user_city[-1].capitalize() == city[0]:
        answer_list.append(city)
    if answer_list == []:
      update.message.reply_text(f'Больше городов на букву "{user_city[-1].capitalize()}" нет в моем списке городов, вы победили.')
    else:
      answer_city = random.choice(answer_list)
      update.message.reply_text(f'"{answer_city}". Ваша очередь. Следующий город должен быть на букву "{answer_city[-1]}"')
      cities_list.remove(answer_city)


def calculator(update, context):
  user_request = update.message.text.replace(' ', '')[5:]
  print(user_request)
  numbers = user_request.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
  print(numbers)
  if '+' in user_request:
    update.message.reply_text(f'{int(numbers[0])+int(numbers[1])}')
  elif '-' in user_request:
    update.message.reply_text(f'{int(numbers[0])-int(numbers[1])}')
  elif '*' in user_request:
    update.message.reply_text(f'{int(numbers[0])*int(numbers[1])}')
  elif '/' in user_request:
    update.message.reply_text(f'{int(numbers[0])/int(numbers[1])}')


def main():
  # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater(settings.API_KEY, use_context=True)
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

  # Процессинг
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_position))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('nextfullmoon', next_full_moon))
    dp.add_handler(CommandHandler('cities', cities))
    dp.add_handler(CommandHandler('calc', calculator))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Started bot')
  # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
  # Запускаем бота, он будет работать, пока мы его не остановим принудительно  
    mybot.idle()

# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()