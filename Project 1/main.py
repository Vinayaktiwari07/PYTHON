'''
1 = rock
-1 = paper
0 = scissor
'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer == you):
    print("Draw Match")

else:

    if (computer == -1 and you == 1):
        print("You Lose")

    elif (computer == -1 and you == 0):
        print("You Win")

    elif (computer == 1 and you == -1):
        print("You Win")

    elif (computer == 1 and you == 0):
        print("You Lose")

    elif (computer == 0 and you == 1):
        print("You Win")

    elif (computer == 0 and you == -1):
        print("You Lose")



