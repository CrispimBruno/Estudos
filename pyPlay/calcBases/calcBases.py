#Calculadora de bases feita inteiramente em python SEM IA, só eu

#Vou fazer a calculadora com 2 partes principais, a primeira vai ser transformar a base atual na base 10, depois vou trasnformar essa base 10 na desejada. Meu foco vai ser colocar uma tela para literalmente virar uma calculadora, mas por hora vai ser no terminal
#os nomes das funções vão ser diretamente relacionadas a base, porém resumidas

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#primeiro uma função que chama outra função (definidor da base)

def chamadorDeFunção(base1, numero):
    if Base1 == "1":
        verificador = verificadorBin(numero)
        if verificadorBin:
            return binDec(numero)
        else: 
            print("O numero digitado está errado. Por favor tente novamente")
            parte1()
    elif Base1 == "2":
        verificador = verificadorOct(numero)
        if verificadorOct:
            return octDec(numero)
        else: 
            print("O numero digitado está errado. Por favor tente novamente")
            parte1()
    elif Base1 == "3":
        verificador = verificadorDec(numero)
        if verificadorDec:
            return decDec (numero)  
        else: 
            print("O numero digitado está errado. Por favor tente novamente")
            parte1()
    elif Base1 == "4":
        verificador = verificadorHex(numero)
        if verificadorHex:
            return hexDex (numero)
        else: 
            print("O numero digitado está errado. Por favor tente novamente")
            parte1()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#primeiro um verificador, para definir se o numero é ou não da base indicada
def verificadorBin(numero):
    for i in range(numero):
        if numero[i] - 1 >= -1 and i+1 <= 2:
            pass
        else: 
            return False
    return True

def verificadorOct(numero):
    for i in range(Numero):
        if numero[i]-1 >= -1 and i + 1 <= 8:
            pass
        else:
            return false
    return True

def verificadorDec(numero):
    for i in range(numero):
        if numero[i].type == int:
            pass
        else: 
            return False
    return True

def verificadorHex(numero):
    for i in range(numero):
        if numero[i].isdigit():
            pass
        elif ord(numero[i].upper()) >=65 and ord(numero[i].upper()) <=70:
            pass
        else: 
            return False
    return True

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#Binario para decmal, aqui vamos fazer uma conta simples. Vou percorrer o numero em binario e para cada casa, irei fazer o numero x 2^index invertido         
def binDec(primeiroNum): 
    decimal = 0
    for i in range(primeiroNum):
        decimal += int(primeiroNum[i-1])*(2**(i-1))
    return decimal



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

def escolherBase2():
    global Base2
    print("Selecione qual será sua base inicial: ")
    print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal")
    Base2 = input("Digite o numero correspondente a base: ")
    if Base2 == "1" or Base2 == "2" or Base2 == "3" or Base2 == "4":
        parte2()
    else:
        print("A base selecionada não está nas opcões")

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#vou fazer varios prints por preguiça de ficar separando as frases no mesmo :)
def parte1():
    global primeiroNumero
    primeiroNum = input("Qual é o numero? (digite '0' para retornar: ")
    if primeiroNum == "0":
        escolherBase1()
    primeiroNumero = chamadorDeFunção1(Base1, primeiroNum)

def parte2():
    global segundoNumero
    print("===========================================================================")
    print("Legal, agora digite a base correspondente ao segundo numero: ")
    print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal 5) para voltar")
    print("============================================================================")
    segundoNum = input("Qual é o numero? (digite '0' para retornar: ")
    if segundoNum == "0":
        escolherBase2()
    elif segundoNum == "5":
        escolherBase1()
    segundoNumero = chamadorDeFunção(Base2, segundoNum)



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

#Deixarei separado a parte de bem vindo para rodar somente no inicio do sistema

print("===========================================================================")
print("Olá, bom vindo(a) à calculadora de bases! Selecione qual será sua base inicial: ")
print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal")
print("============================================================================")
escolherBase1()
escolherBase2()