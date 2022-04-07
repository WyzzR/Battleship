"""battleship.py: battleship game"""


# creates a grid size x size
def create_grid(size):
    result = []
    for i in range(size):
        result.append([])
        for j in range(size):
            result[i].append(" ")
    return result


# prints the grid with everything on it column by column
def show_grid(grid):
    size = range(len(grid))
    for i in size:
        for j in size:
            print(f"| {grid[j][i]:5}", end="")
        print("\n")


def peek_grid(grid):
    pass


# ask user for coordinates as one string and converts it to a list of tuples
# input example: "1,4 2,4 3,4" -> output: [(1, 4), (2, 4), (3, 4)]
def get_location():
    result = []

    # ask user for input
    location = str(input("Enter the coordinates: "))
    coordinates = location.split()

    for i in coordinates:
        (x_cord, y_cord) = (int(i.split(",")[0]), int(i.split(",")[1]))
        result.append((x_cord, y_cord))

    return result


# player a adds ships to the grid with the coordinates from get_location()
def add_ships():
    global grid_p1, grid_p2, played
    ships = 0

    # checks whos turn it is
    if played:
        grid = grid_p1
        player = "1"
    else:
        grid = grid_p2
        player = "2"

    while ships < 5:
        available = True
        coord = get_location()

        # check if all coords are available
        for i in coord:
            if grid[i[0]][i[1]] != " ":
                available = False

        if available:
            for i in coord:
                grid[i[0]][i[1]] = "ship"
            print(
                f"--------------------- Player {player}'s grid ----------------------"
            )
            show_grid(grid)
            ships += 1
        else:
            print("Unavailable space. A ship is already there")


# asks each player to place their ships
def start():
    global grid_p1, grid_p2, played

    # starts with player 1 as True
    played = True

    grid_p1 = create_grid(10)
    grid_p2 = create_grid(10)

    # add ships to player 1
    print("Add your ships player 1")
    add_ships()
    played = False

    # add ships to player 2
    print("Add your ships player 2")
    add_ships()


# player a attacks the other player at coordinate (x, y)
def attack():
    pass


def main():
    start()


if __name__ == "__main__":
    main()
