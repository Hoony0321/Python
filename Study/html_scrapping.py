import requests

from bs4 import BeautifulSoup

def get_items(code, selector):
    url = "https://finance.naver.com/item/main.nhn?code=" + code;
    html = requests.get(url).text;

    soup = BeautifulSoup(html,"html5lib");
    items = soup.select(selector);
    return items;

def get_name(code):
    items = get_items(code, "#middle > div.h_company > div.wrap_company > h2 > a");
    return items[0].text;

def get_per(code):
    items = get_items(code,"#_per");
    return float(items[0].text);

def get_dividend(code):
    items = get_items(code, "#_dvr");
    return float(items[0].text);

def get_foreign(code):
    items = get_items(code,"#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em" );
    
    return items[0].text;

def print_code(code):
    name = get_name(code);
    per = get_per(code);
    dvr = get_dividend(code);
    foreign = get_foreign(code);

    print("NAME : " + name);
    print("per : " , per);
    print("dvr : " , dvr);
    print("foreign : " + foreign);
    

print_code("000660");