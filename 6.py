def split_comma(text):
    return text.split(",")

def main():
    with open("data6a.txt", "r") as f:
        reader = f.read()

        data = split_comma(reader)
        fish = list(map(int, data))
        print(fish)

        for i in range(30):
            print("After day", i+1, end=" ")
            for i in range(len(fish)):
                if fish[i] == 0:
                    fish[i] = 7
                    fish.append(-8)
                elif fish[i] == -9:
                    fish[i] = 7
                fish[i] -= 1
            print(fish)

        print(len(fish))

if __name__ == "__main__":
    main()