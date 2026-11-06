#mini atm
print("----MINI ATM----")
correct_pin = 2008
balance = 10000
pin=int(input("Enter pin "))
if pin==correct_pin:
    print("login Succesful")
    print("1.Check Balance")
    print("2.Withdraw money")
    print("3.Deposit money")
    choice = int(input("Please select one: "))
    if choice==1:
        print(f"The balance is {balance}")
    elif choice==2:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount>0 and amount<=balance:
            balance=balance-amount
            print(f"The available balance is {balance}")
    elif choice==3:
        amount = int(input("Enter the amount you want to deposit: "))
        if amount>0:
            balance=balance+amount
            print(f"The final balance is {balance}")          
    else:
        print("invalid service")
else:
    print("Wrong pin")        
