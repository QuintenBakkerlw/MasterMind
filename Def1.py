import random

"Random combination generator"
n = 4
lst = ["green", "yellow", "red", "blue", "black", "white", "orange", "brown"]
def combination_maker(lst,n):
    combination = []
    for i in range(0,n):
        random_element = random.choice(lst)
        combination.append(random_element)
    return combination

print(combination_maker(lst,n))

