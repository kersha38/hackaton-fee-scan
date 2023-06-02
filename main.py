from dotenv import load_dotenv
from constants.constants import Titles, PaymentMethod, CardType, RANGE_CLEANERS, FEE_INFO_CLEANERS
from utils.columns_parser import get_ranges, get_fee_info, define_fee
from utils.pdf_utils import PDFReader
from dynamo_gateway.dynamo_client import *


def get_fee(
        reader: PDFReader,
        title: Titles,
        ranges: [Range],
        payment_method: PaymentMethod,
        card_type: CardType = CardType.EMPTY
):
    columns = reader.get_columns(title.value)
    fee_info = get_fee_info(columns, FEE_INFO_CLEANERS)
    return define_fee(fee_info, ranges, payment_method.value, card_type.value)


def run():
    dynamo_session = init_dynamo()
    reader = PDFReader("test_files/contrato2.pdf")
    range_columns = reader.get_columns(Titles.MONTH_TRANSACTIONS.value)
    ranges = get_ranges(range_columns, RANGE_CLEANERS)
    fees: List[FeeByPaymentMethod] = [
        get_fee(reader, Titles.TRANSFER_FEE, ranges, PaymentMethod.Transfer),
        get_fee(reader, Titles.CARD_CREDIT_FEE, ranges, PaymentMethod.CARD, CardType.CREDIT),
        get_fee(reader, Titles.CARD_DEBIT_FEE, ranges, PaymentMethod.CARD, CardType.DEBIT)
    ]
    print(fees)

    rates_dynamo = build_rates_dynamo(fees)

    write_rates_dynamo(rates_dynamo, dynamo_session)


def init_dynamo():
    table_name = 'usrv-transaction-rates-' + os.environ['ENV'] + '-configurations'
    return init_dynamo_session(table_name)


def build_rates_dynamo(fees_scan: List[FeeByPaymentMethod]):
    return create_rates_item(fees_scan)


def write_rates_dynamo(items, dynamo_session):
    for item in items:
        put_item(item, dynamo_session)


if __name__ == '__main__':
    load_dotenv()
    run()
