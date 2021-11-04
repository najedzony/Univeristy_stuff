import random as rd

"""
Jako pierwszy argument funkcji podajemy ile eksperymentow mamy wykonac, a jako
drugi podajemy ile reszek lub orlow ma wypasc pod rzad, aby zakonczyc pojedynczy eksperyment.
"""

def eksperyment(cnt, oczekiwana_ilosc):
    ans = 0
    for x in range (0, cnt):
        ost = -1
        il_pod_rzad = 0
        coin = 0
        while il_pod_rzad < oczekiwana_ilosc:
            coin = rd.randint(0, 1)
            if coin == ost:
                il_pod_rzad = il_pod_rzad + 1
            else:
                ost = coin
                il_pod_rzad = 1
            ans = ans + 1
    return ans / cnt

print(eksperyment(10, 5))
