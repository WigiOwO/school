
def fibonacci(n):
    fiblist = [0, 1]
    if n == 1:
        return [fiblist[0]]
    elif n == 0:
        return []
    f0, f1 = fiblist[0], fiblist[1]
    for i in range(2, n):
        f = f1 + f0
        fiblist.append(f)
        f0 = f1
        f1 = f

    return fiblist
