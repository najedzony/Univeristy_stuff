# Wykonałem wariant c) zadania 1, czyli obliczanie pochodnej dla funkcji z jedną zmienną

class Wyrazenie: 
    
    def __init__(self, l, r):
        self.l = l
        self.r = r
    
    def __add__(self, arg):
        return Dodaj(self, arg)

    def __mul__(self, arg):
        return Razy(self, arg)
    
    def oblicz(self, zmienne):
        res = str(self)
        for i, j in zmienne:
            res = res.replace(i, str(j))
        
        try:
            return eval(res)
        except ZeroDivisionError:
            print("Nie można dzielić przez 0!!!")
            return None
        except NameError:
            print("Nie wszystkie zmienne mają przypisane wartości!!!")
            return None  
    

class Stala(Wyrazenie):

    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)

    @staticmethod
    def Pochodna(wyr):
        return Stala(0)


class Zmienna(Wyrazenie):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @staticmethod
    def Pochodna(wyr):
        return Stala(1)


class Dodaj(Wyrazenie):
     
     def __str__(self):
         return '(' + str(self.l) + ' + ' + str(self.r) + ')'

     @staticmethod
     def Pochodna(wyr):
         return Dodaj(wyr.l.Pochodna(wyr.l), wyr.r.Pochodna(wyr.r))

class Razy(Wyrazenie):
    
    def __str__(self):
        return '(' + str(self.l) + ' * ' + str(self.r) + ')'
    
    @staticmethod
    def Pochodna(wyr):
        return Dodaj(Razy(wyr.l.Pochodna(wyr.l), wyr.r), Razy(wyr.l, wyr.r.Pochodna(wyr.r)))

class Odejmowanie(Wyrazenie):

    def __str__(self):
        return '(' + str(self.l) + ' - ' + str(self.r) + ')'
    
    @staticmethod
    def Pochodna(wyr):
        return Odejmowanie(wyr.l.Pochodna(wyr.l), wyr.r.Pochodna(wyr.r))

class Dzielenie(Wyrazenie):

    def __str__(self):
        return '(' + str(self.l) + ' // ' + str(self.r) + ')' 

    @staticmethod
    def Pochodna(wyr):
        return Dzielenie(Odejmowanie(Razy(wyr.r.Pochodna(wyr.r), wyr.l), Razy(wyr.l, wyr.r.Pochodna(wyr.r))), Razy(wyr.r, wyr.r))

#testy:

print("Stworzenie prostych wyrażeń korzystających z jednej zmiennej oraz jednej stałej:")
print("Dodawanie:", Dodaj(Zmienna('x'), Stala(2)))  # x + 2
print("Odejmowanie:", Odejmowanie(Zmienna('x'), Stala(2))) # x - 2
print("Mnożenie:", Razy(Zmienna('x'), Stala(2))) # x * 2
print("Dzielenie:", Dzielenie(Zmienna('x'), Stala(2))) # x // 2
print()

print("Przykłady zagnieżdżonych wyrażeń:")
print(Dodaj(Zmienna('x'), Odejmowanie(Zmienna('y'), Stala(3)))) # x + (y - 3)
print(Razy(Dodaj(Zmienna('x'), Zmienna('y')), Odejmowanie(Stala(2), Zmienna('z')))) # (x + y) * (2 - z)
print()

print("Przykład użycia operatora + i * do obiektów klasy Wyrażenie:")
test1 = Dodaj(Zmienna('x'), Stala(3)) # x + 3
test2 = Odejmowanie(Zmienna('y'), Stala(4)) # y - 4
print("Dodawanie:", test1 + test2) # (x + 3) + (y - 4)
print("Mnozenie:", test1 * test2) # (x + 3) * (y - 4)
print()

print("Przykład obliczania wyrażeń dla x = 1 i y = 2:")
wartosciowanie = [('x', 1), ('y', 2)]  # x = 1 and y = 2
test1 = Dodaj(Zmienna('x'), Zmienna('y')) # x + y
print(test1, '=', test1.oblicz(wartosciowanie)) 
test1 = Dodaj(Zmienna('x'), Odejmowanie('y', 10)) # x + (y - 10)
print(test1, '=', test1.oblicz(wartosciowanie))
test1 = Razy(Zmienna('y'), Dodaj(Zmienna('x'), Stala(3)))
print(test1, '=', test1.oblicz(wartosciowanie)) # y * (x + 3)
print()

print("Przykłady użycia wyjątków:")
print("Dzielenie przez 0:", Dzielenie(Zmienna('x'), Stala(0)).oblicz([('x', 2)]))
print("Brak przypisania wartości do zmiennej:", Dodaj(Zmienna('x'), Stala(2)).oblicz([]))
print()

"""
Warto tutaj zaznaczyć, że jak widać w powyższym przykładzie, dopuszczam istnienie obiektu klasy dzielenie, ktory reprezentuje działanie
x / 0, a wyjątek zgłaszam dopiero przy próbie obliczania wartości. Jest to moja świadoma decyzja.
"""

print("Obliczanie pochodnej:")
test = Dodaj(Zmienna('x'), Stala(3))
print('{0}` = {1}'.format(test, test.Pochodna(test)))
test = Razy(Dodaj(Zmienna('x'), Stala(2)), Odejmowanie(Zmienna('x'), Stala(4)))
print('{0}` = {1}'.format(test, test.Pochodna(test)))

# (x + 2) * (x - 4)` = ((1 + 0) * (x - 4)) + ((x + 2) * (1 - 0)) = x - 4 + x + 2 = 2x - 2
# (x + 2) * (x - 4)` = (x**2 - 4x + 2x - 8)` = (x**2 - 2x - 8)` = 2x - 2

"""
Zdaję sobie sprawę, że wypisywanie mojej funkcji liczącej pochodną nie jest najpiękniejsze, jednak formatowaniem wyniku miały zająć się
osoby robiące podpunkt b), dlatego nie dbałem o to, aby ładnie to wyglądało, tylko aby dawało dobry wynik. A wynik jest prawidłowy.
"""