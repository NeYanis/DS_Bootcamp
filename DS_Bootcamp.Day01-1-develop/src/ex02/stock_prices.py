import sys

def data(key):
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
    key_f=key[:1].upper() + key[1:].lower()
    if key_f in COMPANIES:
        print(STOCKS[COMPANIES[key_f]])
    else:
        print("Unknown company")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        data(sys.argv[1])
