# For Loop


for value in sequence:
    action

# Looping through a List

ingredients = ["Pasta", "Tomatoes", "Garlic", "Basil", "Olive Oil", "Salt"]
quantities = [1000, 800, 40, 30, 30, 15]

# Loop through and Print ingredients
for ingredient in ingredients:
    print(ingredient)

# Loop through quantities
for qty in pasta_quantity:
    if qty > 500 :
        print("Plenty in Stock")
    elif qty >= 100:
        print("Enough for small portion")
    else:
        print("Nearly out!")



#Looping through dictionaries with keys and values 

food_lists = { "rice": 20, "pasta" : 43, "tomatoes": 32, "garlic": 21}

for item, qty in food_lists.items():
    print(item, ":", qty, "grams" )


# Itirate dictionary keys

for item in food_lists.key():
    print("Key is:", item)

for item in food_lists.value()
    print("value is:", item)



