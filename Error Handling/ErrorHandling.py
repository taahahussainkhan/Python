
#- - - - - - - - - - - - - - - - - - -E R R O R  H A N D L I N G - - - - - - - - - - - - - - - - - - - - - - -    
#The two numbers must be integar, but what if some user enters a non-integar What do you think will happen?
#Yeah exactly , it'll give an error and the program will be halted without executing the remaining statements of the program.
#To tackle this situation, we use try-except statements, it prevents the program to halt.

try:
    num1 = int(input("Enter first number (must be integar) : "))
    num2 = int(input("Enter second number (must be integar) : "))    
    print(f'Sum: {num1 + num2}')

except Exception as e:  # ' e ' can be any name.
    print('Error Occured!', e) # ' e ' is an object that contains the information about the error.


#T.H.K Codes