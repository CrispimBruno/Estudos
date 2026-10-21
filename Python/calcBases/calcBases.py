#Calculadora de bases feita inteiramente em python SEM IA, só eu

#Vou fazer a calculadora com 2 partes principais, a primeira vai ser transformar a base atual na base 10, depois vou trasnformar essa base 10 na desejada. Meu foco vai ser colocar uma tela para literalmente virar uma calculadora, mas por hora vai ser no terminal
#os nomes das funções vão ser diretamente relacionadas a base, porém resumidas

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#primeiro uma função que chama outra função (definidor da base)

def chamadorDeFunção(Base1, numero, parte):
        if Base1 == "1":
            if parte == 1:
                    return binDec(numero)
            elif parte == 2:
                    return decBin(numero)
            else: 
                print("O numero digitado está errado. Por favor tente novamente")
                parte1()
        elif Base1 == "2":
            if verificadorOct(numero):
                if parte == 1:
                    return octDec(numero)
                elif parte == 2:
                    return decOct(numero)
            else: 
                print("O numero digitado está errado. Por favor tente novamente")
                parte1()
        elif Base1 == "3":
            if verificadorDec(numero):
                if parte == 1:
                    return decDec(numero)
                elif parte == 2:
                    return decDec(numero)
            else: 
                print("O numero digitado está errado. Por favor tente novamente")
                parte1()
        elif Base1 == "4":
            if verificadorHex(numero):
                if parte == 1:
                    return hexDec(numero)
                elif parte == 2:
                    return decHex(numero)
            else: 
                print("O numero digitado está errado. Por favor tente novamente")
                parte1()



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#primeiro um verificador, para definir se o numero é ou não da base indicada
def verificadorBin(numero):
    for i in numero:
        if int(i)-1  >= -1 and int(i)+1 <= 2:
            pass
        else: 
            return False
    return True

def verificadorOct(numero):
    for i in numero:
        if int(i)-1 >= -1 and int(i) + 1 <= 8:
            pass
        else:
            return False
    return True

def verificadorDec (numero):
    for i in numero:
        if i.isdigit():
            pass
        else: 
            return False
    return True

def verificadorHex(numero):
    for i in numero:
        if i.isdigit():
            pass
        elif ord(i.upper()) >=65 and ord(i.upper()) <=70:
            pass
        else: 
            return False
    return True


#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#funções que transformam todas as bases para base 10, matematicamente. [::-1] é um invertor de string
        
def binDec(numero): 
    decimal = 0
    numeroInvertido = numero[::-1]
    potencia = 0
    for i in numeroInvertido:
        inteiro = int(i)
        decimal += (inteiro)*(2**potencia)
        potencia += 1
    return decimal

def octDec(numero): 
    decimal = 0
    numeroInvertido = numero[::-1]
    potencia = 0
    for i in numeroInvertido:
        inteiro = int(i)
        decimal += (inteiro)*(8**potencia)
        potencia += 1
    return decimal

def decDec(numero):
    #já passou pelo verificador kk, não existe passar da base 10 para 10
    #isso aqui é inutil, coloquei só para seguir a lógica. Basta ter o verificador
    return int(numero)

def hexDec(numero):
    decimal = 0
    numeroInvertido = numero[::-1]
    potencia = 0
    for i in numeroInvertido:
        if i.upper() == "A":
            i = 10
        elif i.upper() == "B":
            i = 11
        elif i.upper() == "C":
            i = 12
        elif i.upper() == "D":
            i = 13
        elif i.upper() == "E":
            i = 14
        elif i.upper() == "F":
            i = 15
        inteiro = int(i)
        decimal += (inteiro)*(16**potencia)
        potencia += 1
    return decimal

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#funções que transformam a base 10 em todas as bases, matematicamente.
#Aqui, a lógica de todos é parecido.É uma divisão subsequente e sua ordem inversa. Salvarei em String

def decBin(numero):
    inteiro = int(numero)
    numString = ""
    while inteiro >= 2:
        restoNum = inteiro%2
        numString += str(restoNum)
        inteiro = int(inteiro)//2
    if inteiro > 0:
        numString += str(inteiro)
    return numString[::-1]

def decOct(numero):
    inteiro = int(numero)
    numString = ""
    while inteiro >= 8:
        restoNum = inteiro%8
        numString += str(restoNum)
        inteiro = int(inteiro)//8
    if inteiro > 0:
        numString += str(inteiro)
    return numString[::-1]

#decDec já tem ali em cima

#esse aqui é delicado, eu preciso reconverter os numeros a cada loop
def decHex(numero):
    inteiro = int(numero)
    numString = ""
    while inteiro >= 16:
        restoNum = inteiro%16 #aqui entra o diferente desse numero
        if restoNum > 9:
            if restoNum == 10:
                restoNum = "A"
            if restoNum == 11:
                restoNum = "B"
            if restoNum == 12:
                restoNum = "C"
            if restoNum == 13:
                restoNum = "D"
            if restoNum == 14:
                restoNum = "E"
            if restoNum == 15:
                restoNum = "F"
        numString += str(restoNum)
        inteiro = int(inteiro)//16
    if inteiro > 0:
        if inteiro == 10:
            inteiro = "A"
        if inteiro == 11:
            inteiro = "B"
        if inteiro == 12:
            inteiro = "C"
        if inteiro == 13:
            inteiro = "D"
        if inteiro == 14:
            inteiro = "E"
        if inteiro == 15:
            inteiro = "F"
        numString += str(inteiro)
    return numString[::-1]



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#A base virou função para poder ser alterada posteriormente
def escolherBase1():
    global Base1
    print("Selecione qual será sua base inicial: ")
    print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal")
    Base1 = input("Digite o numero correspondente a base: ")
    if Base1 == "1" or Base1 == "2" or Base1 == "3" or Base1 == "4":
        parte1()
    else:
        print("A base selecionada não está nas opcões")
        escolherBase1()

def escolherBase2():
    global Base2
    print("===========================================================================")
    print("Legal, agora digite para qual base voce quer levar: ")
    print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal 5) para voltar")
    print("============================================================================")
    print(" ")
    Base2 = input("Digite o numero correspondente a base: ")
    if Base2 == "5":
        escolherBase1()
    elif Base1 == "1" or Base1 == "2" or Base1 == "3" or Base1 == "4":
        parte2()
    else:
        print("A base selecionada não está nas opcões")
        escolherBase1()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#vou fazer varios prints por preguiça de ficar separando as frases no mesmo :)
def parte1():
    global primeiroNumero, parte
    parte = 1
    primeiroNum = input("Qual é o numero? (digite '0' para retornar): ")
    if primeiroNum == "0":
        escolherBase1()
    primeiroNumero = chamadorDeFunção(Base1, primeiroNum, parte)

def parte2():
    global segundoNumero, parte
    parte = 2
    segundoNumero = chamadorDeFunção(Base2, str(primeiroNumero), parte)



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#Deixarei separado a parte de bem vindo para rodar somente no inicio do sistema

escolherBase1()

#apenas um teste por hora. Todos os numeros estão convertendo para decimal
print(primeiroNumero, "(em decimal)")

escolherBase2()
print("Resposta: ", segundoNumero)
# #segundoNumero = resposta
