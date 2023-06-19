import json
from datetime import datetime
import random
from prettytable import PrettyTable
import os

PATH = "atm.json"

def load_data():
   with open(PATH, "r") as f:
      return json.load(f)

def save_data(data):
   with open(PATH, "w") as f:
      json.dump(data, f, indent=4)



def check_account():
   id_no = input("Enter your ID: ")
   data = load_data()

   if id_no not in data:
      print("[+] This account doesn't exist")
      return

   account = data[id_no]
   print("\n")
   print(f"ID: {id_no}")
   print(f"NAME: {account['username']}")
   print(f"DATE AND TIME OF CREATION: {account['account_created']}")
   print(f"AMOUNT: {account['total_money']}")

   table = PrettyTable()
   table.field_names = ["Type", "Date", "Time", "ID", "Amount"]
   table.align = "r"
   table.align["Type"] = "l"
   table.align["ID"] = "l"
   
   transaction_dates = account["transaction_date"]
   
   print("\n")
   if len(transaction_dates) != 0:
      for dtime in transaction_dates:
         data = dtime.split()
         if "W" in dtime:
            data[0] = "Withdraw"
         elif "T" in dtime:
            data[0] = "Transaction"
         elif "R" in dtime:
            data[0] = "Received"
         elif "D" in dtime:
            data[0] = "Deposit"
         table.add_row(data)
      print(table)
   else:
      print("[+] No withdrawals, transactions, or deposits have been made for this account.")
        
        
        
def deposit_account():
   id_no = input("Enter your ID: ")
   data = load_data()

   if id_no not in data:
      print("[+] This account doesn't exist")
      return

   amount = int(input("[=] Enter the amount: "))
   
   account = data[id_no]
   account["total_money"] += amount
   account["transaction_date"].append(f"D {datetime.now():%Y-%m-%d %I:%M:%S%p} {None} {amount}")

   save_data(data)
   print(f"[+] {account['username']} deposited {amount} to the account")


def delete_account():
   id_no = input("Enter your ID: ")
   data = load_data()

   if id_no not in data:
      print("[+] This account doesn't exist")
      return

   username = data[id_no]["username"]
   del data[id_no]

   save_data(data)
   print(f"[+] {username} has been deleted from the ATM")

def withdraw_account():
   id_no = input("Enter your ID: ")
   data = load_data()

   if id_no not in data:
      print("[+] This account doesn't exist")
      return

   amount = int(input("[=] Enter the amount: "))
   account = data[id_no]

   if amount > account["total_money"]:
      print("[-] Invalid amount. Not enough balance.")
      return

   account["total_money"] -= amount
   account["transaction_date"].append(f"W {datetime.now():%Y-%m-%d %I:%M:%S%p} {None} {amount}")

   save_data(data)
   print(f"[-] {account['username']} withdrew {amount} from the account")
def create_account():
   data = load_data()

   id_no = random.randint(100, 999)
   name = input("Enter your name: ")
   amount = int(input("[=] Enter initial amount: "))

   while str(id_no) in data:
      id_no = random.randint(100, 999)

   account = {
      "username": name,
      "account_created": f"{datetime.now():%Y-%m-%d %I:%M:%S%p}",
      "total_money": amount,
      "transaction_date": []
    }

   data[str(id_no)] = account

   save_data(data)

   print(f"[+] Your username is: {name}")
   print(f"[+] Your Account ID is: {id_no}")


def transaction_account():
   data = load_data()

   tran_id = input("Enter your ID: ")
   recv_id = input("Enter receiver ID: ")

   if tran_id not in data or recv_id not in data:
      print("[+] One or both of the accounts don't exist")
      return

   amount = int(input("Enter the amount of transaction: "))

   if amount > data[tran_id]["total_money"]:
      print("[-] Invalid amount. Not enough balance.")
      return

   tran_account = data[tran_id]
   recv_account = data[recv_id]

   tran_account["total_money"] -= amount
   tran_account["transaction_date"].append(f"T {datetime.now():%Y-%m-%d %I:%M:%S%p} {recv_id} {amount}")

   recv_account["total_money"] += amount
   recv_account["transaction_date"].append(f"R {datetime.now():%Y-%m-%d %I:%M:%S%p} {tran_id} {amount}")

   save_data(data)

   print(f"[-] {tran_account['username']} transacted {amount} to {recv_account['username']} from the ATM")


def main():
   if not os.path.exists("atm.json"):
      with open("atm.json", "w") as file:
            file.write("{}")
            
   print('''
   [1.] Check account: check the balance of an account
   [2.] Deposit account: deposit money into an account
   [3.] Delete account: delete an account
   [4.] Withdraw account: withdraw money from an account
   [5.] Create account: create a new account
   [6.] Transaction account: transfer money from one account to another
    ''')

   user = int(input('[*] Enter your option: '))

   if user == 1:
      check_account()
   elif user == 2:
      deposit_account()
   elif user == 3:
      delete_account()
   elif user == 4:
      withdraw_account()
   elif user == 5:
      create_account()
   elif user == 6:
      transaction_account()
   else:
      print("[-] Invalid option.")


if __name__ == "__main__":
   main()


'''
Overall, 
putting the code inside a main() function promotes good programming practices, 
such as 
modularity, 
readability, 
reusability, 
and easier testing/debugging. 
It enhances code organization and provides a clear entry point for the program's execution.
'''
