# called at the beginning of the program to start a simulation and build all required foundations
import datetime as dt
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from Setup import Constants as Con
from Setup import Init_Stock as IS


# collect paths and load data
def init_system():
    Con.paths = collect_paths()
    connect_google_sheets()
    Con.now = get_date()
    IS.load_stock(True)
    return


# collect paths
def collect_paths():
    basePath = Path(__file__).parents[2]  # get base path
    paths = {'Base': basePath, 'Input': (basePath / 'Input'), 'Output': (basePath / 'Output')}
    data = Path(__file__).parents[3]
    paths['Stocks'] = paths['Input'] / 'Stocks'
    paths['Storage'] = paths['Input'] / 'Storage'
    return paths


# get most recent date
def get_date():
    now = dt.datetime.now()
    return(dt.datetime(now.year, now.month, now.day))


def connect_google_sheets():
    Con.creds = ServiceAccountCredentials.from_json_keyfile_name(Con.paths['Storage'] / str('client_secret.json'),
                                                                 Con.scope)
    Con.client = gspread.authorize(Con.creds)

    Con.sheet = Con.client.open(Con.outputfile).sheet1
    Con.row_count = Con.sheet.row_count

    if Con.row_count < 1:
        print("\n\nOUTPUT IS NOT CONNECTED\n\n")
    else:
        print("\n\nOutput file is connected\n\n")
        return
