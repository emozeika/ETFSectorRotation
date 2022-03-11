from config import AVapiKey
from av_extract import AlphaVantageExtract
import time



sectorETFList = [
    'XLE', 
    'XLB', 
    'XLI',
    'XLU',
    'XLV',
    'XLF',
    'XLY',
    'XLP',
    'XLK',
    'XLC',
    'XLRE',
    'VNQ',
    'VOX'
]


tstype = 'daily'
outputsize = 'full'
folderpath = 'raw'


#AlphaVantageExtract(AVapiKey).download_multidata(tstype, sectorETFList, outputsize, folderpath)
AlphaVantageExtract(AVapiKey).download_data(tstype, 'SPY', outputsize, folderpath)


