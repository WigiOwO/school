from math import sqrt
num = float(input("Enter a number: "))

verdict = ""

num_sqrt = sqrt(num)

primes = [2, 3, 5]

for i in range(2, int(num_sqrt)):
    if i % 2 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        primes.append(i)

for prime in primes:
    if num % prime == 0:
        verdict = "Not Prime"
        break
    else:
        verdict = "Prime"

print(verdict)