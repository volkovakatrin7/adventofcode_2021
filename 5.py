def get_lists(reader):
    buffer = list(map(string_to_list_arrow_sep, reader))
    for i in range(len(buffer)):
        buffer[i] = list(map(string_to_list_comma_sep, buffer[i]))
        for j in range(len(buffer[i])):
            buffer[i][j] = list(map(string_to_int, buffer[i][j]))
    return buffer


def string_to_list_arrow_sep(my_string):
    buffer = my_string.split("->")
    return buffer


def string_to_list_comma_sep(my_string):
    my_list = my_string.split(",")
    return my_list


def string_to_int(my_string):
    return int(my_string.strip())


def create_map(size):
    map = list((list(0 for i in range(size))) for i in range(size))
    return map


def main():
    # open file and read line for line
    with open("data5.txt", "r") as f:
        reader = f.readlines()
        coordinates = get_lists(reader)

        map = create_map(1000)

        for entry in coordinates:
            x1 = entry[0][0]
            x2 = entry[1][0]
            y1 = entry[0][1]
            y2 = entry[1][1]

            # only horizontal and vertical lines
            if x1 == x2 or y1 == y2:
                # check the order of coordinates and swap if necessary
                if x1 > x2:
                    temp = x2
                    x2 = x1
                    x1 = temp

                if y1 > y2:
                    temp = y2
                    y2 = y1
                    y1 = temp

                # loop over coordinates to draw a line on the map
                for y in range(y1, (y2+1)):
                    for x in range(x1, (x2+1)):
                        map[y][x] += 1

            # diagonal lines
            else:
                # draw a point and see, where the next point is. Repeat just until the final point
                while (y1 != y2) and (x1 != x2):
                    map[y1][x1] += 1
                    if y1 < y2:
                        y1 +=1
                    elif y1 > y2:
                        y1 -=1

                    if x1 < x2:
                        x1 += 1
                    elif x1 > x2:
                        x1 -= 1
                # draw the final point
                map[y1][x1] += 1

    counter = 0
    for row in map:
        for item in row:
            if item > 1:
                counter +=1
    print(counter)

if __name__ == "__main__":
    main()