tables = [[[{57: True}, {26: False}, {21: True}, {56: True}, {70: False}],
[{38: False}, {48: False}, {78: True}, {40: True}, {54: False}],
[{15: True}, {61: True}, {32: True}, {33: True}, {1: False}],
[{16: False}, {9: False}, {65: True}, {42: False}, {79: True}],
[{43: True}, {94: False}, {39: True}, {12: False}, {67: False}]],

[[{57: True}, {26: False}, {21: True}, {56: True}, {70: False}],
[{38: False}, {48: False}, {78: True}, {40: True}, {54: False}],
[{15: True}, {61: True}, {32: True}, {33: True}, {1: False}],
[{16: False}, {9: False}, {65: True}, {42: False}, {79: True}],
[{43: True}, {94: False}, {39: True}, {12: False}, {67: False}]]]

for i in range(len(tables)):
    tables[i] = [[{-1: False}] * 5] * 5

for table in tables:
    for row in table:
        print(row)
    print("\n")