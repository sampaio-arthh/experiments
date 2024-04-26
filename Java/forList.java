// O programa deverá apresentar ao usuário uma lista de compras de 10 produtos
// A partir dessa o usuário poderá escolher aquilo que quer adicionar ao carrinho
import java.util.Scanner;
public class forList {
    public static void main(String[] args){
            int j, resp, respU; //j -> iterador, resp -> operação e seleção de produto, respU -> quantidade de unidades
            double[] precos = {9.99, 7.98, 7.98, 13.98, 11.99, 8.99, 15.98, 14.98, 33.49, 37.98};
            double carr = 0; //carrinho
            int[] arrComp = new int[10]; //Quantidade de produto no carrinho
            Scanner i = new Scanner(System.in);
            String[] prods = {"Banana", "Maçã", "Pera", "Caju", "Uva", "Pão", "Manteiga", "Requeijão", "Queijo Mussarela", "Queijo Minas"};
            
            do{
                
                System.out.println("Carrinho = "+carr);
                
                do{
                    System.out.println("O que gostaria de fazer ?");
                    System.out.println("1 - Adicionar ao carrinho");
                    System.out.println("2 - Remover do carrinho");
                    System.out.println("99 - Finalizar compra");
                    System.out.println();
                    resp = i.nextInt();
                    System.out.println();
                }while(resp != 1 && resp != 2 && resp != 99);
                
                if(resp==1){
                    
                    do{
                        for (j=0;j!=10;j++){
                            System.out.println((j+1)+" - "+prods[j]+" - "+precos[j]);
                        }
                        System.out.println("Qual produto gostaria ?");
                        resp = i.nextInt();
                        
                    }while(resp>10 && resp <1);
                    
                    do{
                        System.out.println("Quantas unidades de "+prods[(resp-1)]+" gostaria ?");
                        respU = i.nextInt();
                    }while(respU<0);
                    arrComp[(resp-1)] += respU;
                    carr += (respU*precos[(resp-1)]);

                }
                else if (resp==2) {
                    do{
                        System.out.println("Carrinho = "+carr);
                        System.out.println("Qual produto quer retirar ?");
                        resp = i.nextInt();
                    }while(resp>10 && resp <1);
                    
                    if(arrComp[(resp-1)]>=0){
                        do{
                            System.out.println("Quantas unidades de "+prods[(resp-1)]+" deseja remover ?");
                            respU = i.nextInt();
                        }while(respU<0);
                        
                        arrComp[(resp-1)] -= respU;
                        carr -= (respU*precos[(resp-1)]);
                    }
                    
                    


                }
            }while(resp!=99);
    }
}