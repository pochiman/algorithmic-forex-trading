from bs4 import BeautifulSoup
import pandas as pd
import requests

def fx_calendar():

    session = requests.Session()

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Cookie":"calendar-importance=3; cal-custom-range=2022-03-21 00:00|2022-03-26 00:00; TEServer=TEIIS3; cal-timezone-offset=0;"
    }

    resp = session.get("https://tradingeconomics.com/calendar", headers=headers)
        
    soup = BeautifulSoup(resp.content, 'html.parser')

    table = soup.select_one("table#calendar")

    print(table)
