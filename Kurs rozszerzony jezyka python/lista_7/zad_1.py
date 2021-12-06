import requests
import re 
import threading


adres = '([a-zA-Z]+.)*[a-zA-Z]+'
automat_https = re.compile('https?://'+ adres)

url = 'https://skos.ii.uni.wroc.pl/course/view.php?id=406'

was_already = set()
ans = []
lock1 = threading.Lock()


def crawl(start_page, text, distance, action):
    ans.append((start_page, action(text)))
    lista = []
    if distance > 1:
        for i in [url.group() for url in automat_https.finditer(text)]:
            lock1.acquire()
            if i not in was_already:
                was_already.add(i)
                lock1.release()
                try:
                    req = requests.get(i, 'html.parser')
                    text = req.text
                    t = threading.Thread(target = crawl, args=(i, text, distance - 1, action,))
                    lista.append(t)
                    t.start()
                except:
                    continue
            else:
                lock1.release()
    for i in lista:
        i.join()


def how_many_pythons(text):
    res = 0
    for sentence in text.split('.'):
        if 'python' in sentence.lower():
            res += 1
    return res

req = requests.get(url, 'html.parser')
text = req.text

crawl(url, text, 2, how_many_pythons)
print(ans)