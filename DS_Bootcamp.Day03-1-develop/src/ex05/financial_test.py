#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys
import time
from fake_useragent import UserAgent
import pytest

    
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
    else:
        pytest.main([__file__])

def test_get_html_valid_ticker():
    soup = get_html("MSFT")
    assert isinstance(soup, BeautifulSoup), "Функция get_html должна возвращать объект BeautifulSoup"

def test_get_html_invalid_ticker():
    soup = get_html("invalid")
    assert isinstance(soup, BeautifulSoup), "Функция get_html должна возвращать объект BeautifulSoup"

def test_get_html_null_ticker():
    soup = get_html("")
    assert isinstance(soup, BeautifulSoup), "Функция get_html должна возвращать объект BeautifulSoup"

def test_finder_valid_field():
    soup = get_html("MSFT")
    result = finder("Total Revenue", soup)
    assert isinstance(result, tuple), "Функция finder должна возвращать кортеж"
    assert len(result) > 1, "Кортеж должен содержать хотя бы одно значение"
    assert result[0] == "Total Revenue", "Первый элемент кортежа должен быть названием поля"

def test_finder_invalid_field():
    soup = get_html("MSFT")
    with pytest.raises(Exception):
        finder("Invalid Field", soup)

def test_finder_empty_soup():
    soup = BeautifulSoup("", "lxml")
    with pytest.raises(Exception):
        finder("Total Revenue", soup)

if __name__ == '__main__':
    main()

