size = int(input("Enter the size of the array: "))
elem = input("Enter the elements separated by space: ")

elem_lst = elem.split(" ")
if size != len(elem_lst):
    print("Too much elements nigga")
else:
    for em in elem_lst:
        print(int(em) ** 3)
