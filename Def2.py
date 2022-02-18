import itertools
n = 4
lst = ["G", "Y", "R", "B", "B", "W", "O", "B"]
def combination_generator(lst, n):
    lijstcombinatie = []
    lijst = []
    for L in range(0, len(lst) + 1):
        for subset in itertools.combinations(lst, L):
            lijst.append(list(subset))
            for item in lijst:
                if len(item) is not n:
                    lijst.remove(item)
    for item in lijst:
        lijstcombinatie.append(item)
    return lijstcombinatie








# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements