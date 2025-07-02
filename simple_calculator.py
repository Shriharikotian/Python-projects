try:
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))

    choice=input("1)enter a for addition"
    "\n2)enter s for subtraction"
    "\n3)enter m for multiplicetion"
    "\n4)enter d for division")

    match choice:
        case 'a':
            print(a+b)

        case 's':
            print(a-b)
        
        case 'm':
            print(a*b)
        
        case 'd':
            print(a/b)
        case _:
            print("wrong input")
except Exception as e:
    print("enter the valid a and b")