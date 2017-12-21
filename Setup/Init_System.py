# called at the beginning of the program to start a simulation and build all required foundations
import datetime as dt
from pathlib import Path

from Setup import Constants as Con
from Setup import Init_Stock as IS


# collect paths and load data
def init_system():
    Con.paths = collect_paths()
    Con.now = get_date()
    IS.load_stock(True)
    return


# collect paths
def collect_paths():
    basePath = Path(__file__).parents[2]  # get base path
    paths = {'Base': basePath, 'Input': (basePath / 'Input'), 'Output': (basePath / 'Output')}
    data = Path(__file__).parents[3]
    paths['Stocks'] = paths['Input'] / 'Stocks'
    return paths


# get most recent date
def get_date():
    now = dt.datetime.now()
    return(dt.datetime(now.year, now.month, now.day))
