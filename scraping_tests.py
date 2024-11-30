from scraping.investing_com import investing_com
from scraping.dailyfx_com import dailyfx_com
from scraping.bloomberg_com import bloomberg_com
from scraping.fx_calendar import fx_calendar

if __name__ == "__main__":
    # print(investing_com())
    # print(dailyfx_com())
    # data = bloomberg_com()
    # [print(x) for x in data]
    print(fx_calendar())
