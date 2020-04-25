#앞으로의 수정 계획 1, 난이도 조절 (2와 6일때만 게임을 이기는것이 아니라 3이나 5등을 추가
#새로운 주사위 룰 추가 합이아니라 곱셈을 이용 할 수 도있다..
#
import time
import random

dice1 = """
__________
| #1      |
|         |
|    O	  |
|         |
|_________|"""

dice2 = """
__________
| #2      |
|      O  |
|    	  |
|  O      |
|_________|"""

dice3 = """
__________
|#3       |
|      O  |
|    O	  |
|  O      |
|_________|"""

dice4 = """
__________
|#4       |  
|  O   O  |
|    	  |
|  O   O  |
|_________|"""

dice5 = """
__________
|#5       |
|  O   O  |
|    O	  |
|  O   O  |
|_________|"""

dice6 = """
__________
|#6       |
|  O   O  |
|  O   O  |
|  O   O  |
|_________|"""

dice_list = (dice1, dice2, dice3, dice4, dice5, dice6)

# Seconds that the dice animation will be shown
animation_duration_time = 10
time_end = time.time() + animation_duration_time


def roll_dice():
    while time.time() < time_end:
        print(random.choice(dice))


time.sleep(1)

def dice():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice = die1 + die2
        print("You roll a", die1, "and", die2, "for a total of", dice)
        print(dice_list[die1 - 1])
        print(dice_list[die2 - 1], '\n')

        return dice