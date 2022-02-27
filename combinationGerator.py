import itertools
from itertools import combinations_with_replacement
n = 4
lst = ["G", "Y", "R", "B", "W", "O", "P", "L"]
def combination_generator(lst, n):
    lijstcombinatie = []
    lijst = []
    for L in range(0, len(lst) + 1):
        for subset in itertools.combinations(lst, L):
            lijst.append(list(subset))
            for item in lijst:
                if len(item) is not n:
                    lijst.remove(item)
    # for i in combinations_with_replacement(lst, n):
    #     lijstcombinatie.append(list(i))
    for item in lijst:
        lijstcombinatie.append(item)
    return lijstcombinatie
#print(combination_generator(lst,n))












# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements