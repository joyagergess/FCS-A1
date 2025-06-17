balance = 2000 
count_transaction =0 
Password = "88"


while True:
    entered_password = input("Enter your password to access the ATM: ")
    if entered_password == Password:
        print(" Welcome to the ATM!")
        break
    else:
        print("Incorrect password. Try again.")


while True:
    print("""
         What can we help you with ?
          1. Check Balance
          2. Deposit Money
          3. Withdraw Money
          4. Exit
          """)
    choice = input ("Enter your choice (1 for checking balance , 2 for adding deposit etc..) :")

    if choice =='1' :
        print("Your current balance is :"+ str(balance))
     
    elif choice == '2':
        while True:
            deposit = input("Enter how much to deposit: ")
            if not deposit.isdigit() :
                print("Please enter a valid positive number")
            else:
                deposit = int(deposit)
                balance += deposit
                count_transaction += 1
                print("Your current balance now is: " + str(balance))
                break
                   
    elif choice == '3':
        count_failed_withdraw = 0  
        while True:
            withdraw = input("Enter how much to withdraw: ")
            if not withdraw.isdigit():
                print("Please enter a valid positive number")
                continue
            withdraw = int(withdraw)

            if withdraw > balance:
                print("You don't have enough money. Try again.")
                count_failed_withdraw += 1
                if count_failed_withdraw > 3:
                    print("Warning: more than 3 failed withdrawals were attempted.")
            else:
                balance = balance - withdraw
                count_transaction += 1
                print("Withdrawal successful. New balance:", balance)
                break

    elif choice == '4' :
        print ("You made " +  str(count_transaction) + " transactions. Exit ATM" )
        break

    else :
        print("Please enter a number between 1 and 4 ")