import random

def rolldice():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    return (dice1, dice2)

def displaydice(dice):
    (dice1, dice2)= dice
    print(f'Player rolled {dice1} + {dice2} = {sum(dice)}')

die_values = rolldice()
displaydice(die_values)

sum_of_dice = sum(die_values)

if sum_of_dice in (7,11):
    game_status ='WON'
elif sum_of_dice in (2,3,12):
    game_status = 'LOST'
else:
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('point is',my_point)

while game_status = 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    if sum_of_dice == my_point:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOST'

if __name__ == '__main__':
    for i in range(1,10):
        displaydice(rolldice())


