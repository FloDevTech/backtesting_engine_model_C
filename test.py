import polars as pl
import plotly


from models.model import TimeFrame
from models.model import DataType
from models.model import TypeChange
from models.model import Days
from models.commission_model import CommissionPorcentage
from models.swap_model import SwapModel,SwapMoney,SwapPorcentage,SwapPoint,SwapNone
from models.instrument_model import Instrument
from models.data_model import DataModel



data_nmodel = DataModel()

path_txt = './data/NDXm.csv'
data_nmodel.load_data_from_csv(path_txt)
print(data_nmodel.data)


data_nmodel.resample_data(TimeFrame.H1) 
print(data_nmodel.data)