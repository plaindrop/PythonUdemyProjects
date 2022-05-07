print("...rock...\n...paper...\n...scissors...\n")

player1_choice = input("(enter Player 1's choice): ")
player2_choice = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1_choice == "rock" and player2_choice == "scissors":
    print("player1 wins!")
elif player1_choice == "paper" and player2_choice == "rock":
    print("player1 wins!")
elif player1_choice == "scissors" and player2_choice == "paper":
    print("player1 wins!")
elif player1_choice == "scissors" and player2_choice == "rock":
    print("player2 wins!")
elif player1_choice == "rock" and player2_choice == "paper":
    print("player2 wins!")
elif player1_choice == "paper" and player2_choice == "scissors":
    print("player2 wins!")
elif player1_choice == player2_choice:
    print("It's a tie!")
else:
    print("Something went wrong.")