import random

small=int(input('Enter smaller number: '))
big=int(input('Enter biger number: '))

computerNumber=random.randint(small,big)
computerNumber=int(computerNumber)

print('You have 3 chances to find a correct number betwin smaller number and biger number')

user=int(input("Enter your ans: "))

if user == computerNumber:
    print("you win")
else:
    print('you have 2 chances')
    if user>computerNumber:
        print('your number is biger')
    else:
        print('your number is smaller')
        
    user=int(input("Enter your ans: "))
    
    if user == computerNumber:
        print("you win")
    else:
        print('you have 1 chances')
    if user>computerNumber:
        print('your number is biger')
    else:
        print('your number is smaller')
        
    user=int(input("Enter your ans: "))
    
    if user == computerNumber:
        print("you win")
    else:
        print('you have loss')
        print('corect number is', computerNumber)
    