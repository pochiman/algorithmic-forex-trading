from bs4 import BeautifulSoup
import pandas as pd
import requests
import cloudscraper


def investing_com():

    s = cloudscraper.create_scraper()

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Referer":"https://www.google.com/",
        "Accept":"*/*",
        "Accept-Language":"en-GB,en;q=0.5",
        "Pragma":"no-cache"
    }

    params = dict(
        action='get_studies',
        pair_ID=7,
        time_frame=3600
    )

    resp = s.get("https://www.investing.com/common/technical_studies/technical_studies_data.php", 
                        params=params, headers=headers)
    
    print(resp.content)
    print(resp.status_code)
    