# %%
import pandas as pd
import requests
from datetime import datetime, timedelta
# %%
stock_list_df = pd.read_csv("stock_list.txt", header=None)
# target_stock_no = stock_list_df[0].unique()[500:505]
target_stock_no = ['3037']
# %%
# crawler init
month_first_day = datetime.now().replace(day=1)
month_scope = 12
date_list = [(month_first_day - pd.DateOffset(months=n)).strftime("%Y%m%d") for n in range(month_scope)]
# %%
each_stock_price = pd.DataFrame()
for stock_no in target_stock_no:
    for date in date_list:
        no = stock_no
        try:
            data = requests.get(f"https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date={date}&stockNo={no}")
        except:
            continue
        data = data.json()
        stock_title = data['title'].split(' ')[2]
        stock_no = no
        price_df = pd.DataFrame(data["data"], columns=["date", "closing price"])
        price_df = price_df[:-1].copy() # drop last row (月平均價格)
        each_stock_price = pd.concat([each_stock_price, price_df])

    
# %%
