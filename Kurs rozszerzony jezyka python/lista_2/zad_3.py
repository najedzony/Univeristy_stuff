import sys

sys.setrecursionlimit(1000000)  
"""Musiałem zwiększyć limit rekursji, bo inaczej nawet wersja ze spamiętywaniem nie działała dla większych danych"""


def sudan(n, x, y):
    if n == 0:
        return x + y
    if y == 0:
        return x
    return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)


mem = {}
def memoize_sudan(n, x, y):
    if (n, x, y) not in mem:
        if n == 0:
            mem[(n, x, y)] =  x + y
        elif y == 0:
            mem[(n, x, y)] = x
        else:
            mem[(n, x, y)] = memoize_sudan(n - 1, memoize_sudan(n, x, y - 1), memoize_sudan(n, x, y - 1) + y)
    return mem[(n, x, y)]


print(len(str(memoize_sudan(2, 1, 3))))

"""
Jeśli chodzi o wnioski to podzieliłem je dla n = 1 i dla n = 2.
Dla n = 1:
Wersja bez spamiętywania mieli się dosyć długo już dla x = 1 i y = 25.
Wersja zaś ze spamiętywaniem nawet dla x = 10000 i y = 10000 działa bardzo szybko.
Dla n = 2:
Dla wersji bez spamiętywania nie opłaca się nawet tego odpalać. Działa dla x = 1 i y = 2, ale dalej już nie.
Dla wersji ze spamiętywaniem nie ma większej poprawy ale działa dla x = 1 i y = 3. Warto dodać, że wynik
funkcji dla tych danych jest rzędu 10 ** 3084. 
"""