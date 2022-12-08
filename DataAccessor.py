import abc
import pandas as pd

class BaseDataAccessor(abc.ABC):
    @abc.abstractclassmethod
    def get_all(self):
        pass

    @abc.abstractclassmethod
    def get_row_by_idx(self, idx):
        pass

    @abc.abstractclassmethod
    def del_row_by_idx(self, idx):
        pass


class DataAccessor(BaseDataAccessor):
    def __init__(self, df):
        self.df = df

        #initial features
        self.holiday = self.df['holiday']
        self.temp = self.df['temp']
        self.rain = self.df['rain_1h']
        self.snow = self.df['snow_1h']
        self.clouds = self.df['clouds_all']
        self.weather_main = self.df['weather_main']
        self.weather_desc = self.df['weather_description']
        self.date_time = self.df['date_time']

        #target
        self.traffic = self.df['traffic_volume']

        self.precipitation = []
        self.precipitation.extend([self.df['rain_1h'], self.df['snow_1h']])

        self.weather = []
        self.weather.extend([self.df['weather_main'], 
                             self.df['weather_description']])

    def get_all(self) -> pd.DataFrame:
        return self.df

    def get_row_by_idx(self, idx: int) -> pd.Series:
        return self.df.iloc[idx]

    def del_row_by_idx(self, idx: int) -> None:
        self.df.drop(idx, axis=0, inplace=True)