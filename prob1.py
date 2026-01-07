pantry = ["Eggs", "flour", "Milk", "eggs", "salt"]
recipe = ["flour", "milk", "Sugar", "Eggs", "butter"]

def check_ingredients(pantry_list, recipe_list):
   
    pantry_set = set(item.lower() for item in pantry_list)
    recipe_set = set(item.lower() for item in recipe_list)
    missing_items = sorted(recipe_set - pantry_set)
    available_items = sorted(recipe_set & pantry_set)
    return missing_items, available_items

missing, available = check_ingredients(pantry, recipe)

print(f"Need to buy: {missing}")
print(f"Already have: {available}")