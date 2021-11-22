"""
Główna funkcja rozwiązująca problem z zadania.
"""

def reconstruction(n, v2, v1):
    res = []
    for i in range(n):
        res.append([])
    for i in range(n):
        for j in range(n):
            res[i].append('.')
    v2_set = set()
    v2_pom = set()
    v1_list = []
    for i in range(n):
        v1_list.append([v1[i], i])
        v2_set.add((v2[i], i))
    v1_list.sort()
    v1_list.reverse()

    for i in range(n):
        for a, b in v2_set:
            if v1_list[i][0] != 0 and a != 0:
                res[v1_list[i][1]][b] = 'X'
                v2_pom.add((a-1, b))
                v1_list[i][0] -= 1
            else:
                v2_pom.add((a, b))
        v2_set.clear()
        for a, b in v2_pom:
            v2_set.add((a,b))
        v2_pom.clear()

    return res


"""
Funckja wypisująca rozwiązanie. 
"""
def wypisz(l):
    for i in range(len(l)):
        for j in range(len(l)):
            print(l[i][j], end = ' ')
        print()

"""
Funckja sprawdzająca czy rozwiązanie jest poprawne. Korzystałem z niej głównie do testowania.
"""

def check(l, v1, v2):
    for i in range(len(l)):
        pom = 0
        for j in range(len(l)):
            if l[i][j] == 'X':
                pom += 1
        if pom != v2[i]:
            return 0
    
    for j in range(len(l)):
        pom = 0
        for i in range(len(l)):
            if l[i][j] == 'X':
                pom += 1
        if pom != v1[j]:
            return 0
    return 1



n = 4

h = (2, 1, 3, 1)
v = (1, 3, 1, 2)

ans = reconstruction(n, h, v)
wypisz(ans)
print(check(ans, h, v))


"""
X oznacza czarne pole, kropka zaś oznacza białe.
"""

"""
W moim rozwiązaniu korzystam z tego, że sortuję najpierw wiersze, aby najpierw obsługiwać te, które potrzebują najwięcej zakolorowanych
kwadratów, a na koniec te które najmniej. Potem dla każdego wiersza dopóki trzeba tam coś jeszcze zakolorować, koloruje w kolumnach, które aktualnie
mają najwięcej do pokolorowania, aż do tych, które mają najmniej. Wiersze trzymam w liście, a kolumny w secie. Po przejściu całego wiersza
uaktualniam wartości w kolumnach i przechodzę do następnego.
"""