
from models.model import TimeFrame
from models.instrument_model import Instrument
import polars as pl
from datetime import timedelta
import re


class DataModel():
    """
    Model for handling financial data for an instrument.
    
    Attributes:
        name (str): The name of the data model.
        instrument (Instrument): The associated instrument.
        data (pl.DataFrame): The data loaded as a Polars DataFrame.
        time_frame (TimeFrame): The timeframe of the data (default: M1).
    """
    name : str = ""
    instrument: Instrument = Instrument()
    data : pl.DataFrame = None
    time_frame : TimeFrame = TimeFrame.M1
    
    def __init__(self):
        """Initializes the DataModel with default values."""
        self.name : str = ""
        self.instrument: Instrument = Instrument()
        self.data : pl.DataFrame = None
        self.time_frame : TimeFrame = TimeFrame.M1
        self._current_index : int = 0

    def load_data_from_csv(self, path_txt: str, has_header: bool = True):
        """
        Loads data from a CSV file.

        Args:
            path_txt (str): The file path to the CSV.
            has_header (bool): Indicates if the CSV has a header (default: True).

        Raises:
            Exception: If the file type is not supported.
        """
        has_header,file_type = self._get_type_file(path_txt)
        if has_header:
            df = pl.read_csv(path_txt, has_header=True)  
            if file_type == 1 :

                df = df.with_columns(
                    (
                        pl.col('date')+" "+pl.col('time')
                    ).str.strptime(pl.Datetime, "%Y.%m.%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 2:
                df = df.with_columns(
                    (
                        pl.col('date')+" "+pl.col('time')
                    ).str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 3:
                df = df.with_columns(
                    (
                        pl.col('datetime')
                    ).str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 4:
                df = df.with_columns(
                    (
                        pl.col('datetime')
                    ).str.strptime(pl.Datetime, "%Y.%m.%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            else:
                raise Exception("DataModel.load_data_from_csv: File type not supported")
        else:
            df = pl.read_csv(path_txt, has_header=False)  
            if file_type == 1 :
                df.columns = ["date","time","open","high","low","close","tickvol","volume","spread"]
                df = df.with_columns(
                    (
                        pl.col('date')+" "+pl.col('time')
                    ).str.strptime(pl.Datetime, "%Y.%m.%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 2:
                df.columns = ["date","time","open","high","low","close","tickvol","volume","spread"]
                df = df.with_columns(
                    (
                        pl.col('date')+" "+pl.col('time')
                    ).str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 3:
                df.columns = ["datetime","open","high","low","close","tickvol","volume","spread"]
                df = df.with_columns(
                    (
                        pl.col('datetime')
                    ).str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            elif file_type == 4:
                df.columns = ["datetime","open","high","low","close","tickvol","volume","spread"]
                df = df.with_columns(
                    (
                        pl.col('datetime')
                    ).str.strptime(pl.Datetime, "%Y.%m.%d %H:%M:%S").alias("datetime")
                )
                self.data = df.select(["datetime","open","high","low","close","volume"])
            else:
                raise Exception("DataModel.load_data_from_csv: File type not supported")

    def resample_data(self,
            target_timeframe: TimeFrame = TimeFrame.H1, 
         time_col: str = 'datetime',
         resampling_forward: bool = True):
        """
        Resamples the data to a specific timeframe.

        Args:
            target_timeframe (TimeFrame): The target timeframe (e.g., '1h', '4h', '1d').
            time_col (str): The name of the time column to use for resampling (default: 'datetime').
            resampling_forward (bool): Direction of resampling (default: True).

        Returns:
            pl.DataFrame: The resampled DataFrame.

        Raises:
            ValueError: If the time column does not exist.
            Exception: If an error occurs during resampling.
        """
        if time_col not in self.data.columns:
            raise ValueError(f"La columna de tiempo '{time_col}' especificada para remuestreo no existe en el DataFrame.")
        try:
            df = self.data.sort(time_col)
            # Agregaciones estándar para OHLCV
            aggregations = [
                pl.first('open').alias('open'),
                pl.max('high').alias('high'),
                pl.min('low').alias('low'),
                pl.last('close').alias('close'),
                pl.sum('volume').alias('volume')
            ]

            # Intentar agregar otras columnas numéricas con 'mean' y otras con 'first'
            # Esto es una heurística, podría necesitar ajustes
            for col in df.columns:
                if col not in [time_col, 'open', 'high', 'low', 'close', 'volume']:
                    if df[col].dtype in pl.NUMERIC_DTYPES:
                        aggregations.append(pl.mean(col).alias(col))
                    else:
                        aggregations.append(pl.first(col).alias(col))

            if resampling_forward:
                offset_hours = 0
                df_tmp=df.with_columns(
                (pl.col(time_col)+timedelta(hours=offset_hours)).alias(time_col))
            
                resampled_df = df_tmp.group_by_dynamic(
                    index_column=time_col,
                    every = target_timeframe.value,
                ).agg(aggregations)
            else:
                offset_hours = self._convert_time_to_hours(target_timeframe.value)
                df_tmp=df.with_columns(
                (pl.col(time_col)+timedelta(hours=-offset_hours)).alias(time_col))
            
                resampled_df = df_tmp.group_by_dynamic(
                    index_column=time_col,
                    every=target_timeframe.value,
                    # offset=pl.duration(minutes=-1) # Opcional
                    closed='right' 
                ).agg(aggregations)

            # logger.info(f"Datos remuestreados exitosamente. Nuevo shape: {resampled_df.shape}")
            self.data = resampled_df
        except Exception as e:
            # logger.error(f"Error durante el remuestreo a timeframe '{target_timeframe}': {e}")
            # logger.exception("Detalle del error de remuestreo:")
            # logger.warning(f"ADVERTENCIA: Falló el remuestreo a {target_timeframe}. Devolviendo datos sin remuestrear.")
            raise Exception("Error durante el remuestreo a timeframe '{target_timeframe}': {e}")

    def _convert_time_to_hours(self, time_str: str) -> float:
        """
        Converts a time string in 'XhYm' format to decimal hours.
        
        Args:
            time_str (str): Time string (e.g., '4h', '2h30m').
            
        Returns:
            float: Hours in decimal format.
            
        Examples:
            >>> _convert_time_to_hours('4h')
            4.0
            >>> _convert_time_to_hours('2h30m')
            2.5
        """
        time_str = time_str.lower()
        hours = 0.0
        minutes = 0.0
        
        # Extraer horas
        if 'h' in time_str:
            hours_part = time_str.split('h')[0]
            hours = float(hours_part)
            
        # Extraer minutos
        if 'm' in time_str:
            minutes_part = time_str.split('h')[-1].replace('m', '')
            if minutes_part:
                minutes = float(minutes_part) / 60
        # Extraer minutos
        if 'd' in time_str:
            day_part = time_str.split('d')[0].replace('d', '')
            if day_part:
                hours = float(day_part)*24

        return hours + minutes

    def _get_type_file(self, path_txt):
        """
        Determines the type of the file and whether it has a header.

        Args:
            path_txt (str): Path to the file.

        Returns:
            tuple: A tuple containing (has_header: bool, file_type: int or None).
        """
        lineas = []
        n = 3
        try:
            with open(path_txt, 'r', encoding='utf-8') as f:
                for _ in range(n):
                    lineas.append(next(f).strip()) # .strip() para limpiar saltos de línea
        except StopIteration:
            pass # El archivo tiene menos de 3 líneas
        except FileNotFoundError:
            print(f"El archivo {path_txt} no existe.")
            linea_evaluar = lineas[1]
        # if linea[0] == 'date,time,open,high,low,close,tickvol,volume,spread'
        #     and linea[1] == 'date,time,open,high,low,close,tickvol,volume,spread'
        #     and linea[2] == 'date,time,open,high,low,close,tickvol,volume,spread':
        has_header = False
        if 'date' in lineas[0].lower() or 'open' in lineas[0].lower():
            has_header = True
        file_type = None

        if len(lineas) > 1:
            linea_evaluar = lineas[1]
            # Definición de patrones Regex
            # Tipo 1: "2011.09.19,00:53:00..." (Separadores: . . ,)
            regex_tipo_1 = r"^\d{4}\.\d{2}\.\d{2},\d{2}:\d{2}:\d{2}"
            # Tipo 2: "2011-09-19,00:53:00..." (Separadores: - - ,)
            regex_tipo_2 = r"^\d{4}-\d{2}-\d{2},\d{2}:\d{2}:\d{2}"
            # Tipo 3: "2011-09.19 00:53:00..." (Separadores: - . espacio)
            regex_tipo_3 = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

            # Tipo 4: "2011.09.19 00:53:00..." (Separadores: - . espacio)
            regex_tipo_4 = r"^\d{4}.\d{2}.\d{2} \d{2}:\d{2}:\d{2}"
            # Evaluación
            if re.match(regex_tipo_1, linea_evaluar):
                file_type = 1
            elif re.match(regex_tipo_2, linea_evaluar):
                file_type = 2
            elif re.match(regex_tipo_3, linea_evaluar):
                file_type = 3
            elif re.match(regex_tipo_4, linea_evaluar):
                file_type = 4
            else:
                print(f"La línea no coincide con ninguno de los tipos conocidos: {linea_evaluar}")
        else:
            print("No hay suficientes líneas en el archivo para evaluar lineas[1].")
        return has_header, file_type
    def get_current_index(self):
        return self._current_index
    def set_current_index(self, index: int):
        self._current_index = index