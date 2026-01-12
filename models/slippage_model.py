from models.model import TypeChange


class SlippageModel():
    """
    Base class for slippage models.

    Attributes:
        slippage (float): The slippage value.
        name (str): The name of the slippage model.
        type (TypeChange): The type of slippage (e.g., MONEY, PERCENTAGE, POINT).
    """
    slippage :float = 0
    name : str = ""
    type : TypeChange = TypeChange.NONE

    def __init__(self):
        """Initializes the SlippageModel with default values."""
        self.slippage :float = 0
        self.name : str = ""
        self.type : TypeChange = TypeChange.NONE

    def __str__(self):
        """Returns a string representation of the slippage model."""
        return f"{self.name} {self.type} {self.slippage}" 
    
    def __repr__(self):
        """Returns a string representation of the slippage model for debugging."""
        return f"{self.name} {self.type} {self.slippage}" 
    
class SlippageMoney(SlippageModel):
    """
    Slippage model based on a fixed monetary amount per trade/unit.
    """
    
    def __init__(self, slippage: float):
        """
        Initializes the SlippageMoney model.

        Args:
            slippage (float): The fixed slippage amount.
        """
        self.slippage :float = slippage
        self.name : str = ""
        self.type : TypeChange = TypeChange.MONEY
    
class SlippagePercentage(SlippageModel):
    """
    Slippage model based on a percentage of the trade value.
    """

    def __init__(self, slippage: float):
        """
        Initializes the SlippagePercentage model.

        Args:
            slippage (float): The slippage percentage.
        """
        self.slippage :float = slippage
        self.name : str = ""
        self.type : TypeChange = TypeChange.PERCENTAGE
    
class SlippagePoint(SlippageModel):
    """
    Slippage model based on points/pips.
    """

    def __init__(self, slippage: float):
        """
        Initializes the SlippagePoint model.

        Args:
            slippage (float): The slippage in points.
        """
        self.slippage :float = slippage
        self.name : str = ""
        self.type : TypeChange = TypeChange.POINT
    

class SlippageNone(SlippageModel):
    """
    Slippage model representing no slippage.
    """

    def __init__(self):
        """
        Initializes the SlippageNone model.
        """
        self.slippage :float = 0
        self.name : str = ""
        self.type : TypeChange = TypeChange.NONE
