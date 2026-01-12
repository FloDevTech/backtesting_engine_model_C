import pytest
from models.instrument_model import Instrument
from models.commission_model import CommissionMoney
from models.swap_model import SwapPoint
from models.slippage_model import SlippagePercentage, SlippageNone
from models.model import DataType, TypeChange

def test_instrument_defaults():
    """Test Instrument initialization with default values."""
    instrument = Instrument(name="DEFAULT")
    assert instrument.name == "DEFAULT"
    assert instrument.data_type == DataType.STOCK
    
    # Check default embedded models
    assert instrument.commission_model.type == TypeChange.NONE
    assert instrument.swap.type == TypeChange.NONE
    assert isinstance(instrument.slippage_model, SlippageNone)

def test_instrument_custom_models():
    """Test Instrument initialization with custom models."""
    comm_model = CommissionMoney(commission=5.0)
    swap_model = SwapPoint()
    slip_model = SlippagePercentage(slippage=0.01)

    instrument = Instrument(
        name="CUSTOM",
        commission_model=comm_model,
        swap=swap_model,
        slippage_model=slip_model
    )

    assert instrument.commission_model.commission == 5.0
    assert instrument.commission_model.type == TypeChange.MONEY
    
    assert instrument.swap.type == TypeChange.POINT
    
    assert instrument.slippage_model.slippage == 0.01
    assert instrument.slippage_model.type == TypeChange.PERCENTAGE

def test_instrument_attributes():
    """Test other Instrument attributes."""
    instrument = Instrument(
        name="TEST",
        point_value=10,
        pip_tick_size=0.0001
    )
    assert instrument.point_value == 10
    assert instrument.pip_tick_size == 0.0001
