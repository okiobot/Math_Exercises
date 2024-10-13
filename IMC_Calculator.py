def IMC():
    try:
        #Adquire as informações necessárias para o cálculo
        peso = int(input("Digite o seu peso: "))
        altura = float(input("Digite a sua altura: "))

        #Cálculo do IMC
        cimc = peso/altura**2
        
        #Resultados possíveis
        if cimc <= 16.9:
            print("Você está muito abaixo do peso ideal")
        elif cimc <= 18.4:
            print("Você está abaixo do peso ideal")
        elif cimc <= 24.9:
            print("Você está no peso ideal")
        elif cimc <= 29.9:
            print("Você está acima do peso ideal")
        elif cimc <= 34.9:
            print("Você está com obesidade grau 1")
        elif cimc <= 40:
            print("Você está com obesidade grau 2")
        elif cimc < 40:
            print("Você está com obesidade grau 3")
            
        #Mostra o resultado
        print(f"O seu Índice de Massa Corporal (IMC) é de: {(cimc):.2f}")
    
    #Garante que o input do usuário seja compatível  
    except ValueError:
        print("O valor é incompatível")
        
#Linha usada para demilitar
def linha():
    print("="*90)

#Executa
while True:
    IMC()
    linha()