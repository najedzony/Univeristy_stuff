def sqrt(k):
    i = 1
    akt = 0
    while akt < k:
        akt += 2 * i - 1
        i += 1
    if akt == k:
        return i - 1
    else:
        return i - 2


for i in range(1, 37):
    print("Podłoga z pierwiastka z {0} = {1}".format(i, sqrt(i)))