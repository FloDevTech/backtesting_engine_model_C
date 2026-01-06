from enum import Enum
from models.model import TypeChange, Days


class SwapModel():
    """
    Base class for swap models.

    Attributes:
        type (TypeChange): The type of swap (e.g., MONEY, PERCENTAGE, POINT).
        swap_long (float): The swap value for long positions.
        swap_short (float): The swap value for short positions.
        day_swap (Days): The day when triple swap is charged (default: WED).
        rollover_swap_hour (float): The hour when swap is applied (default: 0).
    """
    type : TypeChange = TypeChange.PERCENTAGE
    swap_long : float = 0
    swap_short : float = 0
    day_swap : Days = Days.WED
    rollover_swap_hour : float = 0

class SwapNone(SwapModel):
    """
    Swap model representing no swap.
    """
    type = TypeChange.NONE
    swap_long : float = 0
    swap_short : float = 0
    day_swap : Days = Days.WED
    rollover_swap_hour : float = 0
    
class SwapMoney(SwapModel):
    """
    Swap model based on a fixed monetary amount.
    """
    type = TypeChange.MONEY
    swap_long : float = 0
    swap_short : float = 0
    day_swap : Days = Days.WED
    rollover_swap_hour : float = 23.5
    

class SwapPorcentage(SwapModel):
    """
    Swap model based on percentage.
    """
    type = TypeChange.PERCENTAGE
    swap_long : float = 0
    swap_short : float = 0
    day_swap : Days = Days.WED
    rollover_swap_hour : float = 23.5

class SwapPoint(SwapModel):
    """
    Swap model based on points.
    """
    type = TypeChange.POINT
    swap_long : float = 0
    swap_short : float = 0
    day_swap : Days = Days.WED
    rollover_swap_hour : float = 23.5