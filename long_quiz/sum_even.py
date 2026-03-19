def sum_even_numbers(n:list):
    sums = 0
    for i in n:
        if i % 2 == 0:
            sums += i
    return sums