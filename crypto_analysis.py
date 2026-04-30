import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import numpy as np
import datetime

start = '2016-01-01'
end = datetime.date.today().isoformat()

btc = yf.download('BTC-USD', start=start, end=end, progress=False)['Close'].rename('BTC').to_frame()
sp500 = pdr.DataReader('SP500', 'fred', start=start, end=end).rename(columns={'SP500':'SP500'})

# Align the two data sources and keep matching business days
prices = btc.join(sp500, how='inner')
prices = prices.dropna()
returns = prices.pct_change().dropna()

cor = returns[['BTC','SP500']].corr().iloc[0,1]
vol_btc = returns['BTC'].std() * np.sqrt(252)
vol_sp = returns['SP500'].std() * np.sqrt(252)
vol_ratio = vol_btc/vol_sp

cum = (1+returns['SP500']).cumprod()
peak = cum.cummax()
drawdown = (cum/peak - 1)
crashes = drawdown.nsmallest(5)

print('Correlation (daily simple returns):', cor)
print('Annualized volatility BTC:', vol_btc)
print('Annualized volatility SP500:', vol_sp)
print('Volatility ratio BTC/SP500:', vol_ratio)
print('Top drawdowns dates and values:')
print(crashes)
for date, val in crashes.iteritems():
    start_date = date - pd.Timedelta(days=30)
    window = returns.loc[start_date:date]
    print('\nCrash ending', date.date(), 'SP500 drawdown', val)
    print('BTC return over last 30 days:', (window['BTC']+1).prod()-1)
    print('SP500 return over last 30 days:', (window['SP500']+1).prod()-1)
