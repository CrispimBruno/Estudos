#Calculadora de bases feita inteiramente em python

#Vou fazer a calculadora com 2 partes principais, a primeira vai ser transformar a base atual na base 10, depois vou trasnformar essa base 10 na desejada. Meu foco vai ser colocar uma tela para literalmente virar uma calculadora, mas por hora vai ser no terminal
#os nomes das funções vão ser diretamente relacionadas a base, porém resumidas

#primeiro uma função que chama outra função (definidor da base)
def chamadorDeFunção ():
    if Base1 == 1:
        return binDec(primeiroNum)
    elif Base1 == 2:
        return octDec(primeiroNum)
    elif Base1 == 3:
        return decDec (primeiroNum)
    elif Base1 == 4:
        return hexDex (primeiroNum)
    


def binDec(primeiroNum): {
    #Binario para decmal, aqui vamos fazer uma conta simples. Vou percorrer o numero em binario e para cada casa, irei fazer o numero x 2^index invertido
    #primeiro um verificador, para definir se o numero é ou não binario
    for i in range(primeiroNum){
        if i =! 0 or i=! 1{
            print("Seu numero não é binario, por favor digite outro")
            primeiroNum = int(input("Qual é o numero?: "))
        }
    }

}

#vou fazer varios prints por preguiça de ficar separando as frases no mesmo :)
print("===========================================================================")
print("Olá, bom vindo(a) à calculadora de bases! Selecione qual será sua base inicial: ")
print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal")
print("============================================================================")
Base1 = int(input("Digite o numero correspondente a base: "))
primeiroNum = int(input("Qual é o numero?: "))
Numero = chamadorDeFunção()

print("===========================================================================")
print("Legal, agora digite a base correspondente ao segundo numero: ")
print("1) Binario  2) Octal  3) Decimal 4) Hexadecimal")
print("============================================================================")