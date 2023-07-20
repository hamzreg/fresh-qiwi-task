## QIWI-rates

Консольная утилита, которая выводит курсы валют ЦБ РФ за определенную дату.

### Использование

Для получения курса валюты с кодом *code* за дату *date* необходимо:

```
git clone https://github.com/hamzreg/fresh-qiwi-task.git
cd ./fresh-qiwi-task/
pip3 install -r requirements.
cd qiwi-rates
python3 main.py code date
```

Описание параметров:

* code - код валюты в формате ISO 4217;
* date - дата в формате YYYY-MM-DD.

```
Разработано в рамках отбора на стажировку
#FRESHQIWI, 2023
```