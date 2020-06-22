import pandas as pd
import quandl


# acquisition functions

def get_tickers(path):
    companies =pd.read_csv(path)
    ticker_list = companies['Ticker'].to_list()
    print(f'retrieved {len(ticker_list)} companies...')
    return ticker_list


def get_prices(ticker):
    prices_full = quandl.get(f'WIKI/{ticker}')


