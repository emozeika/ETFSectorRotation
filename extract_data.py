from config import AVapiKey
from av_extract import AlphaVantageExtract






AlphaVantageExtract(AVapiKey).create_query_url('daily', 'TSLA', 'full')