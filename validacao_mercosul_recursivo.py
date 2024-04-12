#regex: ^[A-Z]{3}\d[A-Z]\d{2}$ 

#FUNÇÃO RECURSIVA PARA VERIFICAR PLACA (PROGRAMA RECURSIVO)
def verificar_placa_recursiva(placa, i=0):
    
    #CASO SEJA VALIDADA, ENTRA-SE NESSA ESTRUTURA DE DECEISÃO
    if i == len(placa):
        print("Placa válida.")
        return True
    
    #ESTRUTURAS DE DECESÃO PARA VERIFICAÇÃO DOS DÍGITOS
    if i == 0 and len(placa) != 7:
        print("Placa inválida. O tamanho está incorreto.")
        return False
    
    
    if i < 3:  
        if not placa[i].isupper() or not placa[i].isalpha():
            print("Placa inválida. As primeiras três posições devem ser letras maiúsculas.")
            return False
    elif i == 3:  
        if not placa[i].isdigit():
            print("Placa inválida. A quarta posição deve ser um dígito.")
            return False
    elif i == 4:  
        if not placa[i].isupper() or not placa[i].isalpha():
            print("Placa inválida. A quinta posição deve ser uma letra maiúscula.")
            return False
    else:  
        if not placa[i].isdigit():
            print("Placa inválida. As últimas duas posições devem ser dígitos.")
            return False
    
    #AQUI OCORRE A RECURSÃO (PROGRAM RECURSIVO)
    return verificar_placa_recursiva(placa, i + 1)

#FUNÇÃO PRINCIPAL DO PROGRAMA (SOLICITA INPUTO DO USUÁRIO E VALIDA PLACA)
def main():
    placa = input("Digite a placa no formato Mercosul (exemplo: ABC1D23): ")
    verificar_placa_recursiva(placa)


#DIVISÃO LÓGICA DO PYTHON PARA O BLOCO PRINCIPAL
if __name__ == "__main__":
    main()
