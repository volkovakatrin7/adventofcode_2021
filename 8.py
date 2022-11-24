def decipher(pattern):
    keys = {}
    letters = ["a", "b", "c", "d", "e", "f", "g"]

    # decipher a: compare one and seven
    for digit in pattern:
        if len(digit) == 2:
            one = digit
        elif len(digit) == 3:
            seven = digit
        elif len(digit) == 4:
            four = digit
    for letter in one:
        seven = seven.replace(letter, "")
    keys["a"] = seven


    # decipher b, e, f: each appear a unique number of times
    for letter in letters:
        counter = 0
        for digit in pattern:
            if digit.rfind(letter) != -1:
                counter += 1
        if counter == 6:
            keys["b"] = letter
        elif counter == 4:
            keys["e"] = letter
        elif counter == 9:
            keys["f"] = letter

        # decipher c: appears the same number of times as a
        elif counter == 8 and letter != keys["a"]:
            keys["c"] = letter

    # decipher d: take four and clear of known values of b, c and f
    four = four.replace(keys["b"], "")
    four = four.replace(keys["c"], "")
    four = four.replace(keys["f"], "")
    keys["d"] = four

    for letter in letters:
        counter = 0
        for digit in pattern:
            if digit.rfind(letter) != -1:
                counter += 1
        if counter == 7 and letter != keys["d"]:
            keys["g"] = letter
    return keys


def main():
    with open("data8.txt", "r") as f:
        reader = f.readlines()

        data = [item.split("|") for item in reader]
        data = [[entry.split() for entry in line] for line in data]

        counter = 0

        for line in data:
            for i in line[1]:
                if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                    counter +=1

        print(f"1, 4, 7, 8 appear {counter} times ")

        grand_total = 0
        for line in data:
            keys = decipher(line[0])

            zero = sorted(keys["a"] + keys["b"] + keys["c"] + keys["e"] + keys["f"] + keys["g"])
            one = sorted(keys["c"] + keys["f"])
            two = sorted(keys["a"] + keys["c"] + keys["d"] + keys["e"] + keys["g"])
            three = sorted(keys["a"] + keys["c"] + keys["d"] + keys["f"] + keys["g"])
            four = sorted(keys["b"] + keys["c"] + keys["d"] + keys["f"])
            five = sorted(keys["a"] + keys["b"] + keys["d"] + keys["f"] + keys["g"])
            six = sorted(keys["a"] + keys["b"] + keys["d"] + keys["e"] + keys["f"] + keys["g"])
            seven = sorted(keys["a"] + keys["c"] + keys["f"])
            eight = sorted(keys["a"] + keys["b"] + keys["c"] + keys["d"] + keys["e"] + keys["f"] + keys["g"])
            nine = sorted(keys["a"] + keys["b"] + keys["c"] + keys["d"] + keys["f"] + keys["g"])

            sum = ""
            for digit in line[1]:
                digit = sorted(digit)
                if digit == zero:
                    sum += "0"
                elif digit == one:
                    sum += "1"
                elif digit == two:
                    sum += "2"
                elif digit == three:
                    sum += "3"
                elif digit == four:
                    sum += "4"
                elif digit == five:
                    sum += "5"
                elif digit == six:
                    sum += "6"
                elif digit == seven:
                    sum += "7"
                elif digit == eight:
                    sum += "8"
                elif digit == nine:
                    sum += "9"

            #print(sum)
            grand_total += int(sum)
        print(grand_total)

if __name__ == "__main__":
    main()
