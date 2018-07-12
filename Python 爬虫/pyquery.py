from pyquery import PyQuery as pq

doc = pq(filename='example.html')
print(doc.html())
print(doc('.item-1'))
data = doc('tr')

for tr in data.items():
    temp = tr('td').eq(2).text()
    print(temp)