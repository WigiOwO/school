from math import sqrt
num = float(input("Enter a number: "))

verdict = ""

num_sqrt = sqrt(num)

primes = [2, 3, 5]

# Loop to check prime numbers
# from 2 to the square root of the
# given number
for i in range(2, int(num_sqrt)):
    # If the number is prime, its added to
    # primes list
    if i % 2 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        primes.append(i)


# Final prime check, if the number
# is divisible to its prime
# automatically verdicts its not prime
# and ends the loop
for prime in primes:
    if num % prime == 0:
        verdict = "Not Prime"
        break
    else:
        verdict = "Prime"

# Prints if the number is prime or not
print(verdict)