import random
# Rock Paper Scissors Game
player = int(input("Enter a number(1-3): "))
computer = random.randint(1, 3)
print(computer)
if player == computer:
    print("It's a tie!")
elif(player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("The Player Wins!")
else:
    print("The Computer Wins!")
