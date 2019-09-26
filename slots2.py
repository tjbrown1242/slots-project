wallet = 0
import random


def add_funds(): 
    global wallet
    amount = float(input("Enter amount to be added to your wallet: \n")) 
    wallet += amount 
    print(f"Amount added: ${amount:.2f}\n")
    balance_checker()

def balance_checker():
    global wallet
    print(f'Your wallet balance is: ${wallet:.2f}\n')
    make_choice()


def spin_reels():
    global wallet
    a,b,c = [random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    print("Your numbers are:\n ")
    print(a, b, c)
    if a == b:
      print ("You win 1000!\n")
      wallet += 1000
      balance_checker()
      print('Play again???')
    elif a == b and a == c: 
      print ("You win 10,000!\n")
      wallet += 10000
      balance_checker()
      print('Play again???\n')
    else:
      print("You did not win this time.  Try again?\n")
      make_choice()
    
       

def bet():
  global wallet
  bet_amount = float(input("Enter the amount of your bet:\n "))
  if wallet >= bet_amount:
    wallet -= bet_amount
    spin_reels()
  else:
    print ("You do not have enough money for that bet...Please add funds to your wallet\n")
    make_choice()

def make_choice():
  global wallet
  print('Please Press 1 For Your wallet balance \n\n')
  print('Please Press 2 To Add funds to your wallet \n\n')
  print('Please Press 3 To SPIN the wheels! \n\n')
  print('Please Press 4 To Cash out \n\n')  
  option = int(input('Please make a selection.... \n\n'))
  if option == 1:
    balance_checker()
    print ('Ready to spin??\n\n')
  elif option == 2:
    add_funds()
    balance_checker()
    print('Ready to spin??\n\n')
  elif option == 3:
    bet()
    spin_reels()
  elif option == 4:
    print ('Thank you for playing!!\n\n')
    print(f'Cashing out ${wallet}\n\n')
    exit()
  else:
    print("That was not a valid option, please try again\n")
    options()

def welcome():
 print('Welcome to the Slot Machine!\n \n')
  
    
  


welcome()
make_choice()