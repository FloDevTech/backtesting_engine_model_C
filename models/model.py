from enum import Enum


class DataType(Enum):
    """
    Enum representing different types of financial data.

    Attributes:
        STOCK: Stocks.
        FUTURES: Futures.
        FOREX: Foreign Exchange.
        CFD: Contracts for Difference.
        ETF: Exchange Traded Funds.
        INDEX: Indices.
        CRYPTO: Cryptocurrencies.
    """
    STOCK = 0 
    FUTURES = 1
    FOREX = 2
    CFD = 3
    ETF = 4
    INDEX = 5
    CRYPTO = 6

class TypeChange(Enum):
    """
    Enum representing types of changes or adjustments (commission, swap).

    Attributes:
        NONE: No change.
        PERCENTAGE: Percentage-based change.
        MONEY: fixed monetary amount change.
        POINT: Point/pip-based change.
    """
    NONE = 0
    PERCENTAGE = 1
    MONEY = 2
    POINT = 3


class Days (Enum):
    """
    Enum representing days of the week.
    """
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

class TimeFrame(Enum):
    """
    Enum representing different timeframes for data.
    """
    M1 = "1m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1h"
    H2 = "2h"
    H3 = "3h"
    H4 = "4h"  
    H6 = "6h"
    H8 = "8h"
    H12 = "12h"
    D = "1d"
    W = "1w"
    MO = "1mo"



