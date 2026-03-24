import json
import os
from datetime import datetime

def load_file(filename):
    if os.path.exists(filename) :
        with open(filename , "r") as f :
            data = json.load(f)
            return data
    else:
        return []

def save_file(filename, data):
    with open (filename , "w") as f:
        json.dump(data, f)

def add_record(filename):

    amount = input("how much did you pay?")
    group = input("what for ?")
    description = input("what did you bought?")
    date = input("when was it (DD/MM/YYYY) , (HH:MM) : ?")


    tracker = {
        "amount" : amount ,
        "group" : group ,
        "description" : description ,
        "date" : date
    }


    expenses = load_file(filename) 
    expenses.append(tracker)
    save_file(filename , expenses)

def show(filename):
    expenses = load_file(filename) 
    for record in expenses :
        print(record)

def total_sum(filename):
    expenses = load_file(filename) 
    total = 0
    for record in expenses :
        total += record["amount"]
    print(total)


def main_menu(filename):
    while True :
        option = input("what do you want me to do ?  add , show , total , quit ?")
        if option == "add":
            add_record(filename)
        elif option == "show" :
            show(filename)
        elif option == "total" :
            total_sum(filename)
        elif option == "quit":
            print("bye")
            break
        else :
            print("wrong command")

filename = "expenses.json"
main_menu(filename)

