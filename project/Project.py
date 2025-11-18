import os
Data_file="account.txt"
def load_accounts():
    accounts= {}
    if os.path.exists(Data_file):
        with open(Data_file, 'r') as file:
            for line in file: 
                account_id ,name, balance=line.strip().splip(',')
                accounts[account_id] ={"name" : name , "balance": float(balance)}
                return accounts
def save_accounts(accounts):
    with open(Data_file, "w") as file : 
     for account_id, name , balance in accounts.items(): 
         file.write(f"{account_id},{name},{balance}\n")

def create_account(accounts):
    account_id = input("Enter account ID: ")
    if account_id  in accounts: 
        print("Account already exists.")
        return
    name = input("Enter account holder name:")
    balance= float(input("Enter the balance: "))
    
    accounts[account_id] = { "name" : name , "balance" : balance}
    print("Account create successfully.")      
def deposit(accounts):
    account_id= input("Enter account ID:")
    if account_id not in accounts: 
        print("Account is not found.")
        return 
    balance = float(input("Enter deposit amount:"))  
    accounts[account_id]["balance"] += balance
    print("Deposit successfull.")   
def withdraw(accounts):
    account_id= input("Enter account ID:")
    if account_id not in accounts: 
        print("Account is not found.")
        return 
    balance = float(intput("Enter withdraw amount:"))
    if balance > accounts[account_id]["balance"]:
        print("Insufficient balance.")
        return
    else: 
        accounts[account_id]["balance"] -= balance
        print("Withdraw successful.")
        
def check_balance(accounts):
    account_id= input("Enter account ID:")
    if account_id not in accounts: 
        print("Account is not found.")
        return 
    print(f"Account holder :{accounts[account_id]['name']}")
    print(f"Balance: ${accounts[account_id]['balance']:.2f}")
    
def main():
    accounts = load_accounts()
    while True: 
        print("Weocome to Bank System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            save_accounts(accounts)
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")