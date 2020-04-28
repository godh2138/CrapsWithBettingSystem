
import time
import random

card1 = """
__________
|        |
|    1   |
|        |
|        |
|________|"""

card2 = """
__________
|         |
|         |
|   2 	  |
|         |
|________ |"""

card3 = """
__________
|         |
|         |
|    3	  |
|         |
|_________|"""

card4 = """
__________
|         |
|         |
|    4	  |
|         |
|_________|"""

card5 = """
__________
|         |
|         |
|    5    |
|         |
|_________|"""

card6 = """
__________
|         |
|         |
|    6    |
|         |
|_________|"""

card7 = """
__________
|         |
|         |
|    7    |
|         |
|_________|"""

card8 = """
__________
|         |
|         |
|    8    |
|         |
|_________|"""
card9 = """
__________
|         |
|         |
|    9    |
|         |
|_________|"""
card10 = """
__________
|         |
|         |
|    10   |
|         |
|_________|"""
card11= """
__________
|         |
|         |
|    11   |
|         |
|_________|"""
card12 = """
__________
|         |
|         |
|    12   |
|         |
|_________|"""
card13 = """
__________
|         |
|         |
|    13   |
|         |
|_________|"""
card14 = """
__________
|         |
|         |
|    14   |
|         |
|_________|"""
card15 = """
__________
|         |
|         |
|    15   |
|         |
|_________|"""


card_list = (card1,card2,card3,card4,card5,card6,card7,card8,card9,card10)
card_lis2t= (card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15)
# Seconds that the card animation will be shown
animation_duration_time = 20
time_end = time.time() + animation_duration_time


def roll_card():
    while time.time() < time_end:
        print(random.choice(card))


time.sleep(1)

def card():
        card1 = random.randint(1, 10)
        card2 = random.randint(1, 10)
        card = card1 + card2
       
        print("You get a", card1, "and", card2, "for a total of", card)
        print(card_list[card1 - 1])
        print(card_list[card2 - 1], '\n')
        
        return card
def card2():
        card3 = random.randint(1, 15)
        card4 = random.randint(1, 15)
        card_level2 = card3 + card4
       
        print("You get a", card1, "and", card2, "for a total of", card)
        print(card_list[card3 - 1])
        print(card_list[card4 - 1], '\n')
        
        return card
    

