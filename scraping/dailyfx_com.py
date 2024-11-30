from bs4 import BeautifulSoup
import pandas as pd
import requests

def dailyfx_com():

    resp = requests.get("https://www.dailyfx.com/sentiment")
    
    # print(resp.content)
    # print(resp.status_code)
    
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # print(soup)
    
    rows = soup.select(".dfx-technicalSentimentCard")

    for r in rows:
        print()
        card = r.select_one(".dfx-technicalSentimentCard__pairAndSignal")
        print(card.select_one('a').get_text().replace("/", "_"))
        print(card.select_one('span').get_text())
        change_values = r.select(".dfx-technicalSentimentCard_changeValue")
        print(change_values[0].get_text())
        print(change_values[1].get_text())
        print(change_values[3].get_text())
        print(change_values[4].get_text())
