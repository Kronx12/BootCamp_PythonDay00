import sys

cookbook = {
    'sandwich': {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': "lunch",
        'prep_time': 10
    },
    'cake': {
        'ingredients': ["flour", "sugar", "eggs"],
        'meal': "dessert",
        'prep_time': 60
    },
    'salad': {
        'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
        'meal': "lunch",
        'prep_time': 15
    }
}


def print_all():
    for k in cookbook.keys():
        print(k.capitalize())


def print_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if (cookbook.get(recipe_name) is not None):
        print("Recipe for %s:" % recipe_name.capitalize())
        print("Ingredients list:",
              cookbook.get(recipe_name).get("ingredients"))
        print("To be eaten for %s." % cookbook.get(recipe_name).get("meal"))
        print("Takes %d minutes of cooking." %
              cookbook.get(recipe_name).get("prep_time"))
    else:
        print("Recipe %s does not exist !" % recipe_name)


def delete_recipe(recipe_name):
    cookbook.pop(recipe_name, None)


def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name.lower()] = {'ingredients': ingredients, 'meal': meal,
                                     'prep_time': prep_time}


in_val = 0
while (in_val != 5):
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    print(">> ", end='')
    invalid = True
    while invalid:
        try:
            in_val = int(input())
            if (in_val < 1 or in_val > 5):
                print("\nThis option does not exist, please type the " +
                      "corresponding number.")
                print("To exit, enter 5.\n\n>> ", end='')
            else:
                invalid = False
        except ValueError:
            print("\nThis option does not exist, please " +
                  "type the corresponding number.")
            print("To exit, enter 5.\n\n>> ", end='')
    if in_val == 5:
        print("\nCookbook closed")
    elif in_val == 4:
        print("\n")
        print_all()
    elif in_val == 3:
        print("\nPlease enter the recipe's name to get " +
              "its details:\n>> ", end='')
        name = input()
        print("")
        print_recipe(name)
    elif in_val == 2:
        print("\nPlease enter the recipe's name to delete it:\n>> ", end='')
        delete_recipe(input())
    elif in_val == 1:
        print("\nPlease enter the recipe's name to create it:\n>> ", end='')
        recipe_name = input()
        print("\nPlease enter the ingredients with this format " +
              "\"ingredient1, ingredient2, ingredient3, ...\":\n>> ", end='')
        ingredients = input().split(", ")
        print("\nPlease enter the meal type:\n>> ", end='')
        meal = input()
        time = 0
        tmp = True
        print("\nPlease enter the time for make it:\n>> ", end='')
        while tmp:
            try:
                time = int(input())
                tmp = False
            except ValueError:
                print("\nPlease just enter a number:\n>> ", end='')
        add_recipe(recipe_name, ingredients, meal, time)
