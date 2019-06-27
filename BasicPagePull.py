from bs4 import BeautifulSoup
import requests
import re
import json
import time
import sys
import os



BASE_SITE = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=AAPL&owner=exclude&action=getcompany"

REQ_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.10.382.104 Safari/537.36'
}


def GetPageSoup(requestedUrl):
    with requests.Session() as s:
        try:
            r = s.get(requestedUrl, headers=REQ_HEADERS)
            soup = BeautifulSoup(r.content, 'html.parser')
            time.sleep(10)
            return soup
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            time.sleep(10)


def main():
    htmlPageSoup = GetPageSoup("https://www.sec.gov/Archives/edgar/data/320193/000032019319000066/a10-qq220193302019.htm")
    #print(htmlPageSoup)
    with open("page.html", "w") as file:
        file.write(str(htmlPageSoup.encode("utf-8")))


if __name__ == "__main__":
    main()