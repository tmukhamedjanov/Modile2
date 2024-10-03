numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)) :
    if numbers[i] == 1 :
        continue
    is_prime = True
    for j in range(i + 1) :
        if j > 1 :
            if numbers[i] % j == 0 :
                is_prime = False
                break
    if not is_prime :
        not_primes.extend([numbers[i]])
    else :
        primes.extend([numbers[i]])
print(primes)
print(not_primes)
