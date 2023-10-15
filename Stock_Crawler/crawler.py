# %%
import pandas as pd
import requests
from datetime import datetime, timedelta
# %%
# %%
month_first_day = datetime.now().replace(day=1)
month_scope = 12
date_list = [(month_first_day - pd.DateOffset(months=n)).strftime("%Y%m%d") for n in range(month_scope)]
each_stock_price = pd.DataFrame()
for date in date_list:
    no = '3037'
    data = requests.get(f"https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date={date}&stockNo={no}")
    data = data.json()
    stock_title = data['title'].split(' ')[2]
    stock_no = no
    price_df = pd.DataFrame(data["data"], columns=["date", "closing price"])
    price_df = price_df[:-1].copy() # drop last row (月平均價格)
    each_stock_price = pd.concat([each_stock_price, price_df])

    
# %%
