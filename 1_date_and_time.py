from datetime import datetime, timedelta

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    day30 = today - timedelta(days=30)

    return 'Вчера: {:%d-%m-%Y}, Сегодня: {:%d-%m-%Y}, 30 дней назад: {:%d-%m-%Y}'.format(yesterday, today, day30)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print(print_days())
    print(str_2_datetime("01/01/20 12:10:03.234567"))
