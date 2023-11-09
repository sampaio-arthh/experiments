import random


arq = open("txt.txt", 'a')

def writer(writes, tot):
    if writes == 0:
        num = (random.random()+random.randint(0,9))
        tot+=num
        arq.write(str(num))
        arq.close()
        return tot/500
        
    else:
        num = (random.random()+random.randint(0,9))
        tot += num
        arq.write(str(num))
        arq.write(" ")
        writes-=1
        writer(writes, tot)

tot = 0
med = writer(500, 0)

#####

arqR = open("txt.txt", "r")

def forR(i, val):
    if i <= len(arqR.read()):
        if arqR.read()[i] == " ":
            lista = [i, val]
            return lista
    else:
        i+=1
        val += arqR.read()[i]

def reader(read):
    if read == len(arqR.read()):
        return val
    else:
        lista = forR(read, "")
        next_pos = lista[0] + 1
        val = float(lista[1])
        if read ==0:
            dif = val
        elif (med - val) < dif:
            dif = val
        read = next_pos

reader(0)