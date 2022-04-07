"""battleship.py: battleship game"""


# creates a grid size x size
def create_grid(size):
    result = []
    for i in range(size):
        result.append([])
        for j in range(size):
            result[i].append(0)
    return result

# player a adds ships on the grid at position (x, y)
# takes in a list of coordinates
def add_ships():
    pass

# ask user for coordinates as one string and converts it to a list of tuples
def get_location():
    pass

# player a attacks the other player at coordinate (x, y)
def attack():
    pass