# WiredIn Academy - Rock Paper Scissors Exercise

This repository contains the complete solution for the WiredIn Academy Python trial exercise: building a rock-paper-scissors game with progressive complexity.

## Exercise Overview

The exercise consists of 7 progressive Python programming tasks that build upon each other, demonstrating fundamental programming concepts through a familiar game implementation.

## Files Structure

| File | Description | Lines | Key Concepts |
|------|-------------|-------|--------------|
| `y5YT.py` | Basic game with input/output | 16 | Variables, random numbers, basic I/O |
| `v7Pi.py` | Win/lose/draw logic | 21 | Conditional statements, game rules |
| `a5Qm.py` | Functionalized program | 32 | Functions, modularity, mathematical optimization |
| `gP6s.py` | Hand name display | 43 | Lists, string formatting, user experience |
| `dV9E.py` | Dynamic input messages | 44 | List iteration, string concatenation |
| `L2rT.py` | Dictionary result display | 50 | Dictionaries, key-value mapping |
| `Jv5e.py` | Recursive draw handling | 59 | Recursion, control flow, game state |

## Game Rules

- 0 = Rock
- 1 = Scissors  
- 2 = Paper

**Win Conditions:**
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

## Technical Implementation

### Core Algorithm
The win/lose logic uses modular arithmetic for efficiency:
```python
hand_diff = (player - computer) % 3
```

### Key Programming Concepts Demonstrated

1. **Basic Programming**: Variables, input/output, random number generation
2. **Conditional Logic**: Complex boolean expressions, game rule implementation
3. **Function Design**: Modular code organization, parameter passing, return values
4. **Data Structures**: Lists for hand names, dictionaries for result messages
5. **String Manipulation**: f-string formatting, dynamic content generation
6. **Recursion**: Recursive function calls for continuous play until resolution
7. **Code Optimization**: Mathematical solutions over explicit conditionals

## Usage

Each file can be run independently to demonstrate the progression:

```bash
python y5YT.py  # Basic version
python v7Pi.py  # With win/lose logic
python a5Qm.py  # Functionalized
python gP6s.py  # With hand names
python dV9E.py  # Dynamic input
python L2rT.py  # Dictionary results
python Jv5e.py  # Complete recursive game
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Learning Objectives

This exercise demonstrates:
- Progressive code complexity
- Function decomposition
- Data structure selection
- Algorithm optimization
- User experience design
- Code maintainability
- Recursive problem solving

## Author

Mathieu Munyakazi  
ALU Student  
Email: m.munyakazi1@alustudent.com
