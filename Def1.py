import random
from Def2 import combination_generator
"Random combination generator"
lst = ["G", "Y", "R", "B", "B", "W", "O", "B"]
n = 4
lst = combination_generator(lst,n)
def main_combination(lst):
    combination = random.choice(lst)

    return combination





