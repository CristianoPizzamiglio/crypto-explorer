# -*- coding: utf-8 -*-
"""
@author: Cristiano Pizzamiglio

"""
from __future__ import annotations

from datetime import datetime

import pandas as pd
from pycoingecko import CoinGeckoAPI


def main() -> None:
    """
    Get data from CoinGeckoAPI and write data to an Excel file.

    """
    cg = CoinGeckoAPI()
    data = cg.get_coins_markets("usd")
    data_df = pd.DataFrame(data)
    data_df.drop(["image", "roi"], axis=1, inplace=True)
    data_df.columns = [label.replace("_", " ").title() for label in data_df.columns]
    write_worksheet(data_df)
    

def write_worksheet(data_df: pd.DataFrame) -> None:
    """
    Write data to an Excel file.    

    Parameters
    ----------
    data_df : pd.DataFrame

    """
    date_time = datetime.now()
    current_date_time = date_time.strftime("%Y_%m_%d_%H_%M_%S")
    workbook_title = f"{current_date_time}_crypto_data.xlsx"

    with pd.ExcelWriter(workbook_title, engine='xlsxwriter') as writer:
        sheet_name = "Data"
        data_df.to_excel(writer, index=False, na_rep="NA", sheet_name=sheet_name)
        worksheet = writer.sheets[sheet_name]
        (max_row, max_col) = data_df.shape
        worksheet.autofilter(0, 0, max_row, max_col - 1)
        worksheet.set_column(0, max_col - 1, 30)

    
if __name__ == "__main__":
    main()
    