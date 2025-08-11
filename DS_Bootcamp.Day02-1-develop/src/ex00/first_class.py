class Must_read():
    file = 'data.csv'
    try:
        with open(file, 'r') as input:
            print(input.read())
    except FileNotFoundError:
        raise FileNotFoundError(f'File {file} not found')





if __name__ == '__main__':
    Must_read()
