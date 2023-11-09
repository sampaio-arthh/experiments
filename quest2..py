#produto = {código, nome, preço, quantidade}

#prod_qtd = {(prod_cod: prod_qtd)}
#prod_preco = {(prod_cod: prod_preco)}

prod_nm = {2134: "manteiga", 1289: "nescau", 1241: "leite", 42389: "requeijao"}
prod_qtd = {2134: 50, 1289: 16, 1241: 120, 42389: 6}
prod_preco = {2134: 10.89, 1289: 11.64, 1241: 4.80, 42389: 8.79}

cod = 90909090909090

while (cod!=0):
    cod = int(input("Código de produto: "))
    if cod != 0:

        if cod not in prod_preco:
            print("AAA Erro, código não listado")

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