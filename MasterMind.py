from MastercodeMaker import main_combination
from combinationGerator import combination_generator
from Feedback import combination_checker

"Opdracht MasterMind"
"Gemaakt door : Quinten Bakker"
"Klas : V1B"


### MasterMind Game ###

"verander lengte van code"
n = 4
"lijst van kleuren"
lst = ["G", "Y", "R", "B", "W", "O", "P", "L"]

"kies je methode"
"1 = simple_solution"
"2 = human_guess"
"3 = human_master"
game = 2

### valut(Do not change) ##
count = 0
combinations = combination_generator(lst, n)
main_combi = main_combination(combinations)
##############################################

def simple_solution(main_combo, combinatielijst, count):
    new_lst = []

    ## maakt een variable van de feedback ##
    results = combination_checker(main_combo, combinatielijst[0])

    for i in combinatielijst:

        ## kijkt voor elke element in de combinatie lst of de results dezelfde zijn als de eerste combinatie ##
        results_2 = combination_checker(combinatielijst[0], i)

        ## maakt een new lst met mogelijke combinaties ##
        if results == results_2:
            new_lst.append(i)

    ## Als het combinatie dezelfde is dan endigt de algoritme
    if results == (4, 0):
        return print(f"correct {count}")
    ## herhaalt de functie tot dat het corret is ##
    return simple_solution(main_combi, new_lst, count + 1)


def human_guess(main_combi):
    number = 10
    print('colors : ["G", "Y", "R", "B", "W", "O", "P", "L"]')
    ## aantal kansen dat de speler krijgt
    while number != 0:
        combination_guess = []

        guess = input('Give you combination: ')
        ## maakt van de input een lst die de computer goed kan lezen ##
        for i in guess:
            combination_guess.append(i.upper())
        result = combination_checker(main_combi, combination_guess)

        ## als de combinaitie klopt dan endig loop ##
        if result == (4, 0):
            number = 0
            return print(f'___ WOW you did it in {number} turn"s ___')

        ## geeft alle feedback terug
        number -= 1
        print(f"___ You have {number} turn's left! ___")
        print(result)

    ## als kansen op zijn endig spel ##
    return print("___ You ran out of turn's better luck next time ___")


def human_master():
    master_code = []
    ## vraagt user om code ##
    master_input = input("[G, Y, R, B, W, O, P, L]\nright as 'gyrb' \nGive you master code: ")

    ## veranderd de input naar een leesbaar lst voor de code ##
    for i in master_input:
        master_code.append(i.upper())
    ## start de simple_solution functie ##
    return simple_solution(main_combi, combinations, count)


def choose_your_gamemode(game):
    ## van de input start die de juiste spel ##
    if game == 1:
        return simple_solution(main_combi, combinations, count)
    elif game == 2:
        return human_guess(main_combi)
    elif game == 3:
        return human_master()

print(choose_your_gamemode(game))










