class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Prod:
    def __init__(self, code, nome, qtd, preco):
        self.code = code
        self.nome = nome
        self.qtd = qtd
        self.preco = preco

p1 = Prod(2134,"manteiga", 50, 8.99)
p2 = Prod(1289,"nescau", 16, 11.99)
p3 = Prod(1241,"leite", 120, 4.59)
p4 = Prod(42389,"requeijao", 18, 9.99)

lProd = [p1, p2, p3, p4]

cod = int(input("Código do produto]"))
if cod == 0:
    print("Adeus")
else:
    for i in range(0, len(lProd)):
        if cod not in ((lProd[i]).code)
            print("Erro, código não listado")

            while (cod not in prod_preco) and (cod!=0):

                cod = int(input("Código de produto: "))
                if cod not in prod_preco:
                    print("Erro, código não listado")
        
        qtd = int(input(f"Quantidade do produto código = [{cod}]"))
        if qtd <= prod_qtd[cod]:
            print(f"Preço = {qtd*prod_preco[cod]:.2f}")
            prod_qtd[cod] -= qtd
        else:
            print(f"Erro, quantidade solicitada maior que quantidade em estoque, só temos {prod_qtd[cod]}")


prod_nm = {2134: "manteiga", 1289: "nescau", 1241: "leite", 42389: "requeijao"}
prod_qtd = {2134: 50, 1289: 16, 1241: 120, 42389: 6}
prod_preco = {2134: 10.89, 1289: 11.64, 1241: 4.80, 42389: 8.79}

cod = 90909090909090

while (cod!=0):
    cod = int(input("Código de produto: "))
    if cod != 0:

        if cod not in prod_preco:
            print("Erro, código não listado")

            while (cod not in prod_preco) and (cod!=0):

                cod = int(input("Código de produto: "))
                if cod not in prod_preco:
                    print("Erro, código não listado")
        
        qtd = int(input(f"Quantidade do produto código = [{cod}]"))
        if qtd <= prod_qtd[cod]:
            print(f"Preço = {qtd*prod_preco[cod]:.2f}")
            prod_qtd[cod] -= qtd
        else:
            print(f"Erro, quantidade solicitada maior que quantidade em estoque, só temos {prod_qtd[cod]}")