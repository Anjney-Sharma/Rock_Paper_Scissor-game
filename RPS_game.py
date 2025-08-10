import random

print("~~//Welcome To Rock Paper Scissors Game\\~~")

user_score=0
comp_score=0
ties=0

name=input("Enter your name")
print("""
GAME RULES
1. ROCK VS PAPER-->PAPER WINS
2. SCISSORS VS PAPER-->SCISSORS WINS
3. ROCK VS SCISSORS-->ROCK WINS""")
while True:
    choice= int(input("Choose 1 ,2 or 3 \n 1 for rock\n 2 for paper\n 3 for scissors"))

    while choice >3 or choice<1:
        choice = int(input("Enter valid input"))
    if choice == 1: 
        user_choice ='Rock'
    elif choice == 2:
            user_choice ='Paper'
    else:
            user_choice ='Scissors'

    print("\nYou choose : ",user_choice)        

    computer = random.randint(1,3)
    if computer == 1:
        comp_choice ='Rock'
    elif computer == 2:
        comp_choice ='Paper'
    else:
        comp_choice ='Scissors'

    print("computer choose :",comp_choice)

    if ((user_choice=="Rock" and comp_choice=="Paper")or(user_choice=="Paper" and comp_choice=="Rock")):
        print("\nPaper wins")
        result="Paper"
    elif ((user_choice=="Rock" and comp_choice=="Scissors")or(user_choice=="Scissors" and comp_choice=="Rock")):
        print("\nRock wins")
        result="Rock"
    elif (user_choice==comp_choice):
        print("\nIts a tie")
        result="Tie"
    else:
        print("\nScissors wins")
        result="Scissors"

    if result=="Tie":
        ties+=1
    elif result==user_choice:
        print("\nYou won")
        user_score+=1
    else:
        print("\ncomputer wins")
        comp_score+=1

    print("\nTHE SCORES ARE :-")
    print(name,"'s score is",user_score)
    print("Computer score is : ",comp_score)
    print("Ties :",ties)

    repeat=input('Do you want to play again? \nYES OR NO')
    if repeat == "no" or repeat == "NO":
        break
print("GAME OVER")
print("THANKS FOR PLAYING")