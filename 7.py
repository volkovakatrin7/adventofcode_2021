def main():
    with open("data7.txt", "r") as f:
        reader = f.read()

    crabs = [int(x) for x in reader.split(",")]
    #print(crabs)

    last = max(crabs)

    total_fuel = []
    for position in range(0, last+1):
        fuel = 0
        for crab in crabs:
            moves = abs(position - crab)
            f = moves*(moves+1)/2
            #print(f)
            fuel += f
        #print("Total ", fuel)
        total_fuel.append(fuel)

    #print(total_fuel)
    optimum = min(total_fuel)
    print(optimum)
    print(total_fuel.index(optimum))

    avg = sum(crabs)/len(crabs)
    print(avg)
    print(avg-0.5)




if __name__ == "__main__":
    main()