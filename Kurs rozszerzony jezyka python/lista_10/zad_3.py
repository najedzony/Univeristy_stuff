import pandas as pd
import matplotlib.pyplot as plt

"""
Zadałem sobie pytanie, jak na przestrzeni lat zmieniała się liczba ludzi z nadwagą. Znalazłem dane na tej stronie: https://ourworldindata.org/grapher/share-of-men-defined-as-overweight?tab=chart
Plik z danymi wrzucam również na skos razem z plikiem źródłowym. 
Wyniki zgadzają się z moimi przewidywaniami, czyli na przestrzeni ostatnich kilkudziesięciu lat liczba otyłych mężczyzn rósł. 
"""

overweight_men = pd.read_csv('plik.csv')

s = []
for i in overweight_men['Entity']:
    if i not in s:
        s.append(i)

country_cnt = len(s)
data = []
for i in range(1975, 2017):
    akt = overweight_men["Prevalence of overweight adults (males) - WHO (2019)"].where(overweight_men["Year"] == i).sum() / country_cnt
    data.append([i, akt])

df = pd.DataFrame(data, columns = ['Year', 'Percentage of overweighted men'])

df.plot(x = "Year", y = 'Percentage of overweighted men', title = 'Overweight problem')

plt.show()