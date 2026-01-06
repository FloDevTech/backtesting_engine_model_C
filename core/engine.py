from Strategy.strategy import Strategy
from models.data_model import DataModel
import polars as pl

class Engine():
    """
    The core execution engine for the backtest.
    """
    def __init__(self, strategy: Strategy, data: DataModel):
        """
        Initializes the engine.
        
        Args:
            strategy (Strategy): The strategy instance to run.
            data (DataModel): The primary data feed.
        """
        self.strategy = strategy
        self.data = data
        self.strategy.data = self.data # Link data to strategy
        
        # Ensure data is sorted
        # self.data.data = self.data.data.sort("datetime") 

    def run(self):
        """
        Executes the backtest simulation.
        """
        print("Starting Backtest...")
        
        # 1. Initialization Phase
        print("Compiling Indicators...")
        self.strategy.init()
        
        # 2. Iteration Phase
        print("Running Event Loop...")
        total_steps = len(self.data.data)
        
        # Optimization: Pre-converting columns to lists or numpy arrays could be significantly faster
        # than polars item access in a Python loop. 
        # For now, keeping it robust via DataModel properties.
        
        for i in range(total_steps):
            # Update Context
            self.data.set_current_index(i)
            
            # TODO: Check for Orders/Executions here
            
            # Strategy Logic
            self.strategy.next()
            
        print("Backtest Finished.")
