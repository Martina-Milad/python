mode = input("Welcome to Martina's calculator:\nFor standard calculator press (1)\nFor programmer calculator press(2)\n")
while(1):
	if mode == '1':
		print("please enter 2 numbers to prefom a mathmatical operation on\n")
		num1 = float(input("enter first number\n"))
		num2 = float(input("enter second number\n"))
		choice = input("Select Opration:\n1.Add\n2.Subtract\n3.multiply\n4.Divide\n")
		if choice == '1':
			print(num1, "+", num2, "=", num1+num2 )
		elif choice == '2':
			print(num1, "-", num2, "=", num1-num2 )
		elif choice == '3':
			print(num1, "*", num2 ,"=" ,num1*num2 )
		elif choice == '4':
			print(num1, "/", num2 ,"=" ,num1/num2 )
		else:
			print("Invalid choice")	
			
		new=input("another operation? (yes/no)\n")
		if(new == "no"):
			break	
		
		
		
	elif mode == '2':
		press = input("For number convertion press(1)\nfor bitwise operations press (2)\n")
		if press == "1":
			number= int(input("enter a decimal number\n"))
			convert = input("Convert the decimal number to:\n1.Binary\n2.Octal\n3.Hexadecimal\n")
			if convert == '1':
				print("the binary representation of" , number, "is" , bin(number) )
			elif convert == '2':
				print("the Octal representation of" , number, "is" , oct(number) )
			elif convert == '3':
				print("the Hexadecimal representation of" , number, "is" , hex(number) )
			else:
				print("Invalid number")	
				
			new=input("another convertion? (yes/no)\n")
			if(new == "no"):
				break
		elif press == "2":
			num1 = int(input("enter first number\n"))
			num2 = int(input("enter second number\n"))
			choice = input("Select Opration:\n1.bitwise AND\n2.bitwise OR\n3.bitwise XOR\n4.Shift left\n5.Shift Right")
			if choice == '1':
				print(num1, "&", num2, "=", num1&num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '2':
				print(num1, "|", num2, "=",num1|num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '3':
				print(num1, "^", num2 ,"=" ,num1^num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '4':
				print(num1, "<<", num2 ,"=" ,num1<<num2, "\nwhich equal", bin(num1<<num2), "in binary\n" )
			elif choice == '5':
				print(num1, ">>", num2 ,"=" ,num1>>num2, "\nwhich equal", bin(num1>>num2), "in binary\n" )
				
			new=input("another operation? (yes/no)\n")
			if(new == "no"):
				break	
			else:
				print("Invalid choice")

		
		
	else:
		print("Invalid number")