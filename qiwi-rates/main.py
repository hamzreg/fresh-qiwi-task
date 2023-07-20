import argparse

from utils import handle_data
from rate import Rate


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='код валюты в формате ISO 4217')
    parser.add_argument('date', help='дата в формате YYYY-MM-DD')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    date = handle_data(args.date)
    rate = Rate(args.code)

    rate.get_value(date)
    rate.print_data(date)
