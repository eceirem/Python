healty_choice = {'cup sour cream': {'cup yogurt': 1},
                 'cup milk': {'cup evaporated milk': 1/2,
                              'and': 'and',
                              'cup water': 1/2},
                 'teaspoon lemon juice': {'teaspoon vinegar': 1/2},
                 'cup sugar': {'cup honey': 1/2,
                               'and': 'and',
                               'cup molasses': 1,
                               'or': 'or',
                               'cup avage nectar': 1/4},
                 'cup butter': {'cup margarine': 1,
                                'or': 'or',
                                'cup yogurt': 1},
                 'cup flour': {'cup rye': 1,
                               'or': 'or',
                               'cup rice flour': 1},
                 'cup mayonnaise': {'cup cottage cheese': 1,
                                    'or': 'or',
                                    'cup mayonnaise': 1/8,
                                    'and': 'and',
                                    'cup yogurt': 7/8},
                 'egg': {'tablespoons cornstarch': 2,
                         'and': 'and',
                         'arrowroot flour': 1,
                         'or': 'or',
                         'potato starch': 1,
                         'or': 'or',
                         'egg whites': 2,
                         'or': 'or',
                         'large banana(mashed)': 1/2},
                 'cup milk': {'cup soy milk': 1},
                 'cup oil': {'cup applesauce': 1}}

ingredient = input()
quantity = int(input())

for key, value in healty_choice.items():
    if key == ingredient:
        print(f'SUBSTITUTION OF {quantity} {key.upper()} IS')
        for value2 in value:
            if healty_choice[key][value2] == 'and' or healty_choice[key][value2] == 'or':
                print(healty_choice[key][value2], end= ' ')
            else:
                print(healty_choice[key][value2] * quantity, value2, end= ' ')