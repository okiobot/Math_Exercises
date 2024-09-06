import random
import math

def linha():
    print("="*90)

def menu():
        print('''Escolha a função que você deseja utilizar:
[1] - Soma os números
[2] - Converter para binário
[3] - Converter para octal
[4] - Converter para hexadecimal   
[5] - Calcular média
[6] - Fórmula de Fibonacci
[7] - Minigame
[8] - Cálculo de fatorial
[9] - Cálculo de raiz quadrada
[10] - Divisores do número escolhido
[11] - Cálculo de volume e área de uma esfera
[12] - Cálculo de Celsius para Fahrenheit
[13] - Cálculo de Celsius para Kelvin
''')
linha()

numeros = []
total = []

def soma():
    while True:
        num = int(input("Digite os número para somar: "))
        total.append(num)
        print(total)
        if num == 0:
            print("A soma é: "+str(sum(total)))
            break
            
def binario():
    A = bin(int(input("Digite um número para converter para binário: ")))
    numerobinario = str(A)
    print("O número em binário é: "+numerobinario[2:])
    
def octal():
    B = oct(int(input("Digite o número para converter para octal: ")))
    numerooctal = str(B)
    print("O número em octal é: "+numerooctal[2:])

def media():
    while True:
        lista = int(input("Escolha quais números você deseja adicionar para calcular a média: "))
        if lista == 0:
            media = sum(numeros)/len(numeros)
            print("A média é: "+str(media))
            break
        numeros.append(lista)
        
def hexadecimal():
    H = hex(int(input("Digite um número para converter em hexadecimal: ")))
    C = str(H)
    numerohexa = C.upper()
    print("O número em hexadecimal é: "+numerohexa[2:])

def Fibonacci():
    D = int(input("Escolha o número para calcular a sequência de Fibonacci: "))
    i = 1
    if D > 2:
        fib = [1,1]
        while i < (D - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    print(fib)

def game():
    print("Seu objetivo é acertar o número que o cumputador escolher")
    jogador = int(input("Escolha um número entre 1 e 4: "))
    opcoes = [1,2,3,4]
    bot = random.choice(opcoes)
    if jogador == bot:
        print("O oponente escolheu: "+str(bot))
        print("Você venceu!")
    else:
        print("Você perdeu!")

def fatorial():
    num = int(input("Digite um número para calcular seu fatorial: "))
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("O fatorial do número escolhido é: "+str(fact))

def raizquadrada():
    num = int(input("Digite um número para descobrir sua raiz quadrada: "))
    raiz = math.sqrt(num)
    print("A raiz quadrada do número escolhido é: "+str(raiz))        
   
def divisiveis():
    num = int(input("Digite um número para descobrir seus divisíveis: "))
    lista = []
    listRange = list(range(1,num+1))
    for i in listRange:
        if num % i == 0:
            lista.append(i)
    print(lista)    

def volume():
    radius = float(input("Digite o tamanho da esfera: "))
    areasup = 4*math.pi*(radius**2)
    volum = (4/3)*math.pi*radius**3
    print(f"A área é de: {(areasup):.2f}")
    print(f"O volume é de: {(volum):.2f}")

def celsius():
    temp = int(input("Digite a temperatura que você deseja converter: "))
    farenheint = (9/5 * temp) + 32
    print(f"A temperatura convertida é equivalente a: {(farenheint):.1f}F")

def kelvin():
    temp = int(input("Digite a temperatura que você deseja converter: "))
    k = temp + 273
    print("A temperatura convertido é equivalente a: "+str(k)+"K")

while True:
    menu()
    
    escolha = input("Escolha uma das opções: ")
    linha()
    
    if escolha == "1":
        soma()
        linha()
    
    if escolha == "2":
        binario()
        linha()

    if escolha == "3":
        octal()
        linha()
        
    if escolha == "4":
        hexadecimal()
        linha()

    if escolha == "5":
        media()
        linha() 
           
    if escolha == "6":
        Fibonacci()
        linha()
        
    if escolha == "7":
        game()
        linha()
        
    if escolha == "8":
        fatorial()
        linha()
        
    if escolha == "9":
        raizquadrada()
        linha()
        
    if escolha == "10":
        divisiveis()
        linha()
        
    if escolha == "11":
        volume()
        linha()
        
    if escolha == "12":
        celsius()
        linha()
        
    if escolha == "13":
        kelvin()
        linha()
        
