import os
from random import randint
import logging
import requests
from config import LOG_FILE, LOG_FORMAT,TG_API, CHAT_ID
logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILE,
    format = LOG_FORMAT
)
class Research():
    def __init__(self, file):
        self.file = file
    def file_reader(self):
        has_header = True
        if not os.path.exists(self.file):
            logging.error(f'File {self.file} not found')
            raise FileNotFoundError(f'File {self.file} not found')

        with open(self.file, 'r') as input:
            logging.info("Read file")
            lines = input.readlines()

        if len(lines) < 2:
            logging.error("Null data")
            raise ValueError("Script not support null data")
        header = lines[0].strip().split(',')
        if len(header) != 2:
            logging.error("Unsupport header")
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
                logging.error("Unsupport value")
                raise ValueError('Values not support')
            if value[0] == value[1]:
                logging.error("Not different value")
                raise ValueError('Values must be different')
            result.append([int(value[0]),int(value[1])])
        logging.info(f"Succesfully read {self.file}")
        return result
    def send_log_message(self, message):
        data = {
            "chat_id": CHAT_ID,
            "text": message
        }
        try:
            response = requests.post(TG_API, data = data)
            response.raise_for_status()
            logging.info("Telegram message succesfully sent")
        except Exception:
            logging.error("Failed to sent telegram message")
    class Calculations():
        def __init__(self, list):
            self.list = list
        def counts(self):
            heads = sum(row[0] for row in self.list)
            tails = sum(row[1] for row in self.list)
            logging.info("Count head and tails")
            return heads, tails

        def fractions(self, heads, tails):
            count = heads + tails
            head_procent = heads / (count / 100)
            tail_procent = tails / (count / 100)
            logging.info("Calculating fractions")
            return head_procent, tail_procent
class Analytics(Research.Calculations):
    def predict_random(num):
        predicts = []
        for i in range(num):
            predict = randint(0,1)
            predicts.append([predict, 1 - predict])
        logging.info("Predict random")
        return predicts

    def predict_last(data):
        logging.info("Predict element")
        return data[-1]

    def save_file(data, filename, extension):
        with open(f"{filename}.{extension}", 'w') as file:
            file.write(data)
            logging.info(f"Saving {filename}.{extension}")



