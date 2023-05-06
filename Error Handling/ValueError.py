while True:
    try:
        x=int(input("Enter x: "))
    except ValueError:
        print(f'x is not and integar!')
    else:
        break
print(f'x is {x}')
    
    #This will prompt the user again and again until the correct input is entered.