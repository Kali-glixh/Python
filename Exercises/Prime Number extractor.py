def is_prime(my_list):
    """Checks whether a number is prime

    elem (int): any numberç

    Output (bool): True if the number is prime
    """
    count = 0
    for i in range(2, elem):
        if elem % i == 0:
            return False
    return True

def prime_extractor(my_list):
    """The algorithm extract the prime numbers os a given list
    my_list (list): a sequence of numbers
    Output ()
    """
    result = []
    for number in my_list:
        if  True:
            result.append(number)
    return result
