#Faça um programa que gere numeros aleatorios em um txt e tire a media entre eles
#utilizando recursao

import random #importando biblioteca

arq = open("txt.txt", 'w') #definindo arquivo e premissões

def writer(writes, tot=0): #arg: quantos numeros no total
    #recursao parte do 500 rumo ao 0
    if writes == 1:
        num = (random.random()+random.randint(0,9))
        tot+=num
        arq.write(str(num))
        arq.close()
        print (tot/qtd)
        
    else:
        num = (random.random()+random.randint(0,9))
        tot += num
        arq.write(str(num))
        arq.write(" ")
        writes-=1
        writer(writes,tot)


qtd = 5

writer(qtd)