'''BANKING LEDGER SYSTEM'''

'''
ACCOUNT(account number, name, pin, balance, history)

MAIN MENU:
1. Login
2. Create Account
0. Exit

USER DASHBOARD:
1. Deposit
2. Withdraw
3. Check Balance
0. Logout
'''
import pickle

filename = "bank_ledger.bin"

def load_data():
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {} 

def save_data(records):
    with open(filename, "wb") as file:
        pickle.dump(records, file)

def create_account(records):
    print("\n--- Open a New Account ---")
    try:
        acc_no = int(input("Enter new Account Number (eg. 1001): "))
        
        if acc_no in records:
            print("Sorry, this account number already exists!")
            return 
        
        name = input("Enter Full Name: ")
        pin = input("Create a 4-digit PIN: ")
        amount = int(input("Initial Deposit Amount: Rs. "))
        
        # saving the user details
        records[acc_no] = {
            "name": name, 
            "pin": pin, 
            "balance": amount, 
            "history": [amount]
        }
        
        save_data(records)
        print(f"Account {acc_no} created successfully!")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def deposit(records, acc_no):
    print("\n--- Deposit Money ---")
    try:
        amount = int(input("Enter amount to deposit: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
            
        records[acc_no]["balance"] += amount
        records[acc_no]["history"].append(amount)
        
        save_data(records)
        print(f"Deposited Rs.{amount}. New Balance: Rs.{records[acc_no]['balance']}")
    except ValueError:
        print("Please enter a valid number.")

def withdraw(records, acc_no):
    print("\n--- Withdraw Money ---")
    try:
        amount = int(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
            
        if amount > records[acc_no]["balance"]:
            print(f"Insufficient funds! Your balance is Rs.{records[acc_no]['balance']}")
            return
            
        records[acc_no]["balance"] -= amount
        records[acc_no]["history"].append(-amount)
        
        save_data(records)
        print(f"Withdrawn Rs.{amount}. New Balance: Rs.{records[acc_no]['balance']}")
    except ValueError:
        print("Please enter a valid number.")

def check_balance(records, acc_no):
    print("\n--- Account Details ---")
    print(f"Name: {records[acc_no]['name']}")
    print(f"Balance: Rs.{records[acc_no]['balance']}")
    
    print("\nRecent Transactions:")
    for trans in records[acc_no]["history"]:
        if trans > 0:
            print(f"  Credit: + Rs.{trans}")
        else:
            print(f"  Debit:  - Rs.{abs(trans)}")

def login(records):
    print("\n--- User Login ---")
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in records:
            print("Account not found.")
            return
            
        pin = input("Enter 4-digit PIN: ")
        if pin != records[acc_no]["pin"]:
            print("Incorrect PIN! Access denied.")
            return
            
        print(f"\nWelcome back, {records[acc_no]['name']}!")
        
        # Inner loop for logged in user
        while True:
            print(f"\n*** {records[acc_no]['name'].upper()}'S DASHBOARD ***")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("0. Logout")
            
            choice = int(input("Enter choice: "))
            
            if choice == 0:
                print("Logging out...")
                break 
            elif choice == 1:
                deposit(records, acc_no)
            elif choice == 2:
                withdraw(records, acc_no)
            elif choice == 3:
                check_balance(records, acc_no)
            else:
                print("Invalid choice, try again.")
                
    except ValueError:
        print("Invalid input! Numbers only.")

def main():
    accounts_data = load_data()
    
    while True:
        print("\n*** MAIN MENU ***")
        print("1. Login")
        print("2. Create Account")
        print("0. Exit")

        try:
            ch = int(input("Enter choice: "))
            if ch == 0:
                print("Exiting program. Bye!")
                break
            elif ch == 1:
                login(accounts_data)
            elif ch == 2:
                create_account(accounts_data)
            else:
                print("Invalid option!")

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
