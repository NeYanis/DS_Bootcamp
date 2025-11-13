#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys
import time
from fake_useragent import UserAgent

    
def get_html(ticker):
    ticker = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/"
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers= headers)
        response.raise_for_status()
    except Exception as e:
        raise ValueError(f"Error to access the url: {e}")
    time.sleep(5)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
    except Exception:
        raise ValueError('Error parcing HTML')
    return soup

def finder(field, soup):
    table = soup.find('div', class_="table yf-9ft13")
    if table == None:
        raise Exception("Table not exist")
    rows = table.find_all('div', class_="row lv-0 yf-t22klz")
    if not rows:
        raise Exception("No rows found in the table")
    for row in rows:
        
        item = row.find('div', class_="column sticky yf-t22klz").text.strip()

        if item == field:
            elements = row.find_all('div', class_=["column yf-t22klz" , "column yf-t22klz alt"])
            values = tuple(el.text.strip() for el in elements)
            result = (item, *values)
            
            return result
        
    raise Exception(f"Field '{field}' not found in the table")

def main():
    if len(sys.argv) != 3:
        raise Exception("Incorrect number of arguments Usage: ./financial.py ticker field")
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    try:
        soup = get_html(arg1)
        result = finder(arg2, soup)
        print(result)
    except Exception as e:
        print(f'Error:{e}')


if __name__ == '__main__':
    main()

