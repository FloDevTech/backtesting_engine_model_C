from abc import ABC, abstractmethod
from typing import List, Optional, Any
from models.data_model import DataModel

class Strategy(ABC):
    """
    Abstract Base Class for all trading strategies.
    
    Attributes:
        data (DataModel): The primary data feed for the strategy.
        datas (List[DataModel]): List of all available data feeds.
        params (dict): Dictionary of strategy parameters.
    """

    def __init__(self, data: Optional[DataModel] = None, datas: Optional[List[DataModel]] = None, params: Optional[dict] = None):
        """
        Initializes the strategy with data and parameters.
        
        Args:
            data (DataModel, optional): Primary data feed.
            datas (List[DataModel], optional): All data feeds.
            params (dict, optional): Strategy parameters.
        """
        self.data = data
        self.datas = datas if datas else ([data] if data else [])
        self.params = params if params else {}
        # self.broker = None # TODO: Inject Broker
        # self.position = None # TODO: Inject Position

    @abstractmethod
    def init(self):
        """
        Initialization method called once before the start of the backtest.
        Use this method to:
        - Calculate indicators (Polars expressions).
        - Pre-compute logic.
        - Define artifacts.
        """
        pass
    @abstractmethod
    def notify_order(self, order):
        """
        Method called when an order is updated.
        Use this method to:
        - Check conditions.
        - Place orders (buy/sell).
        - Manage positions.
        """
        pass
    @abstractmethod
    def notify_position(self, position):
        """
        Method called when a position is updated.
        Use this method to:
        - Check conditions.
        - Place orders (buy/sell).
        """
        pass
    @abstractmethod
    def notify(self, event):
        """
        Method called on every new event (e.g., new bar/tick).
        Use this method to:
        - Check conditions.
        - Place orders (buy/sell).
        - Manage positions.
        """
        pass
