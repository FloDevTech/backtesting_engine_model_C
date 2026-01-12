from models.model import TypeChange


class CommissionModel():
    """
    Base class for commission models.

    Attributes:
        commision (float): The commission value.
        name (str): The name of the commission model.
        type (TypeChange): The type of commission (e.g., MONEY, PERCENTAGE, POINT).
    """
    commision :float = 0
    name : str = ""
    type : TypeChange = TypeChange.NONE

    def __init__(self):
        """Initializes the CommissionModel with default values."""
        self.commision :float = 0
        self.name : str = ""
        self.type : TypeChange = TypeChange.NONE

    def __str__(self):
        """Returns a string representation of the commission model."""
        return f"{self.name} {self.type} {self.commision}" 
    
    def __repr__(self):
        """Returns a string representation of the commission model for debugging."""
        return f"{self.name} {self.type} {self.commision}" 
    
class CommissionMoney(CommissionModel):
    """
    Commission model based on a fixed monetary amount per trade/unit.
    """
    
    def __init__(self, commission: float):
        """
        Initializes the CommissionMoney model.

        Args:
            commission (float): The fixed commission amount.
        """
        self.commission :float = commission
        self.name : str = ""
        self.type : TypeChange = TypeChange.MONEY
    
class CommissionPercentage(CommissionModel):
    """
    Commission model based on a percentage of the trade value.
    """

    def __init__(self, commission: float):
        """
        Initializes the CommissionPorcentage model.

        Args:
            commission (float): The commission percentage.
        """
        self.commission :float = commission
        self.name : str = ""
        self.type : TypeChange = TypeChange.PERCENTAGE
    
class CommissionPoint(CommissionModel):
    """
    Commission model based on points/pips.
    """

    def __init__(self, commission: float):
        """
        Initializes the CommissionPoint model.

        Args:
            commission (float): The commission in points.
        """
        self.commission :float = commission
        self.name : str = ""
        self.type : TypeChange = TypeChange.POINT
    

class CommissionNone(CommissionModel):
    """
    Commission model representing no commission.
    """

    def __init__(self):
        """
        Initializes the CommissionNone model.
        """
        self.commission :float = 0
        self.name : str = ""
        self.type : TypeChange = TypeChange.NONE