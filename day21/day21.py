import os
from collections import defaultdict
with open(f'{os.getcwd()}/day21/data.txt', 'r') as f:
    data = f.read()

# data = """
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# """

foods = data.strip().splitlines()

# allergen -> {possible ingredient, }
allergen_map = defaultdict(set)
unassigned_allergens = set()
unassigned_ingredients = set()
ing_count = defaultdict(int)

for food in foods:
    ingredients, allergens = food[:-1].split('(contains ')

    ingredients = set(ingredients.strip().split(' '))
    for ing in ingredients:
        ing_count[ing] += 1
    unassigned_ingredients.update(ingredients)

    for allergen in allergens.split(', '):
        unassigned_allergens.add(allergen)
        if allergen in allergen_map:
            allergen_map[allergen] &= ingredients
        else:
            allergen_map[allergen].update(ingredients)

# list of ings that contain an allergen definitely
bad_ings = []
while len(unassigned_allergens) > 0:
    for allergen, ing_set in allergen_map.items():
        inter = ing_set & unassigned_ingredients
        if len(inter) == 1:
            ing = inter.pop()
            unassigned_allergens.remove(allergen)
            unassigned_ingredients.remove(ing)
            bad_ings.append((allergen, ing))
            break
    else:
        raise AssertionError('ut oh! that didn\'t work')

print(f'Part 1: {sum([ing_count[ing] for ing in unassigned_ingredients])}')
print(f'Part 2: {",".join([ing for _, ing in sorted(bad_ings)])}')
