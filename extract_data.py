import yfinance as yf 


apiKey = 'ASWAK34G8POG9LJS'


baseURL = 'https://www.alphavantage.co/query?'


class AlphaVantageExtract:
    baseURL = 'https://www.alphavantage.co/query?'

    functionMapping = {
        'intraday' : 'TIME_SERIES_INTRADAY',
        'daily' : 'TIME_SERIES_DAILY',
        'weekly' : 'TIME_SERIES_WEEKLY',
        'monthly' : 'TIME_SERIES_MONTHLY'
    }

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.queryURL = ''

    def create_query_url(self, timeseriestype, ticker, outputsize):
        self.queryURL = self.baseURL + f'function={timeseriestype}&symbol={ticker}apikey={self.apiKey}'
        print(self.queryURL)    
AlphaVantageExtract('ERIC').create_query_url('daily', 'TSLA', 'full')