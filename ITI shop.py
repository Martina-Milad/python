print("Welcome to ITI shop\n\n")
menu = {'apple' : '20' ,
		'banana' : '15' ,
		'orange' :'12'
		}
while(1):
	mode = input("Select Mode:\n\t-For customer press (1)\n\t-For Owner press(2)\n\t-To Exit press(0)\n")

	if mode =='1':  #customer mode
		customer = input("Hello Customer...\n\t-To show our products press (1)\n\t-To buy from our products press(2)\n\t-To Exit press(0)\n")
		if customer   ==  '1':
			print("\t\t Our Menu\n", menu)
		elif customer ==  '2':
			name = input("enter the product name\n")
			print("price for ", name," = ")
			print( int((menu[name])) )
			kilos_numbers = int( input("enter how many kilos you would like to buy\n"))
			pay = int((menu[name])) * kilos_numbers
			print("for", kilos_numbers , "kilos of ", name, " you should pay ", pay)
		elif customer == '0':
			break
					
	elif mode =='2': #Owner mode
		owner = input("Hello Owner...\n\t-To add new products press (1)\n\t-To buy from our products press(2)\n\t-To Exit press(0)\n")
		if owner   ==  '1':
			key = input("enter the product name\n")
			value = input("enter the product cost\n")
			menu.update({key: value})
			print("the updated menu is\n" , menu)
		elif owner ==  '2':
			name = input("enter the product name\n")
			print("price for ", name," = ")
			print( int((menu[name])) )
			kilos_numbers = int( input("enter how many kilos you would like to buy\n"))
			pay = int((menu[name])) * kilos_numbers
			print("for", kilos_numbers , "kilos of ", name, " you should pay ", pay)
		elif owner == '0':
			break
	elif mode == '0':
			break
