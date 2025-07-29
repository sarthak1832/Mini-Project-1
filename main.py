import random
'''
1 for snake
-1 for water 
0 for gun'''


computer = random.choice([-1, 0, 1])
userstr = (input("Enter your choice: "))
userDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

user = userDict[userstr]
#By now we have 2 numbers (variables) computer and user

print(f"User chose {reverseDict[user]}\nComputer chose {reverseDict[computer]}")

if(computer == user):
    print("Draw!")
          
else:
    if(computer == -1 and user == 1):
        print("You win!")
    
    elif(computer == -1 and user == 0):
        print("You lose!")
    
    elif(computer == 1 and user == 0):
        print("You win!")
        
    elif(computer == 1 and user == -1):
        print("You lose!")
    
    elif(computer == 0 and user == 1):
        print("You lose!")

    elif(computer == 0 and user == -1):
        print("You win!")

    else:
        print("Invalid input!")