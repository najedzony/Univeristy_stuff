import io

def kompresja(tekst):
    ans = []
    akt_cnt = 1
    akt_char = tekst[0]
    for i in range(1, len(tekst)):
        if akt_char == tekst[i]:
            akt_cnt = akt_cnt + 1
        else:
            ans.append((akt_cnt, akt_char))
            akt_char = tekst[i]
            akt_cnt = 1
    ans.append((akt_cnt, akt_char))
    return ans


def dekompresja(skom_tekst):
    ans = io.StringIO()
    for i, j in skom_tekst:
        ans.write(i * j)
    return ans.getvalue()

"""http://catdir.loc.gov/catdir/enhancements/fy0711/2006051179-s.html   <-  link, pod ktorym dostepny znajduje się tekst, na ktorym wykonywalem test"""
