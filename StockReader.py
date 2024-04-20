import numpy as np
import pandas as pd

class StockReader:

    def read_stocks(self):
        all_data = pd.read_csv("./data/stocklist.csv")
        list_of_stocks = all_data["Symbol"].tolist()
        return list_of_stocks

    def stock_exists(self, stock_name):
        if stock_name in self.read_stocks():
            return True
        else:
            return False

