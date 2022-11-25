def main():
    with open("data9.txt", "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[{int(digit): None} for digit in line] for line in data]

        number_of_basins = 0
        for row in range(0, len(data)):
            for column in range(0, len(data[row])):
                current_point = list(data[row][column].keys())[0]

                # assume we have found a new basin
                new_basin_found = True

                # check if the height is 9. If so, this is not a basin
                if current_point == 9:
                    new_basin_found = False

                # if the height is deeper than 9, check two neighbours: on the left-side and above
                else:
                    if row > 0:
                        adjacent_basin_above = list(data[row - 1][column].values())[0]
                        if adjacent_basin_above:
                            new_basin_found = False
                            data[row][column][current_point] = adjacent_basin_above
                    current_basin = list(data[row][column].values())[0]

                    if column > 0:
                        adjacent_basin_left = list(data[row][column - 1].values())[0]
                        if adjacent_basin_left:
                            new_basin_found = False
                            # if the neighbours on the left and above belong to different basins, merge two basins
                            if current_basin and current_basin != adjacent_basin_left:
                                # in order to merge two basins: loop back and replace basins' numbers
                                for x in range(row + 1):
                                    for y in range(column + 1):
                                        target_basin = list(data[row - x][column - y].values())[0]
                                        target_point = list(data[row - x][column - y].keys())[0]
                                        if target_basin == adjacent_basin_left:
                                            data[row - x][column - y][target_point] = current_basin

                            else:
                                data[row][column][current_point] = adjacent_basin_left
                                new_basin_found = False

                if new_basin_found:
                    number_of_basins += 1
                    data[row][column][current_point] = number_of_basins

        # create a list of basins. Basin with index 0 will put onto the list, because it contains points with height 9
        basins = []
        for i in range(number_of_basins+1):
            basins.append(0)
        for row in data:
            for point in row:
                basin = list(point.values())[0]
                if basin:
                    basins[basin] += 1
        basins.sort(reverse=True)
        print(basins)
        first_largest_basin = basins[0]
        second_largest_basin = basins[1]
        third_largest_basin = basins[2]
        result = first_largest_basin * second_largest_basin * third_largest_basin
        print(result)

if __name__ == "__main__":
    main()