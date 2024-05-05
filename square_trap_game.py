def grid_creator(horizontal_lines):
    vertical_lines = horizontal_lines + 1

    grid = []
    for _ in range(horizontal_lines):
        vertical = [" "] * vertical_lines
        grid.append(vertical)

    return grid


def grid_printer(grid):
    VERTICAL_COORDINATES = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for coordinate in range(len(grid[0])):
        print(f"  {VERTICAL_COORDINATES[coordinate]}  ", end="")

    print("")
    for row in range(len(grid)):
        if row > 0:
            print("  |  " * len(grid[0]))
        print(str(row + 1) + " ", end="")

        for col in range(len(grid)):
            print(f"{grid[row][col]}----", end="")
            if col == len(grid) - 1:
                print(f"{grid[row][col + 1]}", end="")

        print(" " + str(row + 1))

    for coordinate in range(len(grid[0])):
        print(f"  {VERTICAL_COORDINATES[coordinate]}  ", end="")

    print("")


def get_line_count(string):
    MIN_LINES = 3
    MAX_LINES = 7

    invalid_input = True

    while invalid_input:
        try:
            line_count = int(input(string))

            if MIN_LINES <= line_count <= MAX_LINES:
                invalid_input = False
                return line_count
            else:
                print(f"Enter a number between {MIN_LINES} and {MAX_LINES}.")

        except ValueError:
            print("Invalid input.")


def place_stones(horizontal, grid):
    stone_count = horizontal * (horizontal + 1)
    white_stone_count = stone_count / 2
    black_stone_count = stone_count / 2

    turn_number = 1

    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    vertical = horizontal + 1
    columns = columns[0:vertical]

    black_squares = 0
    white_squares = 0

    while white_stone_count != 0 or black_stone_count != 0:
        position_input = "Enter the position you want to place your stone: "

        list1 = check_position(grid, position_input, True, "A")
        row_count = list1[0]
        column_count = list1[1]

        if turn_number % 2 == 0:
            black_stone_count -= 1
            grid[int(row_count) - 1][columns.index(column_count)] = "S"
            black_squares += count_squares(grid, int(row_count) - 1, columns.index(column_count), "S")
            grid_printer(grid)
        else:
            white_stone_count -= 1
            grid[int(row_count) - 1][columns.index(column_count)] = "B"
            white_squares += count_squares(grid, int(row_count) - 1, columns.index(column_count), "B")
            grid_printer(grid)

        turn_number += 1

    return black_squares, white_squares


def check_position(grid, text, place, stone_to_remove):
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    row, column = 0, 0
    invalid_input = True
    while invalid_input:
        try:
            stone = input(text)
            row = stone[0]
            column = stone[1]

            if len(grid) < int(row):
                print("Row number is out of range.")
                invalid_input = True
            elif column not in columns:
                print("Column number is out of range.")
                invalid_input = True

            else:
                invalid_input = False

            if place:
                if grid[int(row) - 1][columns.index(column)] != " ":
                    print("The desired position is occupied.")
                    invalid_input = True
                else:
                    invalid_input = False
            else:
                stone_status = grid[int(row) - 1][columns.index(column)]
                if stone_to_remove == "S":
                    if stone_status == "B" or stone_status == " ":
                        invalid_input = True
                elif stone_to_remove == "B":
                    if stone_status == "S" or stone_status == " ":
                        invalid_input = True
                else:
                    invalid_input = False

        except ValueError:
            print("Invalid input.")

    if not invalid_input:
        stone_x = int(row) - 1
        stone_y = columns.index(column)
        return [row, column, stone_x, stone_y]


def remove_stones(grid, black_square_count, white_square_count):
    while white_square_count != 0 or black_square_count != 0:
        invalid_input = True
        while invalid_input:
            try:
                if white_square_count > 0:
                    invalid_exit = True
                    while invalid_exit:
                        list1 = check_position(grid, "Enter the position of the Black stone to remove: ", False, "S")
                        stone_x = list1[2]
                        stone_y = list1[3]

                        if count_squares(grid, stone_x, stone_y, "S") > 0:
                            print("There is a square, the stone cannot be removed.")
                            invalid_input = True
                            invalid_exit = True
                        else:
                            invalid_input = False
                            invalid_exit = False
                            grid[stone_x][stone_y] = " "
                            grid_printer(grid)
                            white_square_count -= 1
                else:
                    if black_square_count > 0:
                        invalid_exit = True
                        while invalid_exit:
                            list1 = check_position(grid, "Enter the position of the White stone to remove: ", False, "B")
                            stone_x = list1[2]
                            stone_y = list1[3]

                            if count_squares(grid, stone_x, stone_y, "B") > 0:
                                print("There is a square, the stone cannot be removed.")
                                invalid_input = True
                                invalid_exit = True
                            else:
                                invalid_input = False
                                invalid_exit = False
                                grid[stone_x][stone_y] = " "
                                grid_printer(grid)
                                black_square_count -= 1

            except ValueError:
                print("Invalid input.")


