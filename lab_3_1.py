with open("mylife.txt", "a") as f:
    while True:
        f.write(f"{input("Enter line: ")}\n")
        ask = input("Are there more lines y/n? ")
        if ask.lower() == "y":
            continue
        else:
            break
