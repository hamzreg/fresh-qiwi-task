## QIWI-rates

Консольная утилита, которая выводит курсы валют ЦБ РФ за определенную дату.


### Использование

Для получения курса валюты с кодом *code* за дату *date* необходимо:

```
git clone 
cd ./fresh-qiwi-task/qiwi-rates/
pip3 install -r requirements.txt
python3 corrency_rates.py code date
```

Описание параметров:

* code - код валюты в формате ISO 4217;
* date - дата в формате YYYY-MM-DD.
