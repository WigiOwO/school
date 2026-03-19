def calculate_stats(numbers:list):
    info = {}
    info['count'] = len(numbers)
    sum = 0
    for i in numbers:
        sum += i
    info['sum'] = sum
    info['average'] = sum/len(numbers)
    numbers.sort()
    info['max'] = numbers[-1]
    info['min'] = numbers[0]
    return info


