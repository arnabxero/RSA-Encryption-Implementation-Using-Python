import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


p = int(input("Enter A Prime Number : "))
q = int(input("Enter Another Prime Number : "))

if not is_prime(p) or not is_prime(q):
    raise ValueError('P or Q were not prime')

x = int(input("Enter Lower Range of Public Key : "))

eq = (p - 1) * (q - 1) + 1

y = 1
xy = x*y

while xy != eq:
    x += 1
    y = eq // x
    xy = x*y


print ("public key, x: " + str(x))
print ("private key, y: " + str(y))
print ("modulo (pq): " + str(p*q))

input()

