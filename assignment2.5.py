# task the user to enter a number over 100 and then enter a number under 10 and then tell how many times the smaller number goes into the larger number in a user-friendly format.
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

for i in range(10):
    number = input("Choose number #%s : " % i)
    if is_prime(int(number)):
        print("%s is prime" % number)
    else:
        print("%s is not prime" % number)