#include <stdio.h>
#include <stdlib.h>

// Objetivo: Linked-list + Função que obtém uma, arruma e printa

struct Node {
    int valor; //valor guardado pelo node
    struct Node* next; //ponteiro next aponta para um Node
};

struct Node* criarNode(int valor){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));//ponteiro que aponta para Node funciona como criador de nodes
    newNode->valor = valor;
    newNode->next = NULL;
    return newNode;
}

void inserirFim(struct Node** head, int valor){// **head é um ponteiro que apontará para o ponteiro para permitir muda o valor do que ele aponta e não para oq ele aponta
    struct Node* newNode = criarNode(valor);
    
    if (*head ==NULL){//head vazia
        *head = newNode;//head aponta para o node criado com o valor do input
    }

    else{
        struct Node* ant = *head;// ponteiro ant vai guardar para a head
        while(ant->next != NULL){//Atravessa a lista até o último nó
            ant = ant->next; //aponte para o endereço do próximo next
        }
        ant->next = newNode; //o antigo ponteiro aterado final agora aponta para esse novo Node que tem seu ponteiro aterrado
    }
}

void printLista(struct Node* head){
    struct Node* temp = head;
    while(temp !=NULL){// Enquanto não for o fim da lista
        printf("%d -> ", temp->valor); //imprime o valor do nó
        temp = temp->next; //avança para o próximo nó
    }
    printf("-> NULL\n"); //indica que a lista terminou
}

void freeLista(struct Node* head){
    struct Node* temp;
    while(head != NULL){// Enquanto não for o fim da lista
        temp = head;
        head = head->next;
        free(temp); //libera a memória de cada nó
    }
}

int main(){
    int val;

    struct Node* head = NULL; //Ponteiro head que aponta para a sequênciia de nodes
    do{
        puts("Forneça um valor inteiro (-1 para concluir): ");
        scanf("%d", &val);// Receba o valor no regex %d e aloque no endereço de memória de &val
        if (val != -1){
            inserirFim(&head, val);//passando o endereço do ponteiro, assim a função recebe o ponteiro em si e suas propriedades
        }
    }while(val !=-1);//O valor de parada é: -1

    printLista(head);
    freeLista(head);
}
