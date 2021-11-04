from timeit import timeit

def imperatywne_doskonale(n):
    ans = []
    for i in range(2, n):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            ans.append(i)
    return ans


print(imperatywne_doskonale(1000))


def listy_skladane_doskonale(n):
    return [x for x in range(2, n + 1) if sum([y for y in range(1, x) if x % y == 0]) == x]


print(listy_skladane_doskonale(1000))

def funkcyjne_doskonale(n):
    return list(filter(lambda x: sum(y for y in range(1, x) if x % y == 0) == x, (x for x in range(1, n))))

print(funkcyjne_doskonale(1000))


n = 10000

print("Czas dla imperatywnego rozwiązania:", timeit('imperatywne_doskonale(n)', globals = globals(), number = 1))
print("Czas przy użyciu list składanych:", timeit('listy_skladane_doskonale(n)', globals = globals(), number = 1))
print("Czas dla rozwiązania funkcyjnego:", timeit('funkcyjne_doskonale(n)', globals = globals(), number = 1))