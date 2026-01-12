import pytest
from models.commission_model import (
    CommissionNone,
    CommissionPoint,
    CommissionPercentage,
    CommissionMoney,
    TypeChange
)

def test_commission_none():
    """Test CommissionNone initialization and values."""
    model = CommissionNone()
    assert model.commission == 0
    assert model.type == TypeChange.NONE
    assert model.name == ""

def test_commission_point():
    """Test CommissionPoint initialization and values."""
    value = 2.0
    model = CommissionPoint(commission=value)
    assert model.commission == value
    assert model.type == TypeChange.POINT

def test_commission_percentage():
    """Test CommissionPercentage initialization and values."""
    value = 0.05
    model = CommissionPercentage(commission=value)
    assert model.commission == value
    assert model.type == TypeChange.PERCENTAGE

def test_commission_money():
    """Test CommissionMoney initialization and values."""
    value = 10.0
    model = CommissionMoney(commission=value)
    assert model.commission == value
    assert model.type == TypeChange.MONEY
