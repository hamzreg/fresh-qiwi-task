import requests
import xmltodict

from dataclasses import dataclass


@dataclass
class Resource:
    central_bank = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='


@dataclass
class ResourceFields:
    code = 'CharCode'
    name = 'Name'
    value = 'Value'


class Rate():
    def __init__(self, code):
        self.code = code
        self.name = None
        self.value = None


    def get_value(self, date: str):
        """
            Получение курса валюты
            на дату date.
        """

        rates = self.__get_rates(date)
        
        for rate in rates:
            if rate[ResourceFields.code] == self.code:
                self.name = rate[ResourceFields.name]
                self.value = rate[ResourceFields.value]

                return

        print(f'Не найдена информация о валюте с кодом {self.code}.')


    def print_data(self, date):
        """
            Вывод информации о валюте.
        """

        if self.name is not None and self.value is not None:
            print(f'{self.code} ({self.name}): {self.value}')
        else:
            print(f'Не удалось получить информацию.')


    def __get_rates(self, date: str):
        """
            Получение курсов валют
            на дату date.
        """

        rates = []

        try:
            r = requests.get(Resource.central_bank + date)
            r.raise_for_status()

            rates = xmltodict.parse(r.text)
            rates = rates['ValCurs']['Valute']
        except requests.exceptions.HTTPError as errh:
            print("Неудачный запрос:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Ошибка соединения:", errc)
        except requests.exceptions.Timeout as errt:
            print("Время ожидания ответа истекло:", errt)
        except requests.exceptions.JSONDecodeError as errd:
            print("Ошибка декодирования:", errd)
        except requests.exceptions.RequestException as err:
            print("Что-то пошло не так:", err)
        
        return rates
