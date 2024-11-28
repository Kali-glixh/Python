import math

def prime(num):
    
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  
        if num % i == 0:
            return False
    return True

def prime_range():
    primes = []
    for num in range(10000, 10051): 
        if prime(num):  
            primes.append(str(num))  
    print(", ".join(primes))  

prime_range()
