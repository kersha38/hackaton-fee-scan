from enum import Enum

CELL_WIDTH = 100
CELL_HEIGHT = 8


class Titles(Enum):
    MONTH_TRANSACTIONS = "Transacciones Mes"
    CARD_CREDIT_FEE = "Tarifa Tarjeta Crédito"
    CARD_DEBIT_FEE = "Tarifa Tarjeta Débito"
    TRANSFER_FEE = "Tarifa Transfer"


class CardType(Enum):
    DEBIT = "Debit"
    CREDIT = "Credit"
    EMPTY = ""


class PaymentMethod(Enum):
    CARD = "Card"
    Transfer = "Transfer"


# add as many cleaners as you need
RANGE_CLEANERS = ['En adelante', 'De', '-', ' ', '–', '/', '.']
FEE_INFO_CLEANERS = ['%', '$', 'COP']
RANGES_SEPARATORS = 'Hasta'
FEE_SEPARATORS = ' + '
