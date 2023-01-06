# Variable to provide an accurate intiger value and use it to find change and return to the user.
purchases=[]
Water = 1.00
coldtea = 3.00
coldcoffe = 4.00
pepsi = 2.50
chips= 0.50
snickers = 3.50
kitkat = 2.50
cookie=4.50
peanuts=3.50
strawberry = 1.50
redbull = 9.50
cupramen = 4.00
vegsandwich = 4.50
nonvegsandwich = 5.00
burger = 5.00
pizza = 6.50
#	A menu of drinks and snacks presented via the console.
# A set of catagories which takes you to certain required items
def menu():
  print("~~~~~~~~~ WELCOME TO THE VENDING MACHINE ~~~~~~~~~")
  print("__________________________________________________")
  print(" What whould you like to have today ? \n")
  print("1. Snacks")
  print("2. Drinks")
  print("3. Food")
  print("\nChoose the category you want.")
  print("__________________________________________________\n")
# ask the user to choose a category
  inp=int(input("Type in the number: "))
# if inputs the number it takes them to the actual menu
  if inp == 1:
    print("__________________________________________________\n")
    print("Product      Price        Code\n")
    print("Chips        0.50 dhs      107")
    print("Snickers Bar 3.50 dhs      108")
    print("Kit kat      2.50 dhs      109")
    print("Cookie       4.50 dhs      110")
    print("Peanuts      3.50 dhs      111")
# the user can choose anything from the given menu
  elif inp == 2:
    print("__________________________________________________\n")
    print("Product         Price        Code\n")
    print("Water           1.00 dhs      101")
    print("Cold Tea        3.00 dhs      102")
    print("Cold coffee     4.00 dhs      103")
    print("Pepsi           2.50 dhs      104")
    print("Straberry Milk  1.50 dhs      105")
    print("Red bull        9.50 dhs      106")
  elif inp == 3:
    print("__________________________________________________\n")
    print("Product           Price        Code\n")
    print("Cup ramen         4.00 dhs      112")
    print("Veg sandwich      4.50 dhs      113")
    print("Non-veg sandwich  5.00 dhs      114")
    print("Burger            5.00 dhs      115")
    print("Pizza             6.50 dhs      116")
  else:
    print("Wrong code !")
    return menu()
menu()

def user():
# ask the user if he/she need anythig else
  print('Would you like to have anything else ?')
  print("__________________________________________________\n")
  UserInput=str(input("Type 'yes' or 'no'"))
  if UserInput == 'yes':
    print("\n")
    menu()
    item_select() 
# if the user is done with his order print a final message and end the programe
  else:
    print("===================================================")
    print("-------------------- THANK YOU! -------------------")
    print("----------- HOPE WE SEE YOU AGAIN SOON! -----------")
    print("===================================================")
def item_select():
# ask the user to input the code from the menu to select their item  
  UserInput =int(input("\nENTER THE CODE : "))
# this captures all the inputed codes by the user to the list called 'purchases'
  purchases.append(UserInput)
  if UserInput == 101:
    print("__________________________________________________")
    print("""
    Item you have selected: Water 
    Price: 1.00 dhs""")
    print("__________________________________________________")
# after selecting an item "payment" shows how much the user have paid 
    payment=float(input("\nInsert your amount: "))
# "water" is a variable i created in the begining to give a correct amount for the item
    if payment < Water:
# if the user enters lesser amount the machine asks for balance amount to complete the purchase
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ") 
# "balance" shows the amount more needed to complete the purchase
      balance = Water-payment
      print("\nPay",float(balance),"to complete payment\n")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________")   
    elif payment >= Water:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
# "change" shows the amount returned by the vending machine      
      change = payment-Water
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()

#same code used for the above output 
  elif UserInput == 102:
    print("""
    you have selected: Cold Tea 
    Price: 3.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < coldtea:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = coldtea-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= coldtea:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-coldtea
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")    
    user()

  elif UserInput == 103:
    print("""
    you have selected: Cold Coffee 
    Price: 4.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < coldcoffe:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = coldcoffe-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= coldcoffe:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-coldcoffe
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
  
  elif UserInput == 104:
    print("""
    you have selected: Pepsi 
    Price: 2.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < pepsi:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = pepsi-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= pepsi:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")     
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-pepsi
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
   
  elif UserInput == 105:
    print("""
    you have selected: Strawberry milk 
    Price: 1.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < strawberry:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = strawberry-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= strawberry :
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")      
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-strawberry
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
  
  elif UserInput == 106:
    print("""
    you have selected: Red bull 
    Price: 9.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < redbull:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = redbull-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= redbull :
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-redbull
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
   
  elif UserInput == 107:
    print("""
    you have selected: Chips 
    Price: 0.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < chips:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = chips-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= chips:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-chips
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
    
  elif UserInput == 108:
    print("""
    you have selected: Snickers Bar 
    Price: 3.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < snickers:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = snickers-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= snickers:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-snickers
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
    
  elif UserInput == 109:
    print("""
    you have selected: Kit kat 
    Price: 2.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < kitkat:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = kitkat-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= kitkat:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-kitkat
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
  
  elif UserInput == 110:
    print("""
    you have selected: Cookie 
    Price: 4.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < cookie:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = cookie-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= cookie:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-cookie
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")
    user()
    
  elif UserInput == 111:
    print("""
    you have selected: Peanuts 
    Price: 3.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < peanuts:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = peanuts-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= peanuts:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-peanuts
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
  
  elif UserInput == 112:
    print("""
    you have selected: Cup ramen  
    Price: 4.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < cupramen:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = cupramen-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= cupramen:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-cupramen
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
  
  elif UserInput == 113:
    print("""
    you have selected: Veg sandwich   
    Price: 4.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < vegsandwich:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = vegsandwich-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= vegsandwich:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-vegsandwich
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
 
  elif UserInput == 114:
    print("""
    you have selected: Non-veg sandwich   
    Price: 5.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < nonvegsandwich:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = nonvegsandwich-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= nonvegsandwich:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-nonvegsandwich
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
  
  elif UserInput == 115:
    print("""
    you have selected: Burger   
    Price: 5.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < burger:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = burger-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= burger:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-burger
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
  
  elif UserInput == 116:
    print("""
    you have selected: Pizza   
    Price: 6.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < pizza:
      print("__________________________________________________\n")
      print("    PAYMENT NOT COMPLETE !    ")
      balance = pizza-payment
      print("Pay",float(balance),"to complete payment")
      bal=float(input("Enter balance amount: "))
      if bal==balance:
        print("    PAYMENT COMPLETE!    ")
        print("__________________________________________________") 
    elif payment >= pizza:
      print("~~~~~~~~~~~~~~~~~~~~~ RECEIPT ~~~~~~~~~~~~~~~~~~~~~")
      print("___________________________________________________")
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-pizza
      print("\nYour change is : ",float(change),'dhs')
      print("___________________________________________________")  
    user()
#if user inputs the wrong code from the given menu 
#it prints "wrong code" and gives the user chances to input again until user enters the right code
  else:
    print("Wrong Code")
    print("Try again !")
    return item_select()
item_select()
# at the end after all the order and payment is done print a message to show the user that item is dispensed by the machine.
print("----------YOUR ITEM'S HAVE BEEN DISPENSED!---------")
print("===================================================")
# END of the programe
