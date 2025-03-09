//Crie uma linked list
//Organize-a e remova as duplicatas

#include <stdio.h>
#include <stdlib.h>

struct Node { //Estrutura do node:
    int valor;
    struct Node* next; //ponteiro que aponta para um node (ou aterra)
};

struct Node* criarNode(int valor){ //retorna ponteiro(head -> aponta p primeiro node da lista)
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    //ponteiro newNode aponta para o 1o elemento
    //tem o tamanho em bytes de um Node (1 int + 1 ponteiro)
    newNode->valor = valor;
    newNode->next = NULL; //ponteiro aterrado
    return newNode;
};

void inserirFim(struct Node** head, int valor){ //recebe um ponteiro que aponta para o endereço de head(que aponta para o primeiro node) e o valor a inserir
    struct Node* newNode = criarNode(valor);
    
    if(*head == NULL){ // Se não houver node
        *head = newNode; //Insira o 1o
    }
    else{
        struct Node* move = *head; //move aponta para onde head aponta agora(node inicial) (*head indica o valor em si para qual head aponta)
        while(move->next != NULL){
            move = move->next;
        }
        move->next = newNode; //o ponteiro aterrado agora aponta para o node criado
    }
};

void printLista(struct Node* head){ //rece um ponteiro unico (head) que aponta para o primeiro node
    struct Node* temp = head; //criando ponteiro temporário
    do{
        printf("%d -> ", temp->valor);
        temp = temp->next;
    }while(temp != NULL);
    printf("NULL\n"); //incluindo o aterramento
};

int main(){
    int valor;
    struct Node* head = NULL;

    while(valor != -1){
        printf("Valor: ");
        scanf("%d", &valor);
        if(valor!=-1){
            inserirFim(&head, valor); //passando o endereço do ponteiro head em si
        }
    }

    printLista(head);

    return 0;
}