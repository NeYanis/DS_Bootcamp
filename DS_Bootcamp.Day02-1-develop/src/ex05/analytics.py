import os
from random import randint
class Research():
    def __init__(self, file):
        self.file = file
    def file_reader(self):
        has_header = True
        if not os.path.exists(self.file):
            raise FileNotFoundError(f'File {self.file} not found')

        with open(self.file, 'r') as input:
                lines = input.readlines()

        if len(lines) < 2:
            raise ValueError("Script not support null data")
        header = lines[0].strip().split(',')
        if len(header) != 2:
            raise ValueError("Script not support this header")
        if header != ['head', 'tail']:
            has_header = False
        if has_header:
            i=1
        else:
            i=0
        result=[]
        for line in lines[i:]:
            value = line.strip().split(',')
            if len(value) != 2 or (value[0] != '0' and value[0] != '1') or (value[1] != '0' and value[1] != '1'):
                raise ValueError('Values not support')
            if value[0] == value[1]:
                raise ValueError('Values must be different')
            result.append([int(value[0]),int(value[1])])

        return result
    class Calculations():
        def __init__(self, list):
            self.list = list
        def counts(self):
            heads = sum(row[0] for row in self.list)
            tails = sum(row[1] for row in self.list)
            return heads, tails

        def fractions(self, heads, tails):
            count = heads + tails
            head_procent = heads / (count / 100)
            tail_procent = tails / (count / 100)
            return head_procent, tail_procent
class Analytics(Research.Calculations):
    def predict_random(num):
        predicts = []
        for i in range(num):
            predict = randint(0,1)
            predicts.append([predict, 1 - predict])
        return predicts

    def predict_last(data):
        return data[-1]

    def save_file(data, filename, extension):
        with open(f"{filename}.{extension}", 'w') as file:
            file.write(data)



