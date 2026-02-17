.str()

.replace("text_to_replace", "text_to_change_it_to")

.lower()

.upper()


# Update pasta type to be more specific
pasta_type = "pasta"
pasta_type = pasta_type.replace("pasta","fusilli pasta")

# Standardize ingredient_one to lowercase

ingredient_one = "BASIL"
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)