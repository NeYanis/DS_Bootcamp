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
    key_f = ticker.upper()
    if key_f in STOCKS:
        name = next(key for key, value in COMPANIES.items() if value == key_f)
        print(name, STOCKS[key_f])
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        data(sys.argv[1])