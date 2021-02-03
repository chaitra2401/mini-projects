import random
print("*******************************************")
print("| Let's Play Rock,Paper,Scissors |")
print("*******************************************")

#list of elements
Inputs=["ROCK","PAPER","SCISSORS"]

#scores
computer_score=0
user_score=0

#rules
print("Rules for the game: \n"+"ROCK/SCISSOR -> ROCK WINS \n"+"ROCK/PAPER -> PAPER WINS \n"+"PAPER/SCISSOR -> SCISSOR WINS")

while True:
    computer_choice= str(random.choice(Inputs))
    user_choice=input("\n\nEnter your choice Rock,Paper,Scissors: ").upper()

    if user_choice == computer_choice:
        print("###### It's a Tie ######")

    elif user_choice == "ROCK":
        print("The Computer Choice is: ",computer_choice)
        print("The User Choice is: ",user_choice)
        if computer_choice == "PAPER":
            print("\n###### Computer Wins! ###### Paper covers Rock")
            computer_score+=1
        else:
            print("\n###### You Win! ###### Rock smashes scissor")
            user_score+=1

    elif user_choice == "PAPER":
        print("The Computer Choice is: ",computer_choice)
        print("The User Choice is: ",user_choice)
        if computer_choice == "SCISSORS":
             print("\n###### Computer Wins! ###### Scissor cuts Paper")
             computer_score += 1
        else:
              print("\n###### You Win! ###### Paper covers Rock")
              user_score+=1

    elif user_choice=="SCISSORS":
        print("The Computer Choice is: ",computer_choice)
        print("The User Choice is: ",user_choice)
        if computer_choice == "ROCK":
             print("\n###### Computer Wins! ###### Rock smashes Scissors")
             computer_score += 1
        else:
              print("\n###### You Win! ###### Scissors cuts Paper")
              user_score+=1

    else:
        print("\n######WRONG GAME######")
        
    print("\n\nDo you want to play again? (Yes/No): ") 
    ans = input() 
    # if user input n or N then condition is True
    if ans == 'yes' or ans=='Yes':
        continue
    elif ans=='no' or ans=='No':
        break
    else:
        print("Wrong input")

print("*********************************GAME OVER*********************************")
print("\nThanks for playing")

print("The scores are:\n")
print(f"Your score: {user_score}  Computer score: {computer_score}")

if user_score>computer_score:
    print("******************************")
    print("YOU WON THE GAME")
    print("******************************")
elif computer_score>user_score:
    print("******************************")
    print("COMPUTER WON THE GAME")
    print("******************************")
else:
    print("******************************")
    print("DRAW MATCH")
    print("******************************")
      
        
        
