import sys
import re
import requests
import json
from urllib.request import urlopen
import time
import os
import random

def main():
    time.sleep(random.randint(5, 20))
    response = requests.get('https://pedidodevistos.mne.gov.pt/VistosOnline/gettime?id_posto=2067')
    separated_strings = response.text.split(";", -1)

    list_month = []
    list_day = []
    list_dates = []

    for string in separated_strings:
        match = re.match(r'\w*\[2023\]\[[2-4]\]', string)
        if match:
            string_month = re.sub(r'\w*\[2023\]\[', '', string).split("]", 1)[0]
            string_date = re.sub(r'\w*\[2023\]\[[2-4]\]\s\=\s\w*\s\w*\(', '', string).replace(")", "")
            list_dates = string_date.split(",", -1)
            list_month.append(string_month)
            list_day.append(list_dates)

    if bool(list_dates):
        my_dict = dict.fromkeys(list_month, list_dates)
        firstin_month = min(my_dict.keys())
        firtsin_day_by_month = min(my_dict.get(firstin_month))
        TOKEN = ""
        chat_id = ""
        message = "Свободные слоты!\nБлижайщая дата:\n\nМесяц\n" + firstin_month + "\nДень \n" + firtsin_day_by_month + "\n\nСкорее переходи по ссылке!\nhttps://pedidodevistos.mne.gov.pt/VistosOnline/Pedidos\n\n\n" + "Остальные даты кучкой:\n" + str(my_dict)
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())
    print("---")

if __name__ == "__main__":
    while True:
        main()
    
