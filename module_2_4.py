# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = list(range(1, 16))
primes = []
not_primes = []

for i in numbers:
    num_of_div = 0
    for j in numbers:
        if i % j == 0:
            num_of_div = num_of_div + 1
    if num_of_div < 2:
        continue
    elif num_of_div == 2:
        primes.append(i)
    else:
        not_primes.append(i)

print("Primes: ", primes)
print("Not Primes: ", not_primes)