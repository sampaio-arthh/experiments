coeficiente_1_de_x = int(input('Insira o 1º coeficiente de X: '))
coeficiente_1_de_y = int(input('Insira o 1º coeficiente de Y: '))
coeficiente_1_de_z = int(input('Insira o 1º coeficiente de Z: '))
final1 = int(input('Insira o 1º resultado: '))
coeficiente_2_de_x = int(input('Insira o 2º coeficiente de X: '))
coeficiente_2_de_y = int(input('Insira o 2º coeficiente de Y: '))
coeficiente_2_de_z = int(input('Insira o 2º coeficiente de Z: '))
final2 = int(input('Insira o 2º resultado: '))
coeficiente_3_de_x = int(input('Insira o 3º coeficiente de X: '))
coeficiente_3_de_y = int(input('Insira o 3º coeficiente de Y: '))
coeficiente_3_de_z = int(input('Insira o 3º coeficiente de Z: '))
final3 = int(input('Insira o 3º resultado: '))


option = int(input('Opção 1: Determinante da Matriz, Opção 2: Valor de Cada Variável (Responda em número !) '))

if option == 1:
    Operacao1 = coeficiente_1_de_x * coeficiente_2_de_y * coeficiente_3_de_z
    Operacao2 = coeficiente_1_de_y * coeficiente_2_de_z * coeficiente_3_de_x
    Operacao3 = coeficiente_1_de_z * coeficiente_2_de_x * coeficiente_3_de_y
    Resultado1 = Operacao1 + Operacao2 + Operacao3
    
    Operacao4 = coeficiente_1_de_z * coeficiente_2_de_y * coeficiente_3_de_x
    Operacao5 = coeficiente_1_de_x * coeficiente_2_de_z * coeficiente_3_de_y
    Operacao6 = coeficiente_1_de_y * coeficiente_2_de_x * coeficiente_3_de_z
    Resultado2 = Operacao4 + Operacao5 + Operacao6

    Determinante = Resultado1 - Resultado2

    print(Determinante)

if option == 2:
    Operacao1 = coeficiente_1_de_x * coeficiente_2_de_y * coeficiente_3_de_z
    Operacao2 = coeficiente_1_de_y * coeficiente_2_de_z * coeficiente_3_de_x
    Operacao3 = coeficiente_1_de_z * coeficiente_2_de_x * coeficiente_3_de_y
    Resultado1 = Operacao1 + Operacao2 + Operacao3
    
    Operacao4 = coeficiente_1_de_z * coeficiente_2_de_y * coeficiente_3_de_x
    Operacao5 = coeficiente_1_de_x * coeficiente_2_de_z * coeficiente_3_de_y
    Operacao6 = coeficiente_1_de_y * coeficiente_2_de_x * coeficiente_3_de_z
    Resultado2 = Operacao4 + Operacao5 + Operacao6

    Determinante = Resultado1 - Resultado2

    Operacao_x_1 = final1 * coeficiente_2_de_y * coeficiente_3_de_z
    Operacao_x_2 = coeficiente_1_de_y * coeficiente_2_de_z * final3
    Operacao_x_3 = coeficiente_1_de_z * final2 * coeficiente_3_de_y
    Resultado_x_1 = Operacao_x_1 + Operacao_x_2 + Operacao_x_3
    Operacao_x_4 = coeficiente_1_de_z * coeficiente_2_de_y * final3
    Operacao_x_5 = final1 * coeficiente_2_de_z * coeficiente_3_de_y
    Operacao_x_6 = coeficiente_1_de_y * final2 * coeficiente_3_de_z
    Resultado_x_2 = Operacao_x_4 + Operacao_x_5 + Operacao_x_6

    Determinante_x = Resultado_x_1 - Resultado_x_2
    X = Determinante_x / Determinante

    

    Operacao1y = coeficiente_1_de_x * final2 * coeficiente_3_de_z
    Operacao2y = final1 * coeficiente_2_de_z * coeficiente_3_de_x
    Operacao3y = coeficiente_1_de_z * coeficiente_2_de_x * final3
    Resultado1y = Operacao1y + Operacao2y + Operacao3y
    
    Operacao4y = coeficiente_1_de_z * final2 * coeficiente_3_de_x
    Operacao5y = coeficiente_1_de_x * coeficiente_2_de_z * final3
    Operacao6y = final1 * coeficiente_2_de_x * coeficiente_3_de_z
    Resultado2y= Operacao4y + Operacao5y + Operacao6y

    Determinante_y = Resultado1y - Resultado2y
    Y = Determinante_y / Determinante

    Operacao1z = coeficiente_1_de_x * coeficiente_2_de_y * final3
    Operacao2z = coeficiente_1_de_y * final2 * coeficiente_3_de_x
    Operacao3z = final1 * coeficiente_2_de_x * coeficiente_3_de_y
    Resultado1z = Operacao1z + Operacao2z + Operacao3z
    
    Operacao4z = final1 * coeficiente_2_de_y * coeficiente_3_de_x
    Operacao5z = coeficiente_1_de_x * final2 * coeficiente_3_de_y
    Operacao6z = coeficiente_1_de_y * coeficiente_2_de_x * final3
    Resultado2z = Operacao4z + Operacao5z + Operacao6z

    Determinante_z = Resultado1 - Resultado2

    Z = Determinante_z / Determinante

    print('Essa é a sua matriz: ')
    print(' ')
    print('|' + str(coeficiente_1_de_x) + ' ' + str(coeficiente_1_de_y) + ' ' + str(coeficiente_1_de_z) + '|')
    print('|' + str(coeficiente_2_de_x) + ' ' + str(coeficiente_2_de_y) + ' ' + str(coeficiente_2_de_z) + '|')
    print('|' + str(coeficiente_3_de_x) + ' ' + str(coeficiente_3_de_y) + ' ' + str(coeficiente_3_de_z) + '|')
    print(' ')
    print("Os valores das incógnitas são:")
    print('X = ' + str(X))
    print('Y = ' + str(Y))
    print('Z = ' + str(Z))