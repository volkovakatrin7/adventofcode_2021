def split_comma(text):
    return text.split(",")

def main():
    with open("data6.txt", "r") as f:
        reader = f.read()

        data = split_comma(reader)
        fish = list(map(int, data))

        population = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            for f in fish:
                if f == i:
                    population[i] +=1

        days = 256
        total = [population]

        for day in range(days):
            new = [0,0,0,0,0,0,0,0,0]
            new[0] = total[day][1]
            new[1] = total[day][2]
            new[2] = total[day][3]
            new[3] = total[day][4]
            new[4] = total[day][5]
            new[5] = total[day][6]
            new[6] = total[day][0] + total[day][7]
            new[7] = total[day][8]
            new[8] = total[day][0]
            total.append(new)

        total_of_fish = 0
        for item in total[days]:
            total_of_fish += item
        print(total_of_fish)


if __name__ == "__main__":
    main()