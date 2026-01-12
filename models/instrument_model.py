from models.model import DataType
from models.commission_model import CommissionNone,CommissionModel
from models.swap_model import SwapNone,SwapModel
from models.slippage_model import SlippageNone,SlippageModel

class Instrument():
    """
    Represents a financial instrument.

    Attributes:
        name (str): The name of the instrument.
        description (str): A description of the instrument.
        data_type (DataType): The type of data (e.g., STOCK, FOREX).
        point_value (float): The value of one point.
        pip_tick_size (float): The size of a pip/tick.
        pip_tick_step (float): The step size for pip/tick.
        default_spread_pip (float): The default spread in pips.
        default_slippage_pip (float): The default slippage in pips.
        order_size_multiplier (float): The multiplier for order size.
        order_size_step (float): The step size for order size.
        commission_model (CommissionModel): The commission model associated with the instrument.
        swap (SwapModel): The swap model associated with the instrument.
        slippage_model (SlippageModel): The slippage model associated with the instrument.
    """
    
    name : str = ""
    description : str = ""
    data_type : DataType = DataType.STOCK
    point_value : float = 0
    pip_tick_size : float = 0
    pip_tick_step : float = 0
    default_spread_pip : float = 0  
    default_slippage_pip : float = 0
    order_size_multiplier : float = 0
    order_size_step : float = 0
    commission_model: CommissionModel = CommissionNone()
    swap : SwapModel = SwapNone()
    slippage_model : SlippageModel = SlippageNone()

    def __init__(self ,
        name : str ="" , description : str ="",
        data_type :  DataType = DataType.STOCK, point_value : float = 0,
        pip_tick_size : float = 0, pip_tick_step : float = 0,
        default_spread_pip : float = 0, default_slippage_pip : float = 0,
        order_size_multiplier : float = 0,order_size_step : float = 0,
        commission_model: CommissionModel = CommissionNone(),swap : SwapModel = SwapNone(),
        slippage_model: SlippageModel = SlippageNone()):
        """
        Initializes the Instrument with the given parameters.

        Args:
            name (str): Name of the instrument.
            description (str): Description of the instrument.
            data_type (DataType): Type of the instrument data (default: STOCK).
            point_value (float): Value of a point (default: 0).
            pip_tick_size (float): Size of a pip/tick (default: 0).
            pip_tick_step (float): Step size of a pip/tick (default: 0).
            default_spread_pip (float): Default spread in pips (default: 0).
            default_slippage_pip (float): Default slippage in pips (default: 0).
            order_size_multiplier (float): Multiplier for order size (default: 0).
            order_size_step (float): Step size for order size (default: 0).
            commission_model (CommissionModel): Commission model (default: CommissionNone).
            swap (SwapModel): Swap model (default: SwapNone).
            slippage_model (SlippageModel): Slippage model (default: SlippageNone).
        """
        
        self.name : str = name
        self.description : str = description
        self.data_type : DataType = data_type
        self.point_value : float = point_value
        self.pip_tick_size : float = pip_tick_size
        self.pip_tick_step : float = pip_tick_step
        self.default_spread_pip : float = default_spread_pip  
        self.default_slippage_pip : float = default_slippage_pip
        self.order_size_multiplier : float = order_size_multiplier
        self.order_size_step : float = order_size_step
        self.commission_model: CommissionModel = commission_model
        self.swap : SwapModel = swap  
        self.slippage_model : SlippageModel = slippage_model
    