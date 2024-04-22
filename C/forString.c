#include <stdio.h> //Incluindo biblioteca stdio.h para facilitar a programação
int main() {//Abrindo a função main que não receberá nenhum parâmetro

    char str[21]; //Definindo a variável 'str' que guardará a string dada pelo usuário
    // Essa string poderá ter até 20 caracteres, pois o ultimo (str[21]) é \0 que determina o fim da string
    int i, cont = 0, contV = 0, contN = 0, contE=0; // Definindo as variáveis inteiras
    // i -> argumento do for
    // cont -> quantidade total de caracteres
    // contV -> quantidade de vogais
    // contN -> quantidade de consoanmtes
    // contE -> quantidade de caracteres especiais (Maiusculas, símbolos, pontos e etc.)
    
    //Esse bloco de código inteiro está dizendo ao usuário a condição para o programa funcionar corretamente
    printf("Seguindo a seguinte condição:\n");
    printf("\t ->Um espaço depois do 1o caractere será contado como fim da string\n");
    printf("Insira uma string de até 20 caracteres\n");
    //Fim do bloco
    scanf("%s", str); // Recebendo a string do usuário
    
    for (i = 0; str[i] != '\0'; i++) { //Usando o for para verificar certas condições em cada caractere da string
        
        printf("Caractere %d: %c\n", i, str[i]); //Ao usar o printf devemos especificar o tipo de eneunciação que vamos dar às variáveis
        //%d -> representação decimal com sinal
        //%c -> representação ASCII
        //Nesse caso não se usa '&str[i]' pois isso apontaria para o endereço de memória(agindo como um 'pointer') e não o valor
        
        //Se o elemento i de str for uma vogal minúscula, aumente em 1 contV
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') {
            contV++;
        
        //Se o elemento i de str não for uma vogal minúscula, então veja se ele está presente no restante do alfabeto e é minúscula e aumente em 1 contN
        } else if ((str[i] >= 'b')  && (str[i] <= 'z')){
            contN++;
        
        //Se ambas as condições não forem verdade, então o caractere é um caractere especial, dessa forma, aumente em 1 contE
        } else {
            contE++;
        }
        cont++; //Aumente em 1 a quantidade de caracteres preenchidos de str
    }
    
    //**Essas comparações nos if's estão baseadas nos valores da tabela ASCII que guarda a composição binária dos caracteres, como por exemplo 00100110 = &
    
    printf("Total de caracteres: %d\n", cont); //Retorna cont, que guarda a quantidade de caracteres na string str
    printf("Total de vogais: %d\n", contV); // Retorna contV, que guarda a quantidade de vogais minuscúlas
    printf("Total de caracteres especiais: %d\n", contE); // Retorna contV, que guarda a quantidade de vogais minuscúlas
    printf("Total de consoantes: %d\n", contN); // Retorna contV, que guarda a quantidade de consoantes minuscúlas

    return 0; //Programa retorna 0, que é o exit code
}