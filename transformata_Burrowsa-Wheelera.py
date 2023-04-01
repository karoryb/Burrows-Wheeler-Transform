
slowo = 'lusia$'
ciag = list(slowo)
bwt = []

for i in range(len(ciag)):
    x = slowo[-1] + slowo[:-1]
    slowo = x
    bwt.append(x)
    

#alfabetycznie
sort = sorted(bwt)
print(sort)

'''
tabela = []
for i in range(len(ciag)):
    elem = sort[i]
    x = []
    for i in range(len(elem)):
        tabela.append(elem[i])

print('-----\n', tabela)
print(np.array(tabela))

'''

wynik = []
for i in range(len(ciag)):
    element = sort[i]
    ostatni = element[-1]
    wynik.append(ostatni)
print("".join(wynik))
# print(wynik)




'''
def konwert_lancucha(lancuch):
    ciag = []
    for i in range(0, len(lancuch)):
        ciag.append(lancuch[i])
    return ciag

slowo= 'lusia$'
print(konwert_lancucha(slowo))

def przesuniecia(ciag):
    macierz = [ciag] 
    for i in range(0, len(ciag)-1):
        ciag.insert(0, ciag[len(ciag)-1])
        ciag.pop(len(ciag)-1)
        macierz.append(ciag)
        print('tu', macierz)
    return macierz

print(przesuniecia(konwert_lancucha(slowo)))

print("-----------------------------")
macierz = [] 

macierz.append(przesuniecia(konwert_lancucha(slowo)))

print(macierz)


'''

