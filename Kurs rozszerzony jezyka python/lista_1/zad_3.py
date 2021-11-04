def tabliczka(x1, x2, y1, y2):
    print(end = ' ')
    wyrownanie = len(str(x2 * y2))
    wyrownanie_pion = len(str(y2))
    print(wyrownanie_pion * ' ', end = '')
    for i in range(x1, x2 + 1):
        print((wyrownanie - len(str(i)) + 1) * ' ', i, end = '', sep = '')
    print()
    for i in range(y1, y2 + 1):
        print((wyrownanie_pion - len(str(i)) + 1) * ' ', i, end = '', sep = '')
        for j in range(x1, x2 + 1):
            print((wyrownanie - len(str(i * j)) + 1) * ' ', i * j,  end = '', sep = '')
        print()



tabliczka(3, 5, 2, 4)
print()
tabliczka(1, 10, 1, 10)
print()
tabliczka(1, 10, 1, 100)
