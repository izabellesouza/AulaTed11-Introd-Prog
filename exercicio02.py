'''
2. Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
a. Imprima o resultado da soma de todos os valores da matriz no terminal;
b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;
'''


import random  # Importa a biblioteca random para gerar números aleatórios

# Passo 1: Criar uma matriz de 10x10 com valores aleatórios entre 10 e 20
matriz_a = []
for i in range(10):  # Para cada linha (total de 10)
    linha = []  # Cria uma lista para armazenar os valores da linha
    for j in range(10):  # Para cada coluna (total de 10)
        valor_aleatorio = random.randint(10, 20)  # Gera um valor entre 10 e 20
        linha.append(valor_aleatorio)  # Adiciona o valor na linha
    matriz_a.append(linha)  # Adiciona a linha completa na matriz_a

# Passo 2: Calcular a soma de todos os valores da matriz_a
soma = 0
for linha in matriz_a:  # Para cada linha em matriz_a
    for valor in linha:  # Para cada valor na linha
        soma += valor  # Soma o valor ao total

# Passo 3: Exibir a matriz A e o resultado da soma
print('\n--------------- Matriz A ---------------\n')
for linha in matriz_a:
    print(linha)
print('\n')
print(f'Resultado da soma de todos os valores da Matriz A: {soma}')
print('\n')

# Passo 4: Criar a matriz B, onde cada valor é o triplo do valor correspondente em matriz_a
matriz_b = []
for linha in matriz_a:  # Para cada linha em matriz_a
    nova_linha = []  # Cria uma nova linha para matriz_b
    for valor in linha:  # Para cada valor na linha
        novo_valor = valor * 3  # Multiplica o valor por 3
        nova_linha.append(novo_valor)  # Adiciona o novo valor na nova linha
    matriz_b.append(nova_linha)  # Adiciona a linha completa na matriz_b

# Passo 5: Exibir a matriz B
print('--------------- Matriz B ---------------\n')
print('--> Matriz B = Matriz A * 3\n')
for linha in matriz_b:
    print(linha)
print('\n')
