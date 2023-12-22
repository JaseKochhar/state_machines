# Author: Rohit Singh

if __name__== "__main__":
    state = 0
    while True:
        XY = input("Enter XY: ")
        if XY not in ["00", "10", "01", "11"]:
            print("Value must be either 00, 01, 10, 11")
            continue
        x = int(XY[0]) == 1
        y = int(XY[1]) == 1
        state = (state + ((not x) + (not y))) % 4
        print("N =", state)

