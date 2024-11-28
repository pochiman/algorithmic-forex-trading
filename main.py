from api.oanda_api import OandaApi
from api.stream_prices import stream_prices
from infrastructure.instrument_collection import instrumentCollection

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    stream_prices(['GBP_JPY', 'AUD_NZD'])
