integers = open("integers.txt", "r")
even = open("double.txt", "w")
odd = open("triple.txt", "w")
for line in integers.readlines():
    num = int(line)
    if num % 2 == 0:
        even.write(f"{str(num*num)}\n")
    else:
        odd.write(f"{str(num**3)}\n")
even.close()
odd.close() 
integers.close()