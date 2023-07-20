from dataclasses import dataclass

from rate import Rate

@dataclass
class Date:
    year = 0
    month = 1
    day = 2


def handle_data(date: str):
    """
        Преобразование даты 
        из формата YYYY-MM-DD
        в формат dd/mm/yyyy.
    """

    date = date.split('-')
    return date[Date.day] + '/' + \
           date[Date.month] + '/' + \
           date[Date.year]


# def print_exchange_rate(rate: Rate):
#     """
#         Вывод результата.
#     """

#     if rate is not None:
#         print(f'{rate.code} ({rate.name}): {rate.value}')
