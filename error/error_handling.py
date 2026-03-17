# try - except error catch

#This is useful when our code is not sequrntial and it doesnt depend on each other to run
# Avoid errors being produced
# Still execute subsequent code 

def average(values):
    try:
        average_values = sum(values) / len(values)
        return average_values 
    except:
        print("average() accepts list olt set. Please provide a correct data type.")


## Will produce an erro
## Avoid executing subsequent code 

def shopping_list_cost(cost):
    if type(cost) in (list, set):
        total_cost = sum(cost)
        return total_cost
    else:
        raise TypeError("shopping_list_cost() accepts list or set. Please provide a correct data type.")