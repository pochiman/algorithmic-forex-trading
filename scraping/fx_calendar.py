from bs4 import BeautifulSoup
import pandas as pd
import requests
from dateutil import parser

def get_date(c):
    tr = c.select_one("tr")
    ths = list(tr.select("th"))
    for th in ths:
        if th.has_attr("colspan"):
            date_text = th.get_text().strip()
            return parser.parse(date_text)
    return None   

def fx_calendar():

    session = requests.Session()

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Cookie":"calendar-importance=3; cal-custom-range=2022-03-28 00:00|2022-04-02 00:00; TEServer=TEIIS3; cal-timezone-offset=0;"
    }

    resp = session.get("https://tradingeconomics.com/calendar", headers=headers)
        
    soup = BeautifulSoup(resp.content, 'html.parser')

    table = soup.select_one("table#calendar")

    last_header_date = None

    for c in table.children:
        if c.name == 'thead':
            if 'class' in c.attrs and 'hidden-head' in c.attrs['class']:
                continue
            last_header_date = get_date(c)
            print(last_header_date)
