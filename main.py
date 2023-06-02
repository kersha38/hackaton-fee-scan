'''
import pdfquery
import re

from pyquery import PyQuery

pdf = pdfquery.PDFQuery("test_files/contrato2.pdf")
pdf.load()


def search_value(value):
    label = pdf.pq(f'LTTextLineHorizontal:contains("{value}")')
    print(label.text())


def read_position(value):
    label: PyQuery = pdf.pq(f'LTTextLineHorizontal:contains("{value}")')
    print(label.text())
    left_corner = float(label.attr('x0')) - 50
    bottom_label = float(label.attr('y0'))
    bottom_corner = bottom_label - 25
    right_corner = left_corner + 100
    upper_corner = bottom_label - 5
    result = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (
    left_corner, bottom_corner, right_corner, upper_corner))
    print(f'RESULT \n{result.text()}')

    result = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (
        left_corner, bottom_corner, right_corner, upper_corner)).text()

    print(f'RESULT2 \n{result.text()}')

    print("COORD", left_corner, bottom_corner, right_corner, upper_corner)

    a = pdf.pq('LTTextLineHorizontal:contains("DE -")')
    print(a.text())
    print("COORD", a.attr('x0'), a.attr('y0'), a.attr('x1'), a.attr('y1'))


def read_all(regexp):
    text_elements = pdf.pq('LTTextLineHorizontal')

    for t in text_elements:
        text = t.text
        print(text)
        isMatch = re.search(regexp, text)
        if isMatch:
            print("IS A MATCH")
            print(t.text)
'''
from constants.constants import Titles, PaymentMethod, CardType, RANGE_CLEANERS, FEE_INFO_CLEANERS
from utils.columns_parser import get_ranges, Range, Fee, get_fee_info, define_fee
from utils.pdf_utils import PDFReader


def get_fee(reader: PDFReader, title: Titles, ranges: [Range], payment_method: PaymentMethod, card_type: CardType = CardType.EMPTY):
    columns = reader.get_columns(title.value)
    fee_info = get_fee_info(columns, FEE_INFO_CLEANERS)
    return define_fee(fee_info, ranges, payment_method.value, card_type.value)


def run():
    reader = PDFReader("test_files/contrato2.pdf")
    range_columns = reader.get_columns(Titles.MONTH_TRANSACTIONS.value)
    ranges = get_ranges(range_columns, RANGE_CLEANERS)
    fees: [Fee] = [
        get_fee(reader, Titles.TRANSFER_FEE, ranges, PaymentMethod.Transfer),
        get_fee(reader, Titles.CARD_CREDIT_FEE, ranges, PaymentMethod.CARD, CardType.CREDIT),
        get_fee(reader, Titles.CARD_DEBIT_FEE, ranges, PaymentMethod.CARD, CardType.DEBIT)
    ]
    print(fees)


if __name__ == '__main__':
    run()
