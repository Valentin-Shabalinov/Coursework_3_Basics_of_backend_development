import json

from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_value(data):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:5]
    return data

def get_final_list(data):
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if description == "Открытие вклада":
            from_ = 'Открытие счета'

        elif description == "Перевод со счета на счет":
            last_nums = row["from"].split(' ')[-1][-4:]
            from_ = ''.join([row["from"][:4], " **", last_nums])

        else:
            name_card = row["from"][0:-16]
            nums_1 = row["from"][-16:-12]
            nums_2 = row["from"][-12:-10]
            nums_3 = row["from"][-4:]
            from_ = ''.join([name_card, 
                             ' ', 
                             nums_1, 
                             ' ', 
                             nums_2, 
                             '**', 
                             ' ', 
                             '****', 
                             ' ', 
                             nums_3])

        to = row["to"]
        amount = row["operationAmount"]["amount"]
        name = row["operationAmount"]["currency"]["name"]

        print(date, description)
        print(f'{from_} -> {to[:4]} **{to[-4:]}')
        print(amount, name)
        print()

