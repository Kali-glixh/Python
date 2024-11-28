def is_prime(n):
    if n <= 1:
        return False  
    elif n == 2:
        return True  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False 
    return True

def sum_primes(n):
    total = 0
    if n == 2:
        return total
    for num in range(2, n):
        prime = is_prime(num)
        if prime == True:
            total += num
    return total
    
