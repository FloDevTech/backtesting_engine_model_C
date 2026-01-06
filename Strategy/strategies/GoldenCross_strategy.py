
from models.data_model import DataModel
from Strategy.strategy import Strategy
class GoldenCross_strategy(Strategy):
    def __init__(self, data: DataModel):
        super().__init__(data=data)
    
    def init(self):
        pass
    
    def next(self):
        idx = self.data.get_current_index()
        # print(idx, self.data.data[:idx]['close'])
        print(idx)