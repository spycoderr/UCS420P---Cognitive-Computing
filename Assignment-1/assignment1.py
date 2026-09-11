# Assignment-1, Cognitive Computing UCS420
# Nilabh Kishore Gupta

# Q1.1 WAP to print your name three times.
name = input("enter your name: ")
for i in range(3):
    print(name)

# Q2.1 WAP to add three numbers and print the result.
a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))
print("sum =", a + b + c)

# Q2.2 WAP to concatenate three strings and print the result.
s1 = input("string1: ")
s2 = input("string2: ")
s3 = input("string3: ")
print("result =", s1 + s2 + s3)

# Q4.1 WAP to print the table of 7 and 9.
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)
print()
for i in range(1, 11):
    print(9, "x", i, "=", 9 * i)

# Q4.2 WAP to print the table of n, where n is given by the user.
n = int(input("\nn for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Q4.3 WAP to add all the numbers from 1 to n, where n is given by the user.
n = int(input("\nn: "))
total = 0
for i in range(1, n + 1):
    total += i
print("sum =", total)

# Q5.1 WAP to find maximum among three numbers using max() function.
a = int(input("\nnum1: "))
b = int(input("num2: "))
c = int(input("num3: "))
print("max =", max(a, b, c))

# Q5.2 WAP to add all numbers divisible by 7 and 9 from 1 to n.
n = int(input("\nn: "))
total = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        total += i
print("sum =", total)

# Q5.3 WAP to add all prime numbers from 1 to n.
n = int(input("\nn: "))
total = 0
for num in range(2, n + 1):
    prime = True
    for d in range(2, num):
        if num % d == 0:
            prime = False
            break
    if prime:
        total += num
print("sum of primes =", total)

# Q6.1 WAP using a function that adds all odd numbers from 1 to n.
def sum_odd(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
    return s

n = int(input("\nn: "))
print("sum of odds =", sum_odd(n))

# Q6.2 WAP using a function that adds all prime numbers from 1 to n.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    s = 0
    for i in range(1, n + 1):
        if is_prime(i):
            s += i
    return s

n = int(input("\nn: "))
print("sum of primes =", sum_primes(n))
