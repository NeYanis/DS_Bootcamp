class Research():
    def file_reader(self):
        file = '../ex00/data.csv'
        try:
            with open(file, 'r') as input:
                return input.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'File {file} not found')





if __name__ == '__main__':
    res = Research()
    print(res.file_reader())
