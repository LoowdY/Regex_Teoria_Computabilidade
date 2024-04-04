#regex: ^[A-Za-z]{3}\d[A-Za-z]\d{2}$ 

#FUNÇÃO PARA VERIFICAR PLACA
def verificar_placa(placa):
    
    #ESTRUTURA DE DECISÃO PARA VERIFICAR TAMANHO DA PLACA
    if len(placa) != 7:
        print("Placa inválida. O tamanho está incorreto.")
        return False
    
    #AQUI VERIFICA-SE A PARTE ITERATIVA (LOOP FOR)
    #VERIFICANDO DIGITOS (ESTRUTURA DE DECISÃO)
    for i, char in enumerate(placa):
        if i < 3: 
            if not char.isupper() or not char.isalpha():
                print("Placa inválida. As primeiras três posições devem ser letras maiúsculas.")
                return False
        elif i == 3:  
            if not char.isdigit():
                print("Placa inválida. A quarta posição deve ser um dígito.")
                return False
        elif i == 4:  
            if not char.isupper() or not char.isalpha():
                print("Placa inválida. A quinta posição deve ser uma letra maiúscula.")
                return False
        else:  
            if not char.isdigit():
                print("Placa inválida. As últimas duas posições devem ser dígitos.")
                return False
    
    #INFORMANDO USUÁRIO CASO A VALIDAÇÃO SEJA ACEITA
    print("Placa válida.")
    return True

#FUNÇÃO MAIN QUE PEDE INPUT DE PLACA DO USUÁRIO
def main():
    placa = input("Digite a placa no formato Mercosul (exemplo: ABC1D23): ")
    verificar_placa(placa)


#BLOCO DE EXECUÇÃO PRINCIPAL DO PROGRAMA (EXECUTA FUNÇÃO MAIN())
if __name__ == "__main__":
    main()
