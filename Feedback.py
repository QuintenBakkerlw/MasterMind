combination_1 = ['B', 'B', 'L', 'P']
combination_2 = ['B', 'B', 'L', 'P']

def combination_checker(combination_1, combination_2):
    memory = []
    new_combination = []
    red = 0
    white = 0
    for i in range(0, len(combination_1)):
        if combination_1[i] == combination_2[i]:
            red += 1
            memory.append(combination_1.index(combination_1[i]))

    for x in combination_1:
        new_combination.append(x)

    for index in reversed(memory):
        del new_combination[index]

    for x in range(0, len(new_combination)):
        if new_combination[x] in combination_2:
            white += 1

    return red, white










