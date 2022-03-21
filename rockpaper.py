import random
computer_choice = random.choice(['rock','paper','scissors'])
user_choice = input('do you want - rock,paper,scissors?\n')
if computer_choice == user_choice:
    print('TIE')
elif (user_choice == 'paper') and (computer_choice == 'scissors'):
    print('Computer won! '+ computer_choice)
elif (user_choice == 'rock') and (computer_choice == 'paper'):
    print('Computer won! '+ computer_choice)
elif (user_choice == 'scissors') and (computer_choice == 'rock'):
    print('Computer won! '+ computer_choice)
else:
    print('you won, computer choice was '+ computer_choice)