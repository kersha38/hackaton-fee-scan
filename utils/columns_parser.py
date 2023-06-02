from constants.constants import RANGES_SEPARATORS, FEE_SEPARATORS


class Range:
    def __init__(self, fr: int, to: int = 0):
        self.fr: int = fr
        self.to: int = to


class FeeInfo:
    def __init__(self, fixed, variable, ):
        self.fixed: float = fixed
        self.variable: float = variable


class RangeConfig:
    def __init__(self, rang: Range, info: FeeInfo):
        self.info: FeeInfo = info
        self.rang: Range = rang


class Fee:
    def __init__(self, range_configs: [RangeConfig], payment_method: str, card_type=""):
        self.range_configs: [RangeConfig] = range_configs
        self.card_type: str = card_type
        self.payment_method: str = payment_method


def clean_column(column: str, cleaners: [str]):
    clean = column
    for cleaner in cleaners:
        clean = clean.replace(cleaner, '')

    return clean


def get_ranges(columns, cleaners: [str]):
    ranges: [Range] = []
    r: Range
    for column in columns:
        text = column.text
        clean: str = clean_column(text, cleaners)
        limits = clean.split(RANGES_SEPARATORS)
        if len(limits) > 1:
            r = Range(int(limits[0]), int(limits[1]))
        else:
            r = Range(int(limits[0]))
        ranges.append(r)
    return ranges


def get_fee_info(columns, cleaners: [str]):
    info: [FeeInfo] = []
    current_info: FeeInfo
    for column in columns:
        clean = clean_column(column.text, cleaners)
        limits = clean.split(FEE_SEPARATORS)
        current_info = FeeInfo(limits[0], limits[1])
        info.append(current_info)
    return info


def define_fee(fee_info: [FeeInfo], ranges: [Range], payment_method: str, card_type=""):
    range_configs: [RangeConfig] = []
    for i, info in enumerate(fee_info):
        range_config = RangeConfig(ranges[i], info)
        range_configs.append(range_config)

    return Fee(range_configs, payment_method, card_type)
