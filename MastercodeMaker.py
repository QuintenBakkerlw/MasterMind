import random
from combinationGerator import combination_generator
"Random combination generator"
lst = ["G", "Y", "R", "B", "W", "O", "B"]
n = 4
lst = combination_generator(lst,n)
def main_combination(lst):
    combination = random.choice(lst)
    a_set = set(combination)

    contains_duplicates = len(combination) != len(a_set)
    if contains_duplicates == True:
        return main_combination(lst)
    else:
        return combination







