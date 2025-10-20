import random

def start_message():
    """Display start message"""
    print("Start 'rock-paper-scissors'")
    print("Input your hand")
    hands = ['rock', 'scissors', 'paper']
    print(f"0:{hands[0]}, 1:{hands[1]}, 2:{hands[2]}")

def get_player():
    """Get player input"""
    return int(input())

def get_computer():
    """Get computer's random choice"""
    return random.randint(0, 2)

def get_hand_name(hand_number):
    """Return hand name based on number"""
    hands = ['rock', 'scissors', 'paper']
    return hands[hand_number]

def view_hand(player, computer):
    """Display both player and computer hands"""
    print(f"My hand is {get_hand_name(player)}")
    print(f"Computer's hand is {get_hand_name(computer)}")

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
view_hand(player, computer)
hand_diff = (player - computer) % 3
view_result(hand_diff)
