from typing import List, Dict


def to_dict(number):
    return {number: False}


def play(tables, random_numbers):
    # draw a number
    for number in random_numbers:

        # mark it on all boards
        for table in tables:
            for row in table:
                for item in row:
                    if number in item.keys():
                        item[number] = True

        # check each board's row & each board's column
        for table in tables:
            for row in table:
                counter = 0
                for item in row:
                    if True in item.values():
                        counter += 1
                if counter == 5:
                    print("counter (line) reached 5")
                    print("last winning number: ", number)
                    return table

            for i in range(5):
                counter = 0
                for j in range(5):
                    if True in table[j][i].values():
                        counter += 1
                if counter == 5:
                    print("counter (column) reached 5")
                    print("last winning number: ", number)
                    return table


def loose(tables, random_numbers):
    # draw a number
    counter_tables = 0
    for number in random_numbers:

        # mark it on all boards
        for table in tables:
            for row in table:
                for item in row:
                    if number in item.keys():
                        item[number] = True

        # check each board's row & each board's column
        for i in range(len(tables)):
            for row in tables[i]:
                counter = 0
                for item in row:
                    if True in item.values():
                        counter += 1
                if counter == 5:
                    if counter_tables == 99:
                        for table in tables:
                            for row in table:
                                print(row)
                            print("\n")

                        print(number)
                        for row in tables[i]:
                            print(row)
                        return tables[i]
                    else:
                        tables[i] = [[{-1: False}]*5]*5  # turn winning board upside down
                        counter_tables += 1

            for a in range(5):
                counter = 0
                for j in range(5):
                    if True in tables[i][j][a].values():
                        counter += 1
                if counter == 5:
                    if counter_tables == 99:
                        for table in tables:
                            for row in table:
                                print(row)
                            print("\n")


                        print(number)
                        for row in tables[i]:
                            print(row)
                        return tables[i]
                    else:
                        tables[i] = [[{-1: False}]*5]*5  # turn winning board upside down
                        counter_tables += 1


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
        # print(tables)
        # print(tables[0])

    # loop ofer the list, change false to true, stop if counter reaches 5
    # winning_table = play(tables, random_numbers)
    # for row in winning_table:
    # print(row)

    # calculate result
    # sum_false = 0
    # for line in winning_table:
    #   for number in line:
    #      if False in number.values():
    #         sum_false += list(number.keys())[0]

    # print(sum_false)

    last_winning = loose(tables, random_numbers)
    sum_false = 0
    for line in last_winning:
       for number in line:
          if False in number.values():
             sum_false += list(number.keys())[0]
    print(sum_false)





if __name__ == "__main__":
    main()
