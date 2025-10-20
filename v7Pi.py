import random

# Rock-paper-scissors game
print("Start 'rock-paper-scissors'")
print("Input your hand chose")
print("0=rock, 1=scissors, 2=paper")

# Get player input
player = int(input())

# Get computer choice (random)
computer = random.randint(0, 2)

# Determine outcome
if player == computer:
    print("Draw")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("Win")
else:
    print("Lose")
