Name = input("Please enter your user name : ")
print("Hello ", Name)

Message = """
        1. >>> Chech Balance
        2. >>> Deposite
        3. >>> Withdraw
"""
print(Message)

Task = int(input("PLEASE SELECT AN OPTION : "))       
print(Task)

#FiXEd Amount
Total_amount = 5000

#Check user only select the given options 
if Task >= 1 and Task <=3:
    print("Welcome to vist the NA_LENA_NA_DENA bank ")
    if Task == 1:
       #Check_balance
       print("THANKS for visting us ! Your avaliable balance is :" , Total_amount)

    elif Task == 2:
       #Deposite_amount
       Deposite_amount = int(input("PLZ enter the Deposite_amount :  "))
       if Deposite_amount >= 500 :
        Total_amount =Deposite_amount + Total_amount
        print("You have successfully deposit your amount : ", Deposite_amount)
        print("Thanks for visting us , your cuttent balance is : ", Total_amount)

       else:
           print("You have to deposit atleast 500 Rupees !, ")

    else:
       #withdraw_amount
       withdraw_amount = int(input("Enter Amount:"))
       if withdraw_amount<=Total_amount :
        Total_amount=Total_amount - withdraw_amount
        print("You have successfully withdraw your amount : ", withdraw_amount)
        print("Thanks for visting us , your cuttent balance is : ", Total_amount)

       else:
          print("YOU don't have a sufficient amount ,PlS check your balance: ERROR!!! ")

else:
    print("Please enter Vaild option ")
    #THANK YOU