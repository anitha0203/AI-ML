# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")
    
# Call the function
print_hello()


# TODO: Complete the function
def get_expected_cost(beds, baths):
    value = 80000 + (beds * 30000) + (baths * 10000)
    return value

print(get_expected_cost(0,0))



# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    return cost

sqft_walls = 400
sqft_ceiling = 150
sqft_per_gallon = 300
cost_per_gallon = 25

print(get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon))

