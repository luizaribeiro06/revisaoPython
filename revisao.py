#revisão para cp4 - python

#array

a = [1,2,3,4,5]
#print(a[2])

array = [10,20,30,40,50]
array[1] = 25
#print(array)

#loop para aparecer as cidades
cidades = ["SP", "RJ", "BH"]
for i in cidades:
    print(i)

#somar todos os números da lista
soma = [1,2,3,4,5]
somas = 0
for i in soma:
    somas += i
print(somas)

#listas
#adicionar um elemento (sempre no fim)
lista = [1,2,3]
lista.append(4)

#remover um elemento (pode escolher o índice)
lista.pop(0)

#juntar duas listas
lista1 = [1,2,3]
lista2=[4,5,6]

lista1.extend(lista2) #vai adicionar os elementos da lista 2 na lista 1

#lambda (função simplificada, não pode ter condição e não tem retorn
mult = lambda x: x*x
print(mult(2))

#reverter a string
revert = lambda str: str[::-1]

#verificar se é palindromo
palin= lambda texto: texto == texto[::-1]
print(palin("arara")) #ele aparece como True or False

#como contar vogais em uma string?
def vogais(palavra):
    i = 0
    soma =0
    while i < len(palavra):
        if palavra[i] ==  'a' or palavra[i] ==  'e' or palavra[i] ==  'i' or palavra[i] ==  'o' or palavra[i] ==  'u':
            soma +=1
        i +=1
    return soma

#ouuuuuu usando for >>>>>>
def vogais(palavra):
    qtd = 0
    for i in palavra:
        if palavra[i] ==  'a' or palavra[i] ==  'e' or palavra[i] ==  'i' or palavra[i] ==  'o' or palavra[i] ==  'u':
            qtd +=1
        return qtd

#list comprehension
# estrutura: expression for item in objeto iteravel if condition == True

#exercicios
#quadrados dos números de 1 a 10
lista=[1,2,3,4,5,6,7,8,9,10]
quadrados=[i*i for i in lista]
print(quadrados)

#uma lista contendo apenas os números pares de 1 a 20
pares = [i for i in range(1,21) if i%2 == 0]
print(pares)

#lista contendo o comprimento de cada palavra
palavras = ["Python", "List", "Comprehension", "Exercícios"]
len = [len(i) for i in palavras]
print(len)

#converter a temperatura de celsius --> fahrenreit
temp = [0,10,20,30,40]
f = [i*9/5 + 32 for i in temp]
print(f)

#lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz"
nums=["Fizz" if i%3==0 else i for i in range(1,21)]
print(nums)

#criar uma nova lista apenas com as palavras +5 letras
frutas=["maçã", "banana", "uva", "morango", "abacaxi"]
#cinco = [i for i in frutas if len(i)>5]

#lista representando as coordenadas [x,y] para um grid 3x3
coord = [[x,y] for x in range (3) for y in range (3)]
print(coord)

#forma compactada/alternativa de inicializar uma matriz
l= int(input("Número de linhas: "))
c= int(input("Número de linhas: "))
matriz = [[0] for i in range(c) for i in range(l)]

#função
#sistema de depósito, saque e extrato
def depositar(quantia):
    global saldo
    global trans
    saldo  = saldo + quantia
    trans.append(quantia)
    return saldo
saldo = 50
trans = []

def sacar(saque):
    global saldo
    global trans
    saldo = saldo - saque
    trans.append(-saque)
    return saldo
saldo = 20

def extrato():
    for i in trans: # só quer o elemento da lista
        print(i)
    print(f"Saldo final: ", {saldo})

while True:
    opcao = input("1 SAQUE 2 DEPÓSITO 3 EXTRATO 4 SAIR")
    if opcao == "1":
        print(sacar(int(input("Digite o valor que deseja sacar"))))
    elif opcao == "2":
        print(depositar(int(input("Digite o valor que deseja sacar"))))
    elif opcao == "3":
        print(extrato(int(input("Digite o valor que deseja sacar"))))
    elif opcao == "4":
        print("encerrando o app")
        break
    else:
        print("opção inválida")


