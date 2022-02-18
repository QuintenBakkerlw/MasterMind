import itertools
n = 4
lst = ["green", "yellow", "red", "blue", "black", "white", "orange", "brown"]
def combination_generator(lst, n):
    f = open("combination.txt", "w")
    lijst = []
    for L in range(0, len(lst) + 1):
        for subset in itertools.combinations(lst, L):
            lijst.append(subset)
            for item in lijst:
                if len(item) is not n:
                    lijst.remove(item)
    for item in lijst:
        f.write(f"{item}\n")
    return True

print(combination_generator(lst, n))

# stuff = [1, 2, 3]



# https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements