'''
Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram.
'''

# Criar vetor VET com 10 números
# Verificar repetidos e escrever o índice em que estão

vet =[] #lista(vetor) vazio para que números sejam armazenados nele
for i in range(10): #gera uma sequência de n. inteiros e percorre cada n. dessa sequência até o máximo de 10 entradas
    numero = int(input("Digite um número: ")) #criada variável numero que recebe o dado do input
    vet.append(numero) #dentro da lista vet adiciono a variavel numero, que agora tem o valor do input

print("Vetor final: ", vet) #Imprime a lista vet contendo todos os números inseridos

posicoes ={} #Cria um dicionário posicoes para armazenar números e suas respectivas posições no vetor vet

for i in range(len(vet)): #a função len permite verificar o comprimento da lista vet
    num = vet[i] #a variável num vai armazenar o dado na posição i do vetor vet
    if num in posicoes: #se a variável num estiver no dicionário posições, faça:
        posicoes[num].append(i) #indice i é concatenado com num
    else: #caso contrário, faça:
        posicoes[num] =[i] #num é adicionado ao dicionário posições no índice i

for i, numero_repetido in enumerate(vet): #função enumerate itera sobre vet e retorna indice (i) e o valor correspondente de cada iteração (numero_repetido) até que todos os elementos de vet tenham sido processados
    if numero_repetido in vet[i+1:]: #Verifica se numero_repetido aparece na sublista vet[i + 1:], evitando a comparação consigo mesmo e com posições anteriores.
        print(f'numero repetido: {numero_repetido}, na posição {i}') #Imprime o número repetido e sua posição original no vetor