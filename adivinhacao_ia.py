import random

print("Escolha um intervalo de números inteiros para começarmos!")
x = int(input("Primeiro número do intervalo: "))
y = int(input("Último número do intervalo: "))

print(f"Pense em número no intervalo de {x} - {y}")

advinhacao = False

while not advinhacao:

    n_sorteado = random.randint(x+1, y-1)
    print(f"O número escolhido foi {n_sorteado}?  [S/N]")
    opcao = input().upper()

    if opcao == "S":
        advinhacao = True
        print(f"O número pensado por você foi {n_sorteado}!")
        print("Obrigado por jogar!")
    
    elif opcao == "N":

        print(f"O número escolhido é maior ou menor que {n_sorteado}? [M - Maior, N - Menor]")
        tam = input().upper()

        if tam == "N":
            y = n_sorteado
        
        elif tam == "M":
            x = n_sorteado
    
    else: 
        print("Digite uma opção válida!")
