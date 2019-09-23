#restart =('Y')
wallet = 0
import random


def add_funds(): 
    global wallet
    amount = float(input("Enter amount to be added to your wallet: ")) 
    wallet += amount 
    print(f"Amount added: ${amount:.2f}")
    balance_checker()

def balance_checker():
    global wallet
    print(f'Your wallet balance is: ${wallet:.2f}')
    welcome()


def spin_reels():
    a,b,c = [random.randint(0,15),random.randint(0,15),random.randint(0,15)]
    print(a, b, c)
    if a != b or a != c:
      pass
    else: 
      print ("You win 100!")
      wallet += bet_amount + 100
      balance_checker()
      print('Play again???') 
    welcome()  

def bet():
  global wallet
  bet_amount = float(input("Enter the amount of your bet: "))
  if wallet >= bet_amount:
    wallet -= bet_amount
    spin_reels()
  else:
    print ("You do not have enough money for that bet...Please add funds to your wallet")
  welcome()

def welcome():
  global wallet
  print('Welcome to the Slot Machine!')
  print('Please Press 1 For Your wallet balance\n')
  print('Please Press 2 To Add funds to your wallet\n')
  print('Please Press 3 To SPIN the wheels!\n')
  print('Please Press 4 To Cash out\n')  
  option = int(input('What Would you like to do?'))   
  if option == 1:
    balance_checker()
    print ('Ready to spin??')
  elif option == 2:
    add_funds()
    balance_checker()
    print('Ready to spin??')
  elif option == 3:
    bet()
    spin_reels()
  elif option == 4:
    print ('Thank you for playing!!')
    print(f'Cashing out ${wallet}')
    exit()
  else:
    print("That was not a valid option, please try again")


welcome()