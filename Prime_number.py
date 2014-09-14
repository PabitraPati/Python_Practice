# Find all the prime numbers within 1000
# Checks if the given number is a prime number or not

def is_prime(number):
    number = int(number)
    # Collect all the numbes those are not prime
    noprimes = [i for i in range(3, 1000) for j in range(2, i) if i % j == 0]
    # Now make the inverse of the list of all non-prime numbers
    primes = [x for x in range(2, 1000) if x not in noprimes]
    # Sort the list to determine the position
    primes.sort()
    # Check if the number is in prime number list or not
    if number in primes:
        position = primes.index(number) + 1
        print "Yes, your number %d is the (%d)th prime number in the list of prime numbers within 1000." % (number, position)
    else:
        print "No, your number %d is not a prime number." %(number)


is_prime(raw_input("Enter a number to check if its prime or not ?"))
