#Defs usados para fazer todos os cálculos
def triangulo():
    areaT = (baseT * alturaT) / 2
    print(f"A área do triângulo é de: {(areaT):.2f} cm²")

    volumeT = (baseT * alturaT) / 3
    print(f"O volume do triângulo é de: {(volumeT):.2f} cm³")
    
def retangulo():
    areaR = baseR * alturaR 
    print(f"A área do retângulo é de: {(areaR):.2f} cm²")

    volumeR = compR * baseR * alturaR
    print(f"O volume do retângulo é de: {(volumeR):.2f}cm³")    

def esfera():
    areaE = 4 * pi * (raioE**2)
    print(f"A área da esfera é de: {areaE} cm²")

    volumeE = (4 * pi * (raioE**3))/3
    print(f"O volume da esfera é de: {volumeE}cm³")

def cilindro():
    areaC = 2 * pi * raioC * (raioC + alturaC)
    print(f"A área do cilindro é de: {areaC} cm²")
    
    volumeC = ((raioC**2) * pi * alturaC)
    print(f"O volume do cilindro é de: {volumeC}cm3")

#Valor de pi usado nos cálculos 
pi = 3

#Linha usada para demilitar
def linha():
    print("="*90)


while True:
    try:
        #Usuário escolhe qual das opções deseja verificar
        escolha = int(input('''Escolha umas das opções abaixo: 

[1] - Cilindro
[2] - Esfera
[3] - Retângulo
[4] - Triângulo
'''))
    
        if escolha == 1:
            raioC = float(input("Digite o raio do cilindro: "))
            alturaC = float(input("Digite o tamanho da altura do cilindro: "))
            linha()
            cilindro()
            linha()
        
        if escolha == 2:
            raioE = float(input("Digite o raio da esfera: "))
            linha()
            esfera()
            linha()
        
        if escolha == 3:
            baseR = float(input("Digite o tamanho da base do retângulo: "))
            alturaR = float(input("Digite o tamanho da altura do retângulo: "))
            compR = float(input("Digite o comprimento do retângulo: "))
            linha()
            retangulo()
            linha()
        
        
        if escolha == 4:
            baseT = float(input("Digite o tamanho da base do triângulo: "))
            alturaT = float(input("Digite o tamanho da altura do triângulo: "))
            linha()
            triangulo()
            linha()
        
    #Caso o usuário digite algum valor incompatível
    except ValueError:
        linha()
        print("Valor incompatível")
        linha()