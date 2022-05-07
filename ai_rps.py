from random import randint

print("...rock...\n...paper...\n...scissors...\n")

player1_choice = input("(enter Player 1's choice):").lower()

rand_num = randint(1,3)

if rand_num == 1:
    ai_choice = "paper"
elif rand_num == 2:
    ai_choice = "rock"
else:
    ai_choice = "scissors"

if player1_choice == ai_choice:
    print(f"AI chose {ai_choice}")
    print("It's a tie!")
elif player1_choice == "rock" and ai_choice == "scissors":
    print(f"AI chose {ai_choice}")
    print("player1 wins!")
elif player1_choice == "paper" and ai_choice == "rock":
        print(f"AI chose {ai_choice}")
        print("player1 wins!")
elif player1_choice == "scissors" and ai_choice == "paper":
    print(f"AI chose {ai_choice}")
    print("player1 wins!")
elif player1_choice == "scissors" and ai_choice == "rock":
        print(f"AI chose {ai_choice}")
        print("AI wins!")
elif player1_choice == "rock" and ai_choice == "paper":
    print(f"AI chose {ai_choice}")
    print("AI wins!")
elif player1_choice == "paper" and ai_choice == "scissors":
    print(f"AI chose {ai_choice}")
    print("AI wins!")
else:
    print("Something went wrong.")