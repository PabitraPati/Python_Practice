'''
Checks if the given number is a prime number or not

Works for both Python 2.7 and Python 3.4

author - Pabitra Kumar Pati
'''

def is_prime():
    '''
    Checks if the given number is prime or not
    If the number is prime, then says at what position the number lies in the list of prime numbers within 1000
    '''

    number = int(input("Enter a number to check if its prime or not ? "))
    # Collect all the numbes those are not prime
    noprimes = [i for i in range(3, 1000) for j in range(2, i) if i % j == 0]
    # Now make the inverse of the list of all non-prime numbers
    primes = [x for x in range(2, 1000) if x not in noprimes]
    # Sort the list to determine the position
    primes.sort()
    # Check if the number is in prime number list or not
    if number in primes:
        position = primes.index(number) + 1
        print ("Yes, your number %d is the (%d)th prime number in the list of prime numbers within 1000." % (number, position))
    else:
        print ("No, your number %d is not a prime number." %(number))


is_prime()
