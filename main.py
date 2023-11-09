verb = input("Verbo: ")
verb = verb.lower()

letra="n"

for i in range(len(verb)):
    if verb[len(verb)-2:] == "ar":
            pos = i
            letra = "a"

for i in range(len(verb)):
    if verb[len(verb)-2:] == "er":
            pos = i
            letra = "e"

for i in range(len(verb)):
    if verb[len(verb)-2:] == "ir":
            pos = i
            letra = "i"
print(verb[len(verb)-2:])
if letra == "n":
    print("Erro, tente novamente")

else:

    if letra == "a":
        print("Conjugação Presente I.")
        print(f"Eu {verb[:i-1]}"+"o")
        print(f"Tu {verb[:i-1]}"+"as")
        print(f"Ele {verb[:i-1]}"+"a")
        print(f"Nós {verb[:i-1]}"+"amos")
        print(f"Vós {verb[:i-1]}"+"ais")
        print(f"Eles {verb[:i-1]}"+"am")
        print()
        print("Conjugação Pretérito Perfeito I.")
        print(f"Eu {verb[:i-1]}"+"ei")
        print(f"Tu {verb[:i-1]}"+"aste")
        print(f"Ele {verb[:i-1]}"+"ou")
        print(f"Nós {verb[:i-1]}"+"amos")
        print(f"Vós {verb[:i-1]}"+"astes")
        print(f"Eles {verb[:i-1]}"+"aram")
        print()
        print("Conjugação Futuro do Pretérito I.")
        print(f"Eu {verb[:i-1]}"+"aria")
        print(f"Tu {verb[:i-1]}"+"arias")
        print(f"Ele {verb[:i-1]}"+"aria")
        print(f"Nós {verb[:i-1]}"+"aríamos")
        print(f"Vós {verb[:i-1]}"+"aríes")
        print(f"Eles {verb[:i-1]}"+"ariam")
        print()
        print("Conjugação Futuro do Presente I.")
        print(f"Eu {verb[:i-1]}"+"arei")
        print(f"Tu {verb[:i-1]}"+"arás")
        print(f"Ele {verb[:i-1]}"+"ará")
        print(f"Nós {verb[:i-1]}"+"aremos")
        print(f"Vós {verb[:i-1]}"+"areis")
        print(f"Eles {verb[:i-1]}"+"arão")

    if letra =="e":
        print("Conjugação Presente I.")
        print(f"Eu {verb[:i-1]}"+"o")
        print(f"Tu {verb[:i-1]}"+"es")
        print(f"Ele {verb[:i-1]}"+"e")
        print(f"Nós {verb[:i-1]}"+"emos")
        print(f"Vós {verb[:i-1]}"+"eis")
        print(f"Eles {verb[:i-1]}"+"em")
        print()
        print("Conjugação Pretérito Perfeito I.")
        print(f"Eu {verb[:i-1]}"+"i")
        print(f"Tu {verb[:i-1]}"+"este")
        print(f"Ele {verb[:i-1]}"+"eu")
        print(f"Nós {verb[:i-1]}"+"emos")
        print(f"Vós {verb[:i-1]}"+"estes")
        print(f"Eles {verb[:i-1]}"+"eram")
        print()
        print("Conjugação Futuro do Pretérito I.")
        print(f"Eu {verb[:i-1]}"+"eria")
        print(f"Tu {verb[:i-1]}"+"erias")
        print(f"Ele {verb[:i-1]}"+"eria")
        print(f"Nós {verb[:i-1]}"+"eríamos")
        print(f"Vós {verb[:i-1]}"+"eríes")
        print(f"Eles {verb[:i-1]}"+"eriam")
        print()
        print("Conjugação Futuro do Presente I.")
        print(f"Eu {verb[:i-1]}"+"erei")
        print(f"Tu {verb[:i-1]}"+"erás")
        print(f"Ele {verb[:i-1]}"+"erá")
        print(f"Nós {verb[:i-1]}"+"eremos")
        print(f"Vós {verb[:i-1]}"+"ereis")
        print(f"Eles {verb[:i-1]}"+"erão")

    if letra == "i":
        print("Conjugação Presente I.")
        print(f"Eu {verb[:i-1]}"+"o")
        print(f"Tu {verb[:i-1]}"+"es")
        print(f"Ele {verb[:i-1]}"+"e")
        print(f"Nós {verb[:i-1]}"+"imos")
        print(f"Vós {verb[:i-1]}"+"is")
        print(f"Eles {verb[:i-1]}"+"em")
        print()
        print("Conjugação Pretérito Perfeito I.")
        print(f"Eu {verb[:i-1]}"+"i")
        print(f"Tu {verb[:i-1]}"+"iste")
        print(f"Ele {verb[:i-1]}"+"iu")
        print(f"Nós {verb[:i-1]}"+"imos")
        print(f"Vós {verb[:i-1]}"+"istes")
        print(f"Eles {verb[:i-1]}"+"iram")
        print()
        print("Conjugação Futuro do Pretérito I.")
        print(f"Eu {verb[:i-1]}"+"iria")
        print(f"Tu {verb[:i-1]}"+"irias")
        print(f"Ele {verb[:i-1]}"+"iria")
        print(f"Nós {verb[:i-1]}"+"iríamos")
        print(f"Vós {verb[:i-1]}"+"iríes")
        print(f"Eles {verb[:i-1]}"+"iriam")
        print()
        print("Conjugação Futuro do Presente I.")
        print(f"Eu {verb[:i-1]}"+"irei")
        print(f"Tu {verb[:i-1]}"+"irás")
        print(f"Ele {verb[:i-1]}"+"irá")
        print(f"Nós {verb[:i-1]}"+"iremos")
        print(f"Vós {verb[:i-1]}"+"ireis")
        print(f"Eles {verb[:i-1]}"+"irão")