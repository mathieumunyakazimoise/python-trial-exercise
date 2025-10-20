import random

def start_message():
    """Display start message"""
    print("Start 'rock-paper-scissors'")
    print("Input your hand chose")
    print("0=rock, 1=scissors, 2=paper")

def get_player():
    """Get player input"""
    return int(input())

def get_computer():
    """Get computer's random choice"""
    return random.randint(0, 2)

def view_result(hand_diff):
    """Display result based on hand difference"""
    if hand_diff == 0:
        print("Draw")
    elif hand_diff == 1 or hand_diff == -2:
        print("Win")
    else:
        print("Lose")

# Main game logic
start_message()
player = get_player()
computer = get_computer()
hand_diff = (player - computer) % 3
view_result(hand_diff)
