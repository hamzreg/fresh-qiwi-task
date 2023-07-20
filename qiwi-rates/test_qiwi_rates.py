from rate import Rate
from utils import handle_date


def test_get_rate():
    code = 'USD'
    date = '08/10/2022'
    value = '61,2475'
    name = 'Доллар США'

    rate = Rate(code)
    rate.get_value(date)

    assert rate.value == value
    assert rate.name == name


def test_handle_date():
    date = '2022-10-08'
    handled_date = '08/10/2022'

    result = handle_date(date)

    assert result == handled_date
