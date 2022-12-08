import pandas as pd
import numpy as np

def calc_season(date_time_str):
    month = date_time_str.split('-')[1]
    if month in ['09', '10', '11']:
        return 'autumn'
    elif month in  ['06', '07', '08']:
        return 'summer'
    elif month in ['03', '04', '05']:
        return 'spring'
    elif month in ['12', '01', '02']:
        return 'winter'
    else:
        raise ValueError(month)

class Formulas:
    def precipitation_total(data):
        return(sum(data.precipitation))

    def temp_in_celcius(data):
        return data.temp - 273

    def hot(data):
        return data.temp > 300

    def cold(data):
        return data.temp < 263

    def rainy_and_cloudy(data):
        return (data.rain > 0.1)&(data.clouds > 50)

    def is_holiday(data):
        return data.holiday != 'None'

    def year(data):
        return pd.to_datetime(data.date_time).dt.year

    def month(data):
        return pd.to_datetime(data.date_time).dt.month

    def day(data):
        return pd.to_datetime(data.date_time).dt.day

    def weekday(data):
        return pd.to_datetime(data.date_time).dt.weekday

    def hour(data):
        return pd.to_datetime(data.date_time).dt.hour

    def is_day_off(data):
        return pd.to_datetime(data.date_time).dt.weekday.isin([5, 6])

    def season(data):
        return data.date_time.apply(calc_season)

    def weather(data):
        return data.weather_main

    def traffic_cat(data):
        return pd.qcut(data.traffic, q=np.arange(0, 1.2, 0.2), labels=range(0, 5))


class Features:
    def compute(data, include_initial=False):
        feats = [feat(data) for feat in Formulas.__dict__.values() if callable(feat)]
        cols = [feat.__name__ for feat in Formulas.__dict__.values() if callable(feat)]
        new_feats = pd.concat(feats, axis=1)
        new_feats.columns = cols
        if include_initial:
            return pd.concat([data.df, new_feats], axis=1)
        return new_feats