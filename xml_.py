#http://www.diveintopython3.net/xml.html


import xml.etree.ElementTree as etree



def aligncode(code):
    p = code.strip().split(".")
    while len(p)<5:
        p.append(0)
    return(p)


tree = etree.parse('okof.xml')
root = tree.getroot()
print(root[2].text)
okof2014_root = root[2][0]
okof1994_root = root[2][0]
okof2014ex_root = None







for c in okof2014_root:
    print(c.tag)
    print("*"*40)
    for k,v in c.items():
        print(k,' ',v)
        if v=='Исключен из ОКОФ':
            okof2014ex_root=c

for c in okof2014ex_root:
    l = list(c.items())
    if len(l):
        code = aligncode(l[0][1])
        print(code)
