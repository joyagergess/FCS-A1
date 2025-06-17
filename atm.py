balance = 2000 
deposit = 0
withdraw = 0
print ("welcome to ATM ")
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
    elif choice== '2' :
        while True:
            deposit = input("Enter how much to deposit: ")
            if not deposit.isdigit() :
                 print("Please enter a valid positive number")
            else :
                deposit = int(deposit)
                if deposit < 0:
                   print("Enter a positive number")
                else:
                   balance += deposit
                   print("Your current balance now is: " + str(balance))
                   break
                
    elif choice =='3' :
        while True:
            withdraw = int(input("Enter how much to withdraw: "))
            if withdraw > balance:
                print("You don't have enough money. Try again.")
            else:
                balance = balance - withdraw
                print("Withdrawal successful. New balance:", balance)
                break   
    elif choice == '4' :
        print ("Exit ATM")
        break

    else :
        print("Please enter a number between 1 and 4 ")