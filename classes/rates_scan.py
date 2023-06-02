from typing import List


class Range:
    def __init__(self, fr: int, to: int = 0):
        self.fr: int = fr
        self.to: int = to


class FeeInfo:
    def __init__(self, fixed, variable):
        self.fixed = fixed
        self.variable = variable


class RangeConfig:
    def __init__(self, rang: Range, info: FeeInfo):
        self.info: FeeInfo = info
        self.rang: Range = rang


class FeeByPaymentMethod: # Fee
    def __init__(self, range_configs: List[RangeConfig], payment_method: str, card_type=""):
        self.range_configs = range_configs
        self.card_type = card_type
        self.payment_method = payment_method
