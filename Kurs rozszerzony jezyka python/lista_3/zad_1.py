from timeit import timeit
from math import sqrt

def imperatywne_pierwsze(n):
    ans = []
    for i in range(2, n + 1):
        it = 2
        is_prime = 1
        while(it * it <= i):
            if i % it == 0:
                is_prime = 0
            it += 1
        if is_prime == 1:
            ans.append(i)
    return ans

print(imperatywne_pierwsze(20))

def listy_skladane_pierwsze(n):
    return [x for x in range(2, n + 1) if len([m for m in range(2, int(sqrt(x)+1)) if x % m == 0]) == 0]

print(listy_skladane_pierwsze(20))


def funkcyjne_pierwsze(n):
    return list(filter(lambda x: sum(y for y in range(2, int(sqrt(x)+1)) if x % y == 0) == 0, (x for x in range(2, n))))

print(funkcyjne_pierwsze(20))


n = 100000

print("Czas dla imperatywnego rozwiązania:", timeit('imperatywne_pierwsze(n)', globals = globals(), number = 1))
print("Czas przy użyciu list składanych:", timeit('listy_skladane_pierwsze(n)', globals = globals(), number = 1))
print("Czas dla rozwiązania funkcyjnego:", timeit('funkcyjne_pierwsze(n)', globals = globals(), number = 1))
