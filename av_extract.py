import requests
import pandas as pd


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
        self.data = None

    def create_query_url(self, timeseriestype, ticker, outputsize):
        ''' 
        Formats the query url string for KLINE data given the parameters. 
        '''

        self.queryURL = self.baseURL + f'function={self.functionMapping.get(timeseriestype)}&symbol={ticker}&outputsize={outputsize}&apikey={self.apiKey}'


        

    def request_kline_data(self, timeseriestype, ticker, outputsize):
        '''
        Requests kline data in json and returns the json response
        '''
        self.create_query_url(timeseriestype, ticker, outputsize)
        self.data = requests.get(self.queryURL).json()
        


    def parse_kline_data(self, timeseriestype, ticker, outputsize):
        '''
        Parses the OHLCV data out of the json response and stores into pandas dataframe
        '''
        data = []

        self.request_kline_data(timeseriestype, ticker, outputsize)       
        for key in self.data.keys():
            if key != 'Meta Data':
                for date in self.data[key].keys():
                    curr_date = [date]
                    for price, value in self.data[key][date].items():
                        curr_date.append(value)
                    data.append(curr_date)
        
        data = pd.DataFrame(data, columns= ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        data = data.sort_values(by='Date')
        return data

    def download_data(self, timeseriestype, ticker, outputsize):
        ''' 
        Download OHLCV data for stocks and store into csv
        '''
        data = self.parse_kline_data(timeseriestype, ticker, outputsize)
        
        data.to_csv(f'raw/{ticker}_{timeseriestype}.csv')

                   






    def request_data(self, timeseriestype, ticker, outputsize):
        ''' 
        Wrapper function to handle different data requests. KLINE, Fundemental, Indicators, etc...

        '''


