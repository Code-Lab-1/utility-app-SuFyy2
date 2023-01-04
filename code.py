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
  print("  Welcome to THE vending machine  \n")
  print(" What whould you like to have today ? \n")
  print("1. Snacks")
  print("2. Drinks")
  print("3. Food")
  print("\nChoose the category you want.") 
# ask the user to choose a category
  inp=int(input("Type in the number: "))
# if inputs the number it takes them to the actual menu
  if inp == 1:
    print("\n")
    print("Product      Price        Code\n")
    print("Chips        0.50 dhs      107")
    print("Snickers Bar 3.50 dhs      108")
    print("Kit kat      2.50 dhs      109")
    print("Cookie       4.50 dhs      110")
    print("Peanuts      3.50 dhs      111")
# the user can choose anything from the given menu
  elif inp == 2:
    print("\n")
    print("Product         Price        Code\n")
    print("Water           1.00 dhs      101")
    print("Cold Tea        3.00 dhs      102")
    print("Cold coffee     4.00 dhs      103")
    print("Pepsi           2.50 dhs      104")
    print("Straberry Milk  1.50 dhs      105")
    print("Red bull        9.50 dhs      106")
  elif inp == 3:
    print("\n")
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
#ask the user if he/she need anythig else
  print('\nWould you like to have anything else ?')
  UserInput=str(input("Type 'yes' or 'no'"))
  if UserInput == 'yes':
    print("\n")
    menu()
    item_select() 
# if the user is done with his order print a final message and end the programe
  else:
    print("\nTHANK YOU! for using THE vending machine")
    print("HOPE WE SEE YOU AGAIN SOON!")

def item_select():
# ask the user to input the code from the menu to select their item  
  UserInput =int(input("\nENTER THE CODE : "))
# this captures all the inputed codes by the user to the list called 'purchases'
  purchases.append(UserInput)
  if UserInput == 101:
    print("""
    you have selected: Water 
    Price: 1.00 dhs""")

#after selecting an item "payment" shows how much the user have paid 
    payment=float(input("\nInsert your amount: "))
 #"water" is a variable i created in the begining to give a correct amount for the item
    if payment < Water:
#if the user enters lesser amount the machine asks for balance amount to complete the purchase
      print("Payment not complete") 
#"balance" shows the amount more needed to complete the purchase
      balance = Water-payment
      print("Pay",float(balance),"to complete payment")
    
    elif payment >= Water:
      print("\nyou have paid : ",float(payment),'dhs')
# "change" shows the amount returned by the vending machine      
      change = payment-Water
      print("\nDONT FORGET YOUR CHANGE!")
      print("Your change is : ",float(change),'dhs')
    user()

#same code used for the above output 
  elif UserInput == 102:
    print("""
    you have selected: Cold Tea 
    Price: 3.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < coldtea:
      print("Payment not complete")
      balance = coldtea-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= coldtea:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-coldtea
      print("Your change is : ",float(change),'dhs')    
    user()

  elif UserInput == 103:
    print("""
    you have selected: Cold Coffee 
    Price: 4.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < coldcoffe:
      print("Payment not complete")
      balance = coldcoffe-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= coldcoffe:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-coldcoffe
      print("Your change is : ",float(change),'dhs')
    user()
  
  elif UserInput == 104:
    print("""
    you have selected: Pepsi 
    Price: 2.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < pepsi:
      print("Payment not complete")
      balance = pepsi-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= pepsi:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-pepsi
      print("Your change is : ",float(change),'dhs')
    user()
   
  elif UserInput == 105:
    print("""
    you have selected: Strawberry milk 
    Price: 1.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < strawberry:
      print("Payment not complete")
      balance = strawberry-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= strawberry :
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-strawberry
      print("Your change is : ",float(change),'dhs')
    user()
  
  elif UserInput == 106:
    print("""
    you have selected: Red bull 
    Price: 9.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < redbull:
      print("Payment not complete")
      balance = redbull-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= redbull :
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-redbull
      print("Your change is : ",float(change),'dhs')
    user()
   
  elif UserInput == 107:
    print("""
    you have selected: Chips 
    Price: 0.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < chips:
      print("Payment not complete")
      balance = chips-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= chips:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-chips
      print("Your change is : ",float(change),'dhs')
    user()
    
  elif UserInput == 108:
    print("""
    you have selected: Snickers Bar 
    Price: 3.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < snickers:
      print("Payment not complete")
      balance = snickers-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= snickers:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-snickers
      print("Your change is : ",float(change),'dhs')
    user()
    
  elif UserInput == 109:
    print("""
    you have selected: Kit kat 
    Price: 2.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < kitkat:
      print("Payment not complete")
      balance = kitkat-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= kitkat:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-kitkat
      print("Your change is : ",float(change),'dhs')
    user()
  
  elif UserInput == 110:
    print("""
    you have selected: Cookie 
    Price: 4.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < cookie:
      print("Payment not complete")
      balance = cookie-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= cookie:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-cookie
      print("Your change is : ",float(change),'dhs')
    user()
    
  elif UserInput == 111:
    print("""
    you have selected: Peanuts 
    Price: 3.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < peanuts:
      print("Payment not complete")
      balance = peanuts-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= peanuts:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-peanuts
      print("Your change is : ",float(change),'dhs')  
    user()
  
  elif UserInput == 112:
    print("""
    you have selected: Cup ramen  
    Price: 4.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < cupramen:
      print("Payment not complete")
      balance = cupramen-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= cupramen:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-cupramen
      print("Your change is : ",float(change),'dhs')  
    user()
  
  elif UserInput == 113:
    print("""
    you have selected: Veg sandwich   
    Price: 4.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < vegsandwich:
      print("Payment not complete")
      balance = vegsandwich-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= vegsandwich:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-vegsandwich
      print("Your change is : ",float(change),'dhs')  
    user()
 
  elif UserInput == 114:
    print("""
    you have selected: Non-veg sandwich   
    Price: 5.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < nonvegsandwich:
      print("Payment not complete")
      balance = nonvegsandwich-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= nonvegsandwich:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-nonvegsandwich
      print("Your change is : ",float(change),'dhs')  
    user()
  
  elif UserInput == 115:
    print("""
    you have selected: Burger   
    Price: 5.00 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < burger:
      print("Payment not complete")
      balance = burger-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= burger:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-burger
      print("Your change is : ",float(change),'dhs')  
    user()
  
  elif UserInput == 116:
    print("""
    you have selected: Pizza   
    Price: 6.50 dhs""")
    payment=float(input("\nInsert your amount: "))
    
    if payment < pizza:
      print("Payment not complete")
      balance = pizza-payment
      print("Pay",float(balance),"to complete payment") 
    elif payment >= pizza:
      print("\nyou have paid : ",float(payment),'dhs')
      change = payment-pizza
      print("Your change is : ",float(change),'dhs')  
    user()
#if user inputs the wrong code from the given menu 
#it prints "wrong code" and gives the user chances to input again until user enters the right code
  else:
    print("Wrong Code")
    print("Try again !")
    return item_select()
item_select()
# at the end after all the order and payment is done print a message to show the user that item is dispensed by the machine.
print("\nYOUR ITEM'S HAVE BEEN DISPENSED!")
# END of the programe