def count_squares(grid, stone_x, stone_y, stone_type):
    square_count = 0
    try:
        if (grid[stone_x][stone_y - 1] == stone_type and
                grid[stone_x - 1][stone_y] == stone_type and grid[stone_x - 1][stone_y - 1] == stone_type):
            square_count += 1

        if (grid[stone_x][stone_y - 1] == stone_type and
                grid[stone_x + 1][stone_y] == stone_type and grid[stone_x + 1][stone_y - 1] == stone_type):
            square_count += 1

        if (grid[stone_x - 1][stone_y] == stone_type and
                grid[stone_x][stone_y + 1] == stone_type and grid[stone_x - 1][stone_y + 1] == stone_type):
            square_count += 1

        if (grid[stone_x + 1][stone_y] == stone_type and
                grid[stone_x][stone_y + 1] == stone_type and grid[stone_x + 1][stone_y + 1] == stone_type):
            square_count += 1
    except IndexError:
        pass

    return square_count


def move_stone(grid, turn_number):
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]

    invalid_input = True
    while invalid_input:
        try:
            if turn_number % 2 == 0:
                input_data = input("Enter the positions of the Black stone to move [OldPlace NewPlace]: ")
                old_stone_row = int(input_data[0]) - 1
                old_stone_column = input_data[1]
                old_stone_column_index = columns.index(old_stone_column)
                new_stone_row = int(input_data[3]) - 1
                new_stone_column = input_data[4]

                if grid[old_stone_row][old_stone_column_index] == "B":
                    raise ValueError

            else:
                input_data = input("Enter the positions of the White stone to move [OldPlace NewPlace]: ")
                old_stone_row = int(input_data[0]) - 1
                old_stone_column = input_data[1]
                old_stone_column_index = columns.index(old_stone_column)
                new_stone_row = int(input_data[3]) - 1
                new_stone_column = input_data[4]

                if grid[old_stone_row][old_stone_column_index] == "S":
                    raise ValueError

            if len(grid) < int(old_stone_row) or len(grid) < int(new_stone_row):
                print("Row number is out of range.")
                invalid_input = True
            elif old_stone_column not in columns or new_stone_column not in columns:
                print("Column number is out of range.")
                invalid_input = True

            old_stone_column = columns.index(old_stone_column)
            new_stone_column = columns.index(new_stone_column)

            if old_stone_row == new_stone_row:
                if old_stone_column < new_stone_column:
                    for col in range(old_stone_column, new_stone_column):
                        if grid[old_stone_row][col + 1] != " ":
                            print("Another stone is blocking the movement.")
                            break
                    else:
                        invalid_input = False
                        finalize_movement(grid, old_stone_row, old_stone_column, new_stone_row, new_stone_column)

            if old_stone_row == new_stone_row:
                if old_stone_column > new_stone_column:
                    for col in range(new_stone_column, old_stone_column):
                        if grid[old_stone_row][col] != " ":
                            print("Another stone is blocking the movement.")
                            break
                    else:
                        invalid_input = False
                        finalize_movement(grid, old_stone_row, old_stone_column, new_stone_row, new_stone_column)

            if old_stone_column == new_stone_column:
                if old_stone_row < new_stone_row:
                    for row in range(old_stone_row, new_stone_row):
                        if grid[row + 1][old_stone_column] != " ":
                            print("Another stone is blocking the movement.")
                            break
                    else:
                        invalid_input = False
                        finalize_movement(grid, old_stone_row, old_stone_column, new_stone_row, new_stone_column)

            if old_stone_column == new_stone_column:
                if old_stone_row > new_stone_row:
                    for row in range(new_stone_row, old_stone_row):
                        if grid[row][old_stone_column] != " ":
                            print("Another stone is blocking the movement.")
                            break
                    else:
                        invalid_input = False
                        finalize_movement(grid, old_stone_row, old_stone_column, new_stone_row, new_stone_column)

        except ValueError:
            print("Invalid input.")


def finalize_movement(grid, old_row, old_column, new_row, new_column):
    grid[new_row][new_column] = grid[old_row][old_column]
    grid[old_row][old_column] = " "
    grid_printer(grid)

    if count_squares(grid, new_row, new_column, grid[new_row][new_column]) > 0:
        black_square = 0
        white_square = 0
        stone_color = grid[new_row][new_column]
        if stone_color == "S":
            black_square += 1
        elif stone_color == "B":
            white_square += 1
        remove_stones(grid, black_square, white_square)


def count_stones(grid):
    black_count = 0
    white_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                black_count += 1
            elif grid[row][col] == "B":
                white_count += 1

    return black_count, white_count


def main():
    horizontal = get_line_count("Enter the number of horizontal lines [3-7]: ")
    plane = grid_creator(horizontal)

    turn_number = 1

    grid_printer(plane)
    black_square_count, white_square_count = place_stones(horizontal, plane)

    if black_square_count == 0 and white_square_count == 0:
        remove_stones(plane, 0, 1)

    remove_stones(plane, black_square_count, white_square_count)

    black_count, white_count = count_stones(plane)

    while black_count > 3 and white_count > 3:
        move_stone(plane, turn_number)
        turn_number += 1
        black_count, white_count = count_stones(plane)

    if black_count > white_count:
        print("The black player won.")
    else:
        print("The white player won.")


main()
