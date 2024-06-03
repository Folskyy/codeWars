def cakes(recipe, available):
    return min([((available[ingredient] // recipe[ingredient]) if ingredient in available else 0) for ingredient in recipe])

recipe1 = {'flour': 500, 'sugar': 200, 'eggs': 1}
available1 = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

recipe2 = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available2 = {'sugar': 500, 'flour': 2000, 'milk': 2000}

recipe3 = {"flour": 500, "sugar": 200, "eggs": 1}
available3 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe4 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available4 = {"sugar": 500, "flour": 2000, "milk": 2000}

print(f"Receita 1: {cakes(recipe1, available1)}")
print(f"Receita 2: {cakes(recipe2, available2)}")
print(f"Receita 3: {cakes(recipe3, available3)}")
print(f"Receita 4: {cakes(recipe4, available4)}")

# def cakes(recipe, available):
#     return min(available.get(k, 0) // recipe[k] for k in recipe)
# available.get(k, 0): Tenta obter o valor de available[k]. Se k não estiver presente em available, retorna 0.