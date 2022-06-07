import time
from random import randint

def create_account():
      print("Welcome to Promech trust bank")
      time.sleep(3)
      print("""
""")
      while True:
            open_account = input("Do you want to create an account? [YES OR NO]: ").lower()
            if  open_account == "yes" :
                  Surname = input("Please enter your surname: ")
                  Middle_Name =input("Please enter your middle name: ")
                  Last_Name = input("Please enter your last name: ")
                  break
            elif open_account == "no":
                  print("Okay Bye")
                  continue
            else:
                  continue
      global account_number
      account_number = randint(10000000000, 99999999999)
      print("Please wait while we provide your details...")
      time.sleep(3)
      print(f"your details include; \n-----------------------------------------------------------\n Surname: {Surname} \n Middle_Name: {Middle_Name} \n Last_Name: {Last_Name} \n Account_number: {account_number}")
      print("------------------------------------------------------------")
      
create_account()

def atm():
      while True:
            atm_card = input("Do you want an atm card now?[YES OR NO]: ").lower()
            if atm_card == "yes":
                  print("wait while your card is being produced...")
                  time.sleep(3)
                  print("Your card is now ready")
                  break
            elif atm_card == "no":
                  print("Okay Bye")
                  continue
            else:
                  print("please input yes or no")
      global atm_pin
      print("please wait...")
      time.sleep(3)
      while True:
            atm_pin =int( input("Please choose a 4 digit pin for your atm card: "))
            if atm_pin < 1000 or atm_pin > 9999:
                  print("Please it must be 4 digits in number")
                  print("Try again")
                  continue
            elif atm_pin <=  9999:
                  print("Your atm_pin is", atm_pin)
                  print("please wait...")
                  break
            else:
                  print("Please input only numbers")
                  continue
      time.sleep(3)
atm()

def deposit():
      global account_balance
      account_balance = int(input("Please how much are you depositing?: "))
      print("please wait...")
      time.sleep(3)
      print("Your account_balance is", account_balance )
      
deposit()

def deposit2():
      deposit2 = int(input("Please how much are you depositing:"))
      print("please wait...")
      time.sleep(2)
      global account_balance
      account_balance += deposit2
      print("Your current account balance is", account_balance)

def menu():
      print("These are the transactions you can perform next;")
      print("--------------------------------------------------------------")
      print("""For Deposit press 1
For withdrawal, press 2
For Check balance press 3
For Transfer press 4
To change ATM pin press 5
To Exit press 6""")

      
def withdrawal():
      print("Please wait...")
      time.sleep(2)
      while True:
            withdraw_input = int(input("Please how much do you want to withdraw?: "))
            global account_balance
            if withdraw_input >= account_balance or account_balance - withdraw_input <= 100:
                  print("Insufficient funds. Please try again.")
                  continue
            elif withdraw_input > 100  and withdraw_input < account_balance:
                   print("Please wait...")
                   time.sleep(3)
                   break
      while True:
            check_pin = int(input("Please insert your atm pin: "))
            if check_pin == atm_pin:
                  print("You're in")
                  time.sleep(2)
                  break
            elif check_pin != atm_pin:
                  print("Wrong pin. Please try again")
                  continue
      print("Transaction successful")
      print("Please wait...")
      time.sleep(3)
      print("Your account has been debited with", withdraw_input)
      print("Please wait...")
      time.sleep(3)
      account_balance -=  withdraw_input
      print("Your current account balance is", account_balance)
            
            
            

            
def check_balance():
      time.sleep(3)
      print("Please wait while we fetch your account balance...")
      time.sleep(3)
      print("Your account balance is", account_balance)
            


def transfer():
      global account_balance
      print("Please wait...")
      time.sleep(2)
      while True:
            transfer = int(input("Please how much do you want to transfer?: " ))
            if transfer >= account_balance or account_balance - transfer <= 100:
                  print("Insufficient funds. Please try again.")
                  continue
            elif transfer > 100  and transfer < account_balance:
                   print("Please wait...")
                   time.sleep(3)
                   break
      while True:
            recipient_acc_num = int(input("please input recipient account number: "))
            if recipient_acc_num > 9999999999 and recipient_acc_num <= 99999999999:
                  print("Please wait...")
                  time.sleep(3)
                  break
            else:
                  print("Invalid account number")
                  continue
      while True:
            atm_check = int(input("Please input your atm pin: "))
            if atm_check == atm_pin:
                  print("You're in")
                  print("Please wait...")
                  time.sleep(3)
                  print("Your request to transfer", transfer, "to",recipient_acc_num, "is in process, please wait...")
                  time.sleep(3)
                  print("Transaction successful")
                  time.sleep(2)
                  print("Your account has been debited with", transfer)
                  print("-----------------------------------------------------------")
                  time.sleep(3)
                  account_balance -= transfer
                  print("Your current account balance is", account_balance)
                  break
            else:
                  print("Wrong atm pin" "\n" "please try again")
                  continue



def change_atm_pin():
      print("Please wait...")
      time.sleep(2)
      global atm_pin
      while True:
            previous_pin = int(input("Please input your previous atm pin: "))
            if previous_pin == atm_pin:
                  print("You're in")
                  break
            else:
                  print("Wrong pin, please try again")
                  continue
      while True:
            atm_pin =int( input("Please choose a new 4 digit pin for your atm card: "))
            if atm_pin < 1000 or atm_pin > 9999:
                  print("Please it must be 4 digits in number")
                  print("Try again")
                  continue
            elif atm_pin <=  9999:
                  print("Your new atm_pin is", atm_pin)
                  break
            else:
                  print("Please input only integers abeg")
                  continue


def stop():
      print("Dear customer, thank you for choosing Promtech trust bank","\n""We hope to see you another time, God bless you.")
      print("Please wait...")
      time.sleep(2)
      exit()

def runner():
      while True:
            print("Please wait...")
            time.sleep(3)
            menu()
            you = int(input("What transaction will you like to perform?: "))
            if you == 1:
                  deposit2()
            elif you == 2:
                  withdrawal()
            elif you == 3:
                  check_balance()
            elif you == 4:
                  transfer()
            elif you == 5:
                  change_atm_pin()
            elif you == 6:
                  stop()
            else:
                  print("Please input the correct thing")

runner()


             
             





      

                        
                         
                   
       






            


                
