## QIWI-rates

Консольная утилита, которая выводит курсы валют ЦБ РФ за определенную дату.

### Использование

Для получения курса валюты с кодом *code* за дату *date* необходимо выполнить следующие команды:

```
git clone https://github.com/hamzreg/fresh-qiwi-task.git
cd ./fresh-qiwi-task/
pip3 install -r requirements.txt
cd qiwi-rates/
python3 main.py code date
```

Описание параметров:

* code - код валюты в формате ISO 4217;
* date - дата в формате YYYY-MM-DD.

### Тестирование

Для запуска тестов необходимо в директории fresh-qiwi-task/qiwi-rates/ выполнить:

```
pytest
```

```
Разработано в рамках отбора на стажировку
#FRESHQIWI, 2023
```