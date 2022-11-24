def main():
    with open("data9.txt", "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(digit) for digit in line] for line in data]
        for line in data:
            print(line)
        #print(len(data))

        total = 0
        for row in range(0, len(data)):
            for column in range(0, len(data[row])):
                minimum = True

                if row < (len(data) - 1):
                    if data[row][column] >= data[row + 1][column]:
                        minimum = False
                if row > 0:
                    if data[row][column] >= data[row - 1][column]:
                        minimum = False
                if column < (len(data[row]) - 1):
                    if data[row][column] >= data[row][column + 1]:
                        minimum = False
                if column > 0:
                    if data[row][column] >= data[row][column - 1]:
                        minimum = False

                if minimum:
                    total += (data[row][column] + 1)
        print(total)


if __name__ == "__main__":
    main()