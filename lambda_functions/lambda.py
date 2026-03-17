## Lambda function represent an anonymous function

# x is use for a single argument

# The expression is the equivalent of the function body 

# Mo return statment is  to produce an output


# Single Argument Lambda
(lambda x: sum(x) / len(x))([3,6,9])

print((lambda x: sum(x) / len(x))([3,6,9]))

average = lambda x: sum(x) / len(x)

print(average([3,6,9]))


## Multiple Arguments Lambda

power = lambda x, y: x**y

print(power(2,3))


# Lamba functions with iterables

names = ["jone", "Sally", "Leah"]

capitalize = map(lambda x: x.capitalize(), names)

print(list(capitalize))


colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list
cleaned_list = list(cleaned)
print(cleaned_list)

# ['sarah_martinez', 'michael_chen', 'emily_brown']
