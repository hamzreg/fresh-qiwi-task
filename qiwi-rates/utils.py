from dataclasses import dataclass

from rate import Rate

@dataclass
class Date:
    year = 0
    month = 1
    day = 2


def handle_date(date: str):
    """
        Преобразование даты 
        из формата YYYY-MM-DD
        в формат dd/mm/yyyy.
    """

    date = date.split('-')
    return date[Date.day] + '/' + \
           date[Date.month] + '/' + \
           date[Date.year]
