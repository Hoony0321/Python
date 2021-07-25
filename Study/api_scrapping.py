import requests
import datetime
from bs4 import BeautifulSoup
from pandas import Series

def get_content(code):
    url = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=" + code;
    content = requests.get(url).json();

    return content;

content = get_content("btc_krw");
print("=" * 20 + "BTC_KRW" + "=" * 20);
print(datetime.datetime.fromtimestamp(content['timestamp']/1000));
print("price : " + content['last']);
print("volume : " + content['volume']);
print("changePercent : " + content['changePercent']);


