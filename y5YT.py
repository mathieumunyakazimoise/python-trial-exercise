import random

# Rock-paper-scissors game
print("Start 'rock-paper-scissors'")
print("Input your hand chose")
print("0=rock, 1=scissors, 2=paper")

# Get player input
player = int(input())

# Get computer choice (random)
computer = random.randint(0, 2)

print(f"player: {player}")
print(f"computer: {computer}")
