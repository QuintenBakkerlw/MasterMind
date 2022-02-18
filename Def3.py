
def combination_checker(combination_1, combination_2):
    lst = []
    red = 0
    white = 0
    for i in range(0, len(combination_1)):
        if combination_1[i] == combination_2[i]:
            red += 1
            lst.append(combination_1.index(combination_1[i]))

    for x in reversed(lst):
        del combination_1[x]

    for y in range(0, len(combination_1)):
        if combination_1[y] in combination_2:
            white += 1

    return red, white








