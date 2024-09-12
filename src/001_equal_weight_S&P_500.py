import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv("sp_500_stocks.csv")

from secrets import IEX_CLOUD_API_TOKEN

symbol = "AAPL"
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}"
print(api_url)
data = requests.get(api_url).json()
print(data)
