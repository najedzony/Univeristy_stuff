import decimal as d


def vat_faktura(tab):
    ans = 0.0
    for i in tab:
        ans += i
    return ans * 0.23

def vat_paragon(tab):
    ans = 0.0
    for i in tab:
        ans += (i * 0.23)
    return ans

zakupy = [0.2, 0.5, 4.59, 6]

print(vat_faktura(zakupy))
print(vat_paragon(zakupy))
print(vat_faktura(zakupy) == vat_paragon(zakupy))

def fixed_vat_faktura(tab):
    ans = d.Decimal(0.0)
    for i in tab:
        ans += d.Decimal(i)
    return ans * d.Decimal(0.23)

def fixed_vat_paragon(tab):
    ans = d.Decimal(0.0)
    for i in tab:
        ans += (d.Decimal(i) * d.Decimal(0.23))
    return ans

print(fixed_vat_faktura(zakupy))
print(fixed_vat_paragon(zakupy))
print(fixed_vat_faktura(zakupy) == fixed_vat_paragon(zakupy))

"""
Okazuje sie, ze uzycie Decimal nic nie pomoglo i to wyrazenie nadal jest falszywe, jednak
blad jest sporo mniejszy.
"""

fixed_zakupy = ['0.2', '0.5', '4.59', '6']
print(fixed_vat_faktura(fixed_zakupy) == fixed_vat_paragon(fixed_zakupy))

"""
Jednak jak widac mozemy temu zaradzic, jesli jako elementy listy podamy stringi a nie floaty
"""

