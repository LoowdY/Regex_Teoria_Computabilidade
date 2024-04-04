# Estudo de Programas Monolíticos, Iterativos e Recursivos: Filtragem de Placas do Mercosul

Este projeto tem como objetivo explorar diferentes paradigmas de programação – especificamente, a abordagem monolítica, iterativa e recursiva – por meio do desenvolvimento de programas que realizam a mesma tarefa: a validação de placas de veículos do padrão Mercosul. Este estudo permite comparar as características, vantagens e desvantagens de cada paradigma de programação ao lidar com um problema prático e específico.

## Contexto

As placas de veículos do Mercosul seguem um formato padronizado, que pode ser descrito pela expressão regular `^[A-Z]{3}\d[A-Z]\d{2}$`. Este padrão estabelece que as placas devem começar com três letras maiúsculas, seguidas por um dígito, outra letra maiúscula, e terminar com dois dígitos. A tarefa de filtrar essas placas exige uma verificação rigorosa de cada parte da placa para garantir que ela esteja em conformidade com o padrão estabelecido.

## Abordagens

### Programa Monolítico

Na abordagem monolítica, o programa é estruturado como um bloco único, geralmente sequencial, sem a divisão em funções ou métodos. Esta abordagem foi exemplificada com um programa em C, que utiliza estruturas de decisão e o comando `goto` para navegar entre as diferentes verificações necessárias para validar a placa.

### Programa Iterativo

O programa iterativo divide o problema em uma série de passos repetidos, processando cada parte da placa em sequência. Utilizamos Python para demonstrar essa abordagem, onde um loop `for` percorre cada caractere da placa, aplicando as regras de validação específicas dependendo da posição do caractere.

### Programa Recursivo

Na abordagem recursiva, o programa se chama repetidamente até que um critério de parada seja atingido. Isso permite uma estrutura elegante e teoricamente simples, mas que requer atenção especial à condição de término para evitar a recursão infinita. O exemplo fornecido em Python verifica cada parte da placa chamando a si mesmo com o próximo caractere a ser validado, até que todos os caracteres tenham sido verificados.

## Conclusão

Este estudo revelou como diferentes abordagens de programação podem ser aplicadas para resolver o mesmo problema. Cada paradigma oferece suas próprias vantagens: o monolítico pela sua simplicidade estrutural, o iterativo pela sua clareza e eficiência em problemas sequenciais, e o recursivo pela sua elegância e expressividade em dividir o problema em subproblemas menores. A escolha entre esses paradigmas depende das necessidades específicas do projeto, da complexidade do problema e da preferência do programador.
