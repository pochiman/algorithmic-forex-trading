import threading
import time
from stream_bot.trade_settings_collection import tradeSettingsCollection
from stream_example.stream_prices import PriceStreamer


def run_bot():
    tradeSettingsCollection.load_trade_settings()
    tradeSettingsCollection.print_collection()


    shared_prices = {}
    shared_prices_events = {}
    shared_prices_lock = threading.Lock()

    for p in tradeSettingsCollection.pair_list():
        shared_prices_events[p] = threading.Event()
        shared_prices[p] = {}

    threads = []
    
    price_stream_t = PriceStreamer(shared_prices, shared_prices_lock, shared_prices_events)
    price_stream_t.daemon = True
    threads.append(price_stream_t)
    price_stream_t.start()

    
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    print("ALL DONE")
    