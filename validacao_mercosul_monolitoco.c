//incluindo bibliotecas para tratar placas do mercosul (sem regex)
#include <stdio.h>
#include <ctype.h>

//expressão regular: ^[A-Za-z]{3}\d[A-Za-z]\d{2}$ 
//o codigo abaixo é monolítico, ou seja, possui apenas estruturas de decisão e o uso do goto.

//função principal do programa (onde a lógica mais relevante se desenvolve)
int main() {
    
    //vetor com 8 posições (7 digitos e terminador nulo)
    char placa[8]; 
    printf("Digite a placa no formato Mercosul (exemplo: ABC1D23): ");
    
    //captura do input do usuário com 7 digitos e com string.
    scanf("%7s", placa);

//inicializando contador para validação da placa (estruturas de decião mais abaixo)
    int i = 0;

    // estrutura de decisão para verificar letras (input)
    check_letters:
        if (i < 3) {
            if (isupper(placa[i])) {
                i++;
                goto check_letters;
            } else {
                printf("Placa inválida. As primeiras três posições devem ser letras maiúsculas.\n");
                return 1;
            }
        }

    // verificador de dígitos (input)
    check_first_digit:
        if (isdigit(placa[3])) {
            i = 4; 
            goto check_letter;
        } else {
            printf("Placa inválida. A quarta posição deve ser um dígito.\n");
            return 1;
        }

    // verificador de letra (input entre numero e dois digitos finais)
    check_letter:
        if (isupper(placa[i])) {
            i++;
            goto check_digits;
        } else {
            printf("Placa inválida. A quinta posição deve ser uma letra maiúscula.\n");
            return 1;
        }

    // Verificar dígitos finais (ultimos dois elementos)
    check_digits:
        if (i < 7) {
            if (isdigit(placa[i])) {
                i++;
                goto check_digits;
            } else {
                printf("Placa inválida. As últimas duas posições devem ser dígitos.\n");
                return 1;
            }
        }

    printf("Placa válida.\n");
    return 0;
}
