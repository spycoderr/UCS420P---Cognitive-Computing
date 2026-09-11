# Assignment-2, Cognitive Computing UCS420
# List, Tuple, Set, Dictionary
# Nilabh Kishore Gupta

import random

# Q1. Create a List L = [10,20,30,40,50,60,70,80]
# i. add 200 and 300  ii. remove 10 and 30  iii. sort ascending  iv. sort descending
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
print("added 200,300 ->", L)

L.remove(10)
L.remove(30)
print("removed 10,30 ->", L)

L.sort()
print("ascending ->", L)

L.sort(reverse=True)
print("descending ->", L)

# Q2. tuple scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
# i. highest score and its index  ii. lowest score and its count
# iii. reverse tuple as list  iv. check if user given score is present
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
top = max(scores)
print("\nhighest =", top, "index =", scores.index(top))

low = min(scores)
print("lowest =", low, "count =", scores.count(low))

print("reversed list ->", list(scores[::-1]))

check = float(input("check score: "))
if check in scores:
    print("found at index", scores.index(check))
else:
    print("not present")

# Q3. list of 100 random numbers between 100 and 900, count odd, even, prime numbers
nums = [random.randint(100, 900) for i in range(100)]
odd_cnt = even_cnt = prime_cnt = 0

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True

for n in nums:
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
    if is_prime(n):
        prime_cnt += 1

print("\nodd:", odd_cnt, " even:", even_cnt, " prime:", prime_cnt)

# Q4. sets A = {34,56,78,90}, B = {78,45,90,23}
# union, intersection, symmetric difference, subset/superset check, remove X from A
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print("\nunion:", A | B)
print("intersection:", A & B)
print("symmetric diff:", A ^ B)
print("A subset of B:", A.issubset(B))
print("B superset of A:", B.issuperset(A))

X = int(input("remove from A: "))
if X in A:
    A.remove(X)
    print("removed, A =", A)
else:
    print("not in A")

# Q5. rename key 'city' to 'location' in the given dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
sample_dict["location"] = sample_dict.pop("city")
print("\n", sample_dict)
