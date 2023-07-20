import json
from datetime import datetime
import random
from prettytable import PrettyTable
import os


class Bank:
   path = "atm.json"
   
   def __init__(self, id_no):
      self.id_no = id_no
      
   @staticmethod
   def load_data():
      with open(Bank.path, "r") as f:
         return json.load(f)
        
   @staticmethod
   def save_data(data):
      with open(Bank.path, "w") as f:
         json.dump(data, f, indent=4)
   
   
   
   @staticmethod
   def ispath():
      if not os.path.exists(Bank.path):
         with open("atm.json", "w") as file:
            file.write("{}")
               
               
   def check_account(self):
      data = Bank.load_data()
      if self.id_no not in data:
         print("[+] This account doesn't exist")
         return None
      account = data[self.id_no]
      print("\n")
      print(f"ID: {self.id_no}")
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

   def deposit_account(self,amount):
      data=Bank.load_data()
      if self.id_no not in data:
         print("[+] This account doesn't exist")
         return None
      account = data[self.id_no]
      account["total_money"] += amount
      account["transaction_date"].append(f"D {datetime.now():%Y-%m-%d %I:%M:%S%p} {None} {amount}")

      Bank.save_data(data)
      print(f"[+] {account['username']} deposited {amount} to the account")

   def delete_account(self):
      data=Bank.load_data()
      
      if self.id_no not in data:
         print("[+] This account doesn't exist")
         return None
      
      username=data[self.id_no]["username"]
      del data[self.id_no]
      Bank.save_data(data)
      print(f"[+] {username} has been deleted from the ATM")
      
   def withdraw_account(self,amount):

      data = Bank.load_data()

      if self.id_no not in data:
         print("[+] This account doesn't exist")
         return None


      account = data[self.id_no]

      if amount > account["total_money"]:
         print("[-] Invalid amount. Not enough balance.")
         return

      account["total_money"] -= amount
      account["transaction_date"].append(f"W {datetime.now():%Y-%m-%d %I:%M:%S%p} {None} {amount}")

      Bank.save_data(data)
      print(f"[-] {account['username']} withdrew {amount} from the account")
      
      
   @staticmethod
   def create_account(username,amount):
      data = Bank.load_data()

      id_no = random.randint(100, 999)

      while str(id_no) in data:
         id_no = random.randint(100, 999)

      account = {
         "username": username,
         "account_created": f"{datetime.now():%Y-%m-%d %I:%M:%S%p}",
         "total_money": amount,
         "transaction_date": []
      }

      data[str(id_no)] = account

      Bank.save_data(data)

      print(f"[+] Your username is: {username}")
      print(f"[+] Your Account ID is: {id_no}")


   def transaction_account(self,recv_id,amount):
      data = Bank.load_data()

      if self.id_no  not in data or recv_id not in data:
         print("[+] One or both of the accounts don't exist")
         return


      if amount > data[self.id_no]["total_money"]:
         print("[-] Invalid amount. Not enough balance.")
         return

      tran_account = data[self.id_no]
      recv_account = data[recv_id]

      tran_account["total_money"] -= amount
      tran_account["transaction_date"].append(f"T {datetime.now():%Y-%m-%d %I:%M:%S%p} {recv_id} {amount}")

      recv_account["total_money"] += amount
      recv_account["transaction_date"].append(f"R {datetime.now():%Y-%m-%d %I:%M:%S%p} {self.id_no} {amount}")

      Bank.save_data(data)

      print(f"[-] {tran_account['username']} transacted {amount} to {recv_account['username']} from the ATM")
      
   
      
def main():
   
   Bank.ispath()
   while True:
      print("\n------ Bank Menu ------")
      print("1. Check Account")
      print("2. Deposit Account")
      print("3. Delete Account")
      print("4. Withdraw Account")
      print("5. Create Account")
      print("6. Transaction Account")
      print("7. Quit")

      choice = int(input("Enter your choice: "))

      if choice == 1:
         account_id = input("Enter account ID: ")
         account = Bank(account_id)
         account.check_account()
      elif choice == 2:
         account_id = input("Enter account ID: ")
         amount = int(input("Enter amount to deposit: "))
         account = Bank(account_id)
         account.deposit_account(amount)
      elif choice == 3:
         account_id = input("Enter account ID: ")
         account = Bank(account_id)
         account.delete_account()
      elif choice == 4:
         account_id = input("Enter account ID: ")
         amount = int(input("Enter amount to withdraw: "))
         account = Bank(account_id)
         account.withdraw_account(amount)
      elif choice == 5:
         username = input("Enter username: ")
         amount = int(input("Enter initial deposit amount: "))
         Bank.create_account(username, amount)
      elif choice == 6:
         sender_id = input("Enter sender's account ID: ")
         receiver_id = input("Enter receiver's account ID: ")
         amount = float(input("Enter transaction amount: "))
         account = Bank(sender_id)
         account.transaction_account(receiver_id, amount)
      elif choice == 7:
         print("Exiting...")
         break
      else:
         print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
