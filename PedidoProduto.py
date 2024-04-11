#Terminar de incluir: Função de compra(Verificar quantidade, apresentar preço)
p1 = {"nome": "manteiga", "cod": 1289, "qtd": 413, "preco": 6.99}
p2 = {"nome": "requeijao", "cod": 4189, "qtd": 30, "preco": 6.99}
p3 = {"nome": "nescau", "cod": 1389, "qtd": 100, "preco": 6.99}
p4 = {"nome": "queijo 300g", "cod": 76589, "qtd": 43, "preco": 14.98}

def Cod(x):
    return x["cod"];

p = 0

lP = [p1, p2, p3, p4]

cod = int(input("Código do produto\n"))
if cod == 0:
    print("Adeus")
else:
    cont=0
    for i in lP:
        if cod == Cod(i):
            cont+=1
            p = i
            
    if cont == 1:
        print(f'Produto: {p["nome"]}, código: {p["cod"]}, quantidade em estoque: {p["qtd"]}, preço: {p["preco"]}')
    else:
        while cont!=1:
            print("Erro, código indisponível")
            cod = int(input("Código do produto\n"))
            for i in lP:
                if cod == Cod(i):
                    p = i
                    cont+=1
        print(f'Produto: {p["nome"]}, código: {p["cod"]}, quantidade em estoque: {p["qtd"]}, preço: {p["preco"]}')
