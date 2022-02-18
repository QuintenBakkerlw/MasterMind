from Def1 import main_combination
from Def2 import combination_generator
from Def3 import combination_checker

"Opdracht MasterMind"
"Gemaakt door : Quinten Bakker"
"Klas : V1B"
n = 4
lst = ["G", "Y", "R", "B", "B", "W", "O", "B"]
combination_2 = ['G', 'B', 'W', 'O']
combinations = combination_generator(lst, n)
main_combi = main_combination(combinations)




def simple_solution(main_combo,lst):

    ## maar een variable van de feedback ##
    results = combination_checker(main_combo, lst[0])

    for i in lst:
        ## kijkt voor elke element in de combinatie lst of de results dezelfde zijn als de eerste combinatie ##
        results_2 = combination_checker(lst[0], i)

        ## Als het combinatie dezelfde is dan endigt de algoritme
        if results == (4, 0):
            return print('correct')

        ## maakt een new lst met mogelijke combinaties ##
        elif results == results_2:
            new_lst = []
            new_lst.append(i)

    ## herhaalt de functie tot dat het corret is ##
    return simple_solution(main_combo, new_lst)

print(simple_solution(main_combi,combinations))



