f=open("Öğrenci Sayıları.dat","r")
satirlar=f.readlines()
toplam=0

for i in range(1,len(satirlar)):
    if satirlar[i].find("\t")==-1:
        continue

    sutunlar = satirlar[i].split("\t")
    if not sutunlar[1].strip().isdigit():
        continue

    toplam+=int(sutunlar[1])

f.close()
print(toplam)