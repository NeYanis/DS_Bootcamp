import sys

def data(ticker):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }
    flag = True
    key_u = ticker.upper()
    if key_u in STOCKS:
        flag = False
        name = next(key for key, value in COMPANIES.items() if value == key_u)
        print(f'{key_u} is a ticker symbol for {name}')
    
    key_c =ticker.capitalize()
    if key_c in COMPANIES and flag:
        flag = False
        tic = COMPANIES[key_c]
        price = STOCKS[tic]
        print(f'{key_c} stock price is {price}')
    if flag:
        print(f'{ticker} is an unknown company or an unknown ticker symbol')
def input(line):
    strip_line = [name.strip() for name in line.split(',')]
    return strip_line

def cooking(strips):
    for strip in strips:
        if strip == '':
            return
    for strip in strips:
        data(strip)
def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        line = input(sys.argv[1])
        cooking(line)

if __name__ == '__main__':
    main()