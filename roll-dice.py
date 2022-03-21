import random
roll = random.randint(1,6)
print("the computer rolled the dice and value is "+str(roll))
guess = int(input("guess the value of dice\n"))
if guess == roll:
    print('yes correct\n')
else:
    print("not correct\n")

