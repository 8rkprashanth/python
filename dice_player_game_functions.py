import random

def roll_dice():
    dice_total=random.randint(1,6)+random.randint(1,6)
    return dice_total

def main():
    user1_roll_dice_value= roll_dice()
    user2_roll_dice_value= roll_dice()
    if user1_roll_dice_value> user2_roll_dice_value:
        print('user1 wins','user1 value ',user1_roll_dice_value, 'user2 value ',user2_roll_dice_value)
    elif user1_roll_dice_value< user2_roll_dice_value:
        print('user2 wins','user1 value is',user1_roll_dice_value, 'user2 value is',user2_roll_dice_value)
    else:
        print("tied",'user1 value is',user1_roll_dice_value, 'user2 value is',user2_roll_dice_value)


main()




