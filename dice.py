import random
import time

def roll_dice(sides):
    dice_results= []
    for side in sides:
        roll_result= random.randint(1,side+1)
        dice_results.append(roll_result)
    return dice_results
#change so it utilizes random.sample
def dice_fell(roll_result):	 
    player1_dice= player1_dice_results
    player2_dice= player2_dice_results
    for item in player1_dice:
        if item % 4 == 0:
            player1_dice.remove(item)
            return player1_dice

    for item in player2_dice:
        if item % 4 == 0:
            player2_dice.remove(item)
            return player2_dice

dice_set1=[4,6,8,10,12,20,100]
dice_set2=[4,6,8,10,12,20,100]

player1_score = 0
player2_score = 0

while player1_score < 3 or player2_score < 3:
    player1_dice_results = roll_dice(dice_set1)
    player2_dice_results = roll_dice(dice_set2)

    player1_final_results = dice_fell(player1_dice_results)
    player2_final_results = dice_fell(player2_dice_results)

    player1_total= sum(player1_dice_results)
    player2_total= sum(player2_dice_results)

    exit= input(str("Press Enter to start! Press 'q' to leave after each round! \n"))
    if exit != "q":
        print("Let's begin! Be careful for the small table!")
    elif exit == "q":
        quit()

    print("You are rolling...")
    time.sleep(2)
    print("You have rolled: ",player1_final_results)
    if len(player1_final_results) != 7:
        print("Sorry player 1, some of your dice has fallen off the table!")
    elif len(player1_final_results) == 0:
        print("Whoa there! Ease up on the rolling!")
    print()
    print("Your total is: ",player1_total)
    print()

    print("Player 2 is rolling...")
    time.sleep(2)
    print("Player 2 has rolled:" ,player2_final_results)
    if len(player2_final_results) != 7:
        print("Sorry player 2, some of your dice has fallen off the table!")
    elif len(player2_final_results) == 0:
        print("Whoa there! Ease up on the rolling!")
    print()
    print("Player 2's total is: ",player2_total)
    print()
    
    if player1_total > player2_total:
        print()
        print("You have won the round with,",player1_total,"!"),
        player1_score += 1
        print("Your score is: ",player1_score)
    elif player2_total > player1_total:
        print()
        print("Player 2 has won the round with,",player2_total,"!"),
        player2_score += 1
        print("Player 2's score is: ",player2_score)

    if player1_score == 3:
    	print("Congratulations, you won!")
    elif player2_score == 3:
    	print("Player 2 wins! Better luck next time champ!")