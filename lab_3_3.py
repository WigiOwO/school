text = open("gwa.txt", "r")
highest = 0
names = ['placeholder']
for line in text.readlines():
    poop = line.strip().split(",")
    gwa = int(poop[1].strip())
    if gwa > highest:
        highest = gwa
        names.pop()
        names.append(line.strip())
print(names[0])