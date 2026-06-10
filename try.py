def square_of_odds(int_list):
    return [x**2 for x in int_list if x % 2 != 0]

print(square_of_odds([2,4,3]))