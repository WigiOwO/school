side = int(input("Enter the side length of the square: "))

for i in range(1, side+1):
    for j in range(1, side+1):
        if i == 1 or i == side or j == 1 or j == side:
            print("x", end="")
        else:
            print(" ", end='')
    print()