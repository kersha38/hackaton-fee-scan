import uuid
import time
from classes.rates_scan import *


def get_timestamp():
    return int(time.time() * 1000)


class RateConfiguration:
    def __init__(self, fixed_amount, greater_than, variable_amount):
        self.fixedAmount = variable_amount
        self.greaterThan = greater_than
        self.variableAmount = fixed_amount

    def get_dict(self):
        return vars(self)


class RatesDynamo:
    def __init__(self, mid: str, fee: FeeByPaymentMethod):
        card_types = []
        condition_list = None
        rates = []
        if fee.card_type:
            card_types.append(fee.card_type)
            condition_list = "cardType"
        payment_method = fee.payment_method
        alias = f"Fee {payment_method} {card_types[0] if len(card_types) else ''}"

        for index, config in enumerate(fee.range_configs):
            greater_than = config.rang.fr
            fixed_amount = config.info.fixed
            variable_amount = config.info.variable
            rates_dict = RateConfiguration(fixed_amount, greater_than, variable_amount).get_dict()
            if index == 0:
                rates.append(rates_dict)
                rates.append(rates_dict)
            else:
                rates.append(rates_dict)

        self.id: str = str(uuid.uuid4())
        self.alias: str = alias
        self.applyChangesDay: int = get_timestamp()
        self.cardPaymentType: List[str] = []
        self.cardType: List[str] = card_types
        self.conditionList: List[str] = [condition_list]
        self.configuration: List[RateConfiguration] = rates
        self.country = "Colombia"
        self.created = get_timestamp()
        self.createdBy = "automatic admin"
        self.createdMerchant = get_timestamp()
        self.currency = "COP"
        self.description = f'Description for {alias}'
        self.evaluatePeriod = 1
        self.maximumAmount = 0
        self.minimumAmount = 0
        self.paymentMethod: List[str] = [payment_method]
        self.paymentType = "payIn"
        self.publicMerchantId: str = mid
        self.ratesType = "1"
        self.taxId = "345654327"
        # data hardcoded for demo porpoises.

    def get_dict(self):
        return vars(self)

