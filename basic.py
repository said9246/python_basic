class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:  # loop taake menu bar bar aaye
            user_input = input(""" 
-------------------------------
Hello, how would you like to proceed?
1. Create PIN
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
-------------------------------
Enter your choice: """)

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = input("Enter a new PIN: ")
        print("✅ PIN created successfully!")

    def deposit(self):
        if self.pin == "":
            print("⚠️ Please create a PIN first.")
            return
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print(f"✅ Deposit successful! New balance: {self.balance}")
        else:
            print("❌ Incorrect PIN!")

    def withdraw(self):
        if self.pin == "":
            print("⚠️ Please create a PIN first.")
            return
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ You withdrew {amount}. Remaining balance: {self.balance}")
            else:
                print("❌ Insufficient balance!")
        else:
            print("❌ Incorrect PIN!")

    def check_balance(self):
        if self.pin == "":
            print("⚠️ Please create a PIN first.")
            return
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print(f"💰 Your current balance is: {self.balance}")
        else:
            print("❌ Incorrect PIN!")


# Run program
obj = ATM()


obj.balance=1000
obj.check_balance()