#criação de uma matriz
matriz = []
#com input do usuario
l = int(input("Digite o valor para a qtd de linhas: "))
c = int(input("Digite o valor para a qtd de colunas: "))
for i in range(l):
    linha = []
    matriz.append(linha)
    for j in range(c):
        linha.append(int(input(f"Digite o valor para [{i}] e [{j}]: ")))
print(matriz)

#ordem sequencial 1  9
l = 3
c = 3
qtd = 1

for i in range(l):
    linha = []
    matriz.append(linha)
    for j in range(c):
        for h in range(qtd <=10):
            linha.append(qtd)
            qtd +=1
print(matriz)

#para somar os elementos da segunda linha, por exemplo:

soma = 0
indice_linha = 1
for i in matriz[indice_linha]:
    soma+=i
print(soma)

#encontrar o maior valor da matriz
#ele vai comparando até chegar no maior = 9
maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero
print(maior)


#para acessar elementos
#indice começa em 0 sempre
#matriz[linha][coluna]

#para copiar uma matriz
a = [1,2,3]
b  = a.copy()
#ou
b = a[:]
#print(b)

#printar apenas colunas pares da matriz
def colunas_pares(matriz):
    colunaspar = []
    for i in len(matriz):
        linhaspar=[]
        for j in len(matriz[0]):
            if j%2 == 0:
                linhaspar.append(matriz[i][j])
            colunaspar.append(linhaspar)
    return colunaspar

#e se fosse ímpar?
"""if j%2 != 0:
    linhasimpar.append(matriz[i]) #pega a linha inteira"""

#somente a diagonal
def diagonal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i], end='')
print(diagonal(matriz))

#soma da diagonal
def soma_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

print(soma_diagonal(matriz))

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in matriz:
    for j in i:
        print(f"{j:^2}", end='')
    print()

#tranposta
def transposta(matriz):
    t = []
    for i in len(matriz[0]):
        linha= []
        for j in len(matriz):
            linha.append(matriz[i][j])
        t.append(linha)
    return t

#soma de matrizes
#linha.append(matriz1[i][j] + matriz2[i][j])

#calcular o produto interno entre dois vetores
#o primeiro vezes o primeiro + segundo vezes o segundo + ....
def produto_interno(j,h):
    resultado = 0
    for i in range(len(j)):
        resultado += j[i] * h[i]
    return resultado

j = [1,2,3]
h= [4,5,6]
print(produto_interno(j,h))

#multiplicar matrizes (dimensão nxn)
def mult(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam) for i in range(tam)]]
    for i in range(tam):
        for j in range(tam):
            for k in range(tam):
                mat3[i][j] =  mat3[i][j] + (mat1[i][k] *  mat2[k][j])

#aparecer sem colchete e pular linha
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in matriz:
    for j in i:
        print(f"{j:^2}", end='') #end fica do lado da outra
    print() #pula linha

#desafio de pi usando matriz

import random

#definição do tamanho da matriz
n= 10000
#cria uma matriz para armazenar os pontos
pontos = [[random.uniform(-1,1), random.uniform(-1,1)] for i in range(n)]

#contador de qnts pontos caem dentro do circulo de acordo com a equação x2 + y2 <=
dentro_circulo = 0
for ponto in pontos:
    x,y = ponto
    if x**2 + y**2 <= 1:
        dentro_circulo +=1

#a razão dentro_circulo/n significa aproxima pi/4, por isso multiplica
pi = 4* (dentro_circulo/n)

#em função:
import random
def gerar_pontos(n):
    return [[random.uniform(-1,1), random.uniform(-1,1)] for i in range(n)]

def contar_pontos_circulo(pontos):
    cont = 0
    for x,y in pontos:
        if x ** 2 + y ** 2 <= 1:
            cont += 1
    return cont

def calcular_pi(n):
    pontos = gerar_pontos(n)
    dentro_circulo = contar_pontos_circulo(pontos)
    return 4 * (dentro_circulo/n)

n = 1000
pi = calcular_pi(n)
print(f"Estimativa de Pi com {n} pontos: {pi}")

#docstring - serve para documentação
"""
    :param a: inteiro
    :param b: inteiro
    :param c: inteiro
    :return: retorna a soma dos 3 parâmetros
"""
