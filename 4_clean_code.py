from typing import List, Dict


def to_dict(number):
    return {number: False}


def mark_number_on_boards(number, tables):
    for table in tables:
        for row in table:
            for item in row:
                if number in item.keys():
                    item[number] = True
    return tables


def check_row_and_column(table):
    winning_row = check_row(table)
    winning_column = check_column(table)
    if winning_row or winning_column:
        return True
    else:
        return False


def check_row(table):
    five_matches = False
    for row in table:
        counter = 0
        for item in row:
            if True in item.values():
                counter += 1
        if counter == 5:
            five_matches = True
    return five_matches


def check_column(table):
    five_matches = False
    for column in range(5):
        counter = 0
        for row in range(5):
            if True in table[row][column].values():
                counter += 1
        if counter == 5:
            five_matches = True
    return five_matches


def check_boards_left(counter_winning_boards):
    return counter_winning_boards == 100


def turn_board_upside_down():
    table = [[{-1: False}] * 5] * 5
    return table


def get_winner(tables, random_numbers):
    for number in random_numbers:
        tables = mark_number_on_boards(number, tables)

        for i in range(len(tables)):
            board_has_won = check_row_and_column(tables[i])
            if board_has_won:
                return {number: tables[i]}


def get_looser(tables, random_numbers):
    counter_winning_boards = 0

    for number in random_numbers:
        tables = mark_number_on_boards(number, tables)

        # check each board
        for i in range(len(tables)):
            board_has_won = check_row_and_column(tables[i])

            if board_has_won:
                counter_winning_boards += 1

                last_board_left = check_boards_left(counter_winning_boards)
                if last_board_left:
                    return {number: tables[i]}
                else:
                    tables[i] = turn_board_upside_down()


def main():
    # copy random numbers to a list
    random_numbers = [15, 61, 32, 33, 87, 17, 56, 73, 27, 83, 0, 18, 43, 8, 86, 37, 40, 6, 93, 25, 14, 68, 64, 57, 39,
                      46, 55, 13, 21, 72, 51, 81, 78, 79, 52, 65, 36, 92, 97, 28, 9, 24, 22, 69, 70, 42, 3, 4, 63, 50,
                      91, 16, 41, 94, 77, 85, 49, 12, 76, 67, 11, 62, 99, 54, 95, 1, 74, 34, 88, 89, 82, 48, 84, 98, 58,
                      44, 5, 53, 7, 19, 29, 30, 35, 26, 31, 10, 60, 59, 80, 71, 45, 38, 20, 66, 47, 2, 23, 96, 90, 75]

    # open file and read line for line
    with open("data4.txt", "r") as f:
        reader = f.readlines()

        # create a list of tables (100 tables)
        tables = []
        table_number = -1
        for line in reader:
            if line == '\n':
                tables.append([])  # generate new table
                table_number += 1
            else:
                row = list(map(int, line.split()))  # save the line data into a row of a table
                row = list(map(to_dict, row))
                tables[table_number].append(row)

    print("FIRST WINNING BOARD")
    winning_table = get_winner(tables, random_numbers)
    first_winning_number = list(winning_table.keys())[0]

    first_winning = list(winning_table.values())[0]
    for row in first_winning:
        print(row)
    print("\n")

    # calculate result
    sum_false = 0
    for line in first_winning:
        for number in line:
            if False in number.values():
                sum_false += list(number.keys())[0]
    print("Winning number: ", first_winning_number)
    print("Sum of remaining numbers: ", sum_false)
    result = first_winning_number * sum_false
    print("Result: " + str(result))

    print("\n\nLAST WINNING BOARD")
    last_winning = get_looser(tables, random_numbers)
    last_winning_number = list(last_winning.keys())[0]

    last_winning = list(last_winning.values())[0]

    for row in last_winning:
        print(row)
    print("\n")

    sum_false = 0
    for line in last_winning:
        for number in line:
            if False in number.values():
                sum_false += list(number.keys())[0]
    print("Winning number: ", first_winning_number)
    print("Sum of remaining numbers: ", sum_false)

    result = last_winning_number * sum_false
    print("Result: " + str(result))


if __name__ == "__main__":
    main()
