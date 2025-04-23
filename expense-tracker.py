import argparse
import json
import datetime

class Expense:
    def __init__(self,id,description,amount):
        self.id = id
        self.date = datetime.date.today()
        self.description = description
        self.amount = amount

def write_data(expense_data):
    with open("expense_tracker.json","w") as json_file:
        json.dump(expense_data,json_file)

def read_data():
    with open("expense_tracker.json","r") as json_file:
        json_object = json.load(json_file)

        id = json_object[-1]["id"]
        data = json_object[-1]["data"]
        description = json_object[-1]["description"]
        amount = json_object[-1]["amount"]

        return id,data,description,amount

def main():
    arguments_handler()

def arguments_handler():
    try:
        # Initialize parser
        parser = argparse.ArgumentParser()
        subprasers = parser.add_subparsers(required=True)

        # Add command
        add_parser = subprasers.add_subparsers("add",help="add new expense")
        add_parser.add_argument("--description",required=True,help="description to the expense")
        add_parser.add_argument("--amount",required=True,help="amount of the expense")

        # list command
        list_parser = subprasers.add_subparsers("list",help="list of the expenses")

        # summary command
        summary_parser = subprasers.add_subparsers("list",help="summary of all expenses")
        summary_parser.add_argument("--month",help="summary of specific month")

        # delete command
        delete_parser = subprasers.add_subparsers("delete",help="summary of all expenses")
        delete_parser.add_argument("--id",required=True,help="id of a expense")

        # update command 
        update_parser = subprasers.add_subparsers("update",help="update the specific expense")
        update_parser.add_argument("--id",required=True,help="id of a expense")
        update_parser.add_argument("--description",help="description to the expense")
        update_parser.add_argument("--amount",help="amount of the expense")

        # Read arguments from command line
        args = parser.parse_args()

        # check what arguments called
        if args.command == "add":
            add_command(args.description,args.amount)
        elif args.command == "list":
            list_command()
        elif args.command == "summary":
            summary_command(args.month)
        elif args.command == "delete":
            delete_command(args.id)
        # elif args.command == "update":
        #     update_command(args.id,args.description,args.amount)

    except Exception as e:
        print(e)

    def add_command(description,amount):
        print(f"Expense added successfully (ID: {Expense.id})")
    def list_command():
        pass
    def summary_command(month=None):
        pass
    def delete_command():
        pass
    # def update_command(id):
    #     pass

if __name__ == "__main__":
    main()