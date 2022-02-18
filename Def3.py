# m_combination = ['yellow', 'blue', 'red', 'white']
# combination = ['yellow', 'yellow', 'black', 'black']
def combination_checker(m_combination, combination):
    lst = []
    red = 0
    white = 0
    for index in range(0, 3):
        if m_combination[index] == combination[index]:
            red += 1
            lst.append(index)


    for i in reversed(lst):
        m_combination.remove(m_combination[i])


    for x in range(0, len(m_combination)):
        if m_combination[x] in combination:
            white += 1

    return red, white

