import pytest
from models.swap_model import (
    SwapNone,
    SwapPoint,
    SwapPorcentage,
    SwapMoney,
    TypeChange,
    Days
)

def test_swap_none():
    """Test SwapNone initialization and values."""
    model = SwapNone()
    assert model.swap_long == 0
    assert model.swap_short == 0
    assert model.type == TypeChange.NONE
    assert model.day_swap == Days.WED
    assert model.rollover_swap_hour == 0

def test_swap_money():
    """Test SwapMoney defaults."""
    model = SwapMoney()
    # Assuming defaults are 0 if not set, checking type specifically
    assert model.type == TypeChange.MONEY
    assert model.rollover_swap_hour == 23.5

def test_swap_percentage():
    """Test SwapPorcentage defaults."""
    model = SwapPorcentage()
    assert model.type == TypeChange.PERCENTAGE
    assert model.rollover_swap_hour == 23.5

def test_swap_point():
    """Test SwapPoint defaults."""
    model = SwapPoint()
    assert model.type == TypeChange.POINT
    assert model.rollover_swap_hour == 23.5
