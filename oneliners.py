# Fixed point binary to decimal (or normal binary)
bin_num = "0101"
print(sum([val for pos, val in enumerate([2 ** j for j in range(len(bin_num.split(".")[0]) - 1, (len(bin_num.split(".")[0]) - len(bin_num.replace(".", ""))) - 1, -1)]) if bin_num.replace(".", "")[pos] == "1"]))

# Mode average
arr = [1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 3, 4, 5, 5, 6, 5, 5, 5]
print([i[0] for i in list(filter(lambda x: x if x[1] == sorted({k: v for k, v in [(i, arr.count(i)) for i in set(arr)]}.items(), key=lambda x: x[1], reverse=True)[0][1] else 0, sorted({k: v for k, v in [(i, arr.count(i)) for i in set(arr)]}.items(), key=lambda x: x[1], reverse=True)))])

# Mean average
arr = [1, 3, 5, 6, 7]
print(sum(arr) / len(arr))

# Median average
arr = [1, 2, 3, 4, 5]
print(sorted(arr)[(len(arr) // 2) - 1: (len(arr) // 2) + 1] if len(arr) % 2 == 0 else sorted(arr)[len(arr) // 2])

# Factorial
fact = lambda y: f"{y}! = {eval('*'.join([str(i) for i in range(y, 0, -1)])) if y > 0 else 1}"
print(fact(5))

# Factors
facrors = lambda y: [l[0] for l in [[(i, j) for j in range(1, y + 1) if i * j == y and i < j] for i in range(1, y + 1) if y % i == 0] if l]
print(facrors(326))

# Quadratic Solutions
import math
solutions = [(((-j[1]) + math.sqrt(j[1] ** 2 - (4 * j[0] * j[2]))) / (2 * j[0]), ((-j[1]) - math.sqrt(j[1] ** 2 - (4 * j[0] * j[2]))) / (2 * j[0])) for j in [[int(input(f"Enter {i}")) for i in ["ax^2", "bx", "c"]], ]][0]
print(solutions)

# Prime numbers
import itertools
primes = list(itertools.chain.from_iterable(filter(lambda y: len(y) == 1, [[k for k in range(1, i + 1) if i / k == i // k and k != 1] for i in [j for j in range(1, int(input("Enter number: ")) + 1)]])))
print(primes)

