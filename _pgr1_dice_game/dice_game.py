import random
import sys

roll_again = True

start = int(input("Bet money and roll the dice and get as close as you can to 21 total score, Start game 1 yes, 2 no:"))

money = 1000
total_score = 0
rounds = 3
win = False


if start == 1:

    if rounds > 0:

        while rounds > 0:
            bet = int(input(f"You have {money}$ how much do you what to bet:"))
            print(f"total money on round {rounds} is {money}")

            
            while roll_again == True:
                number_on_dice = random.randint(1, 6)
                roll = int(input("Roll the dice 1 yes, 2 no:"))
                
                if roll == 1:

                    total_score = number_on_dice + total_score

                    print(number_on_dice)
                    print("Your total is score: ",total_score )

                    roll_again = True

                    if total_score > 21:
                        print("you lost")
                        roll_again = False
                        win = False

                    else:
                        continue
                    
                elif roll == 2: 
                    roll_again = False
                    win = True  


            if roll_again == False:
                end_score = 21 - total_score
                print(f"Your score was: {total_score}\nAnd you where {end_score} off.") 
                

            if roll_again == False:
                rounds = rounds - 1
                roll_again = True
                

                if win == True and total_score == 21:
                    money = money + bet * 5
                    total_score = 0

                elif win == True and total_score >= 18 and total_score <= 20:      
                    money = money + bet * 3
                    total_score = 0

                elif win == True and total_score >= 16 and total_score <= 18 :
                    money = money + bet * 2
                    total_score = 0

                elif win == True and total_score >= 14 and total_score <= 16 :
                    money = money + bet 
                    total_score = 0  

                else:   
                    money = money - bet
                    roll_again = True
                    total_score = 0
    else:
        print(f"End of game you won {money}$")
        sys.exit()

else:
    print("bye, bye")
    sys.exit()
    