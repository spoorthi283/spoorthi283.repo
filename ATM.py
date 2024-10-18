#balance, deposit,withdraw,exit

balance = 1000 
while True:
    print("\n ATM menu:")
    print("1.Checkbalance")
    print("2. deposit")
    print("3. withdraw")
    print("4.Exit")
    choice= input("enter your choice")
    if choice== '1':
        print(f"your current balance is:{ balance}")
    elif choice == '2':
        deposit_amount = float(input("enter the deposit amount:"))
        balance += deposit_amount
        print(f"your total amount is {deposit_amount}.your total balance is {balance}")
    elif choice == '3':
        withdrawl_amount = float(input("enter the amount you want to withdraw: "))
        if withdrawl_amount > balance:
            print("insufficient balance!")
        else:
            balance -= withdrawl_amount
            print(f"withdrawl of {withdrawl_amount} has been done! your total balance is {balance}")
    elif choice == '4':
        print("thankyou")
        break
