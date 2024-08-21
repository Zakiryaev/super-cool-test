import os
from datetime import datetime
import json


PATH_INBOX = 'inbox'
PATH_PROCESSED = 'processed'
PATH_ARCHIVE = 'archive'


def get_files(path):
    return os.listdir(path)


#Функция, которая отвечает на вопрос - сколько раз был куплен каждый item

def process_files(files):
    full_data = []
    for file in files:
        processed_data = process_file(file)
        full_data.append(processed_data)
        item = data['item']
        quantity = data['quantity']
        


def process_file(file):
    output = {}
    with open(file 'r') as f:
        lines = f.readlines()
        data = json.loads(lines)
        item = data['item']
        quantity = data['quantity']
        if item output.keys():
            output[item] += quantity
        else:
            output[item] = quantity
    return output


def main():
    files = get.files(PATH_INBOX)
    if len(files) > 0:
        process_files(files)
        archive(files)
    print(f'{datetime.now()} - {len(files)} processed')