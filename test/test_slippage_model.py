import pytest
from models.slippage_model import (
    SlippageNone,
    SlippagePoint,
    SlippagePercentage,
    SlippageMoney,
    TypeChange
)

def test_slippage_none():
    """Test SlippageNone initialization and values."""
    model = SlippageNone()
    assert model.slippage == 0
    assert model.type == TypeChange.NONE
    assert model.name == ""

def test_slippage_point():
    """Test SlippagePoint initialization and values."""
    value = 5.0
    model = SlippagePoint(slippage=value)
    assert model.slippage == value
    assert model.type == TypeChange.POINT

def test_slippage_percentage():
    """Test SlippagePercentage initialization and values."""
    value = 0.01
    model = SlippagePercentage(slippage=value)
    assert model.slippage == value
    assert model.type == TypeChange.PERCENTAGE

def test_slippage_money():
    """Test SlippageMoney initialization and values."""
    value = 2.5
    model = SlippageMoney(slippage=value)
    assert model.slippage == value
    assert model.type == TypeChange.MONEY

