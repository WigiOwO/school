numbers = open("number.txt", "r")
even = open("even.txt", "w")
odd = open("odd.txt", "w")
for line in numbers.readlines():
    num = int(line)
    if num % 2 == 0:
        even.write(f"{str(num)}\n")
    else:
        odd.write(f"{str(num)}\n")
even.close()
odd.close() 
numbers.close()