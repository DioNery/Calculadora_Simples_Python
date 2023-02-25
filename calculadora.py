#calculadora basica em python
#funções da calculadora
def soma():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    soma = 0
    if quant < 1 :
        return print("Não é possível criar uma operação com apenas um número.")
    else :
        while cont <= quant:
            visor = cont + 1
            valores.append(int(input("Digite o " + str(visor)+"° valor : "))) 
            soma = soma + valores[cont]
            if cont == (quant - 1):
                return soma
            else:
                cont = cont + 1
def sub():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    sub = 0
    soma = 0
    valorMa = 0
    if quant < 1 :
        return print("Não é possível criar uma operação com apenas um número.")
    else :
        while cont <= quant:
            visor = cont + 1
            valores.append(int(input("Digite o " + str(visor)+"° valor : "))) 
            if cont == 0:
                valorMa = valores[cont]
                soma = 0
            else :
                soma = soma + valores[cont]
                sub = valorMa - soma
            if cont == (quant - 1):
                return sub
            else:
                cont = cont + 1
def mult():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    mult = 1
    if quant < 1 :
        return print("Não é possível criar uma operação com apenas um número.")
    else :
        while cont <= quant:
            visor = cont + 1
            valores.append(int(input("Digite o " + str(visor)+"° valor : "))) 
            mult = mult * valores[cont]
            if cont == (quant - 1):
                return mult
            else:
                cont = cont + 1
def div():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    div = 1
    primeiroV = 1
    mult = 1
    if quant < 1 :
        return print("Não é possível criar uma operação com apenas um número.")
    else :
        while cont <= quant:
            visor = cont + 1
            valores.append(float(input("Digite o " + str(visor)+"° valor : "))) 
            if cont == 0:
                div = valores[cont]
            if cont == 1 :
                primeiroV = valores[cont]
                div = div/valores[cont]
            if cont > 1:
                mult = mult * valores[cont]
                div = div/mult
            if cont == (quant - 1):
                return div
            else:
                cont = cont + 1
def repet(respostaF):
 resp = str(respostaF)
 if resp == "não" or resp == "Não" or resp == "N" or resp == "n":
      return print("Obrigado por usar a calculadora.")
 else: 
  tipoOp = input("Digite o tipo de operação : ")
 if tipoOp == "soma" or tipoOp == "Soma":
         result = soma()
         print("Resultado da " + tipoOp + " : " + str(result))
         respF = input("Você deseja fazer mais alguma operação? ")
         return repet(respF)
 elif tipoOp == "subtração" or tipoOp == "Subtração" or tipoOp == "sub":
         result = sub()
         print("Resultado da " + tipoOp + " : " + str(result))
         respF = input("Você deseja fazer mais alguma operação? ")
         return repet(respF)  
 elif tipoOp == "multiplicação" or tipoOp == "Multiplicação" or tipoOp == "mult":
         result = mult()
         print("Resultado da " + tipoOp + " : " + str(result))
         respF = input("Você deseja fazer mais alguma operação? ")
         return repet(respF)  
 elif tipoOp == "divisão" or tipoOp == "Divisão" or tipoOp == "div":
         result = div()
         print("Resultado da " + tipoOp + " : " + str(result))
         respF = input("Você deseja fazer mais alguma operação? ")
         return repet(respF)
 else:
         print("Nenhuma Operação selecionada ou não entendida.")
#Seleção da Operação que vai ser aplicada
print("Bem-vindo a Calculadora em python, nela realizamos as seguintes operações : ")
print(" -Soma")
print(" -Subtração")
print(" -Multiplicação")
print(" -Divisão")
tipoOp = input("Digite o tipo de operação : ")
if tipoOp == "soma" or tipoOp == "Soma":
   result = soma()
   print("Resultado da " + tipoOp + " : " + str(result))
   respF = input("Você deseja fazer mais alguma operação? ")
   repet(respF)
elif tipoOp == "subtração" or tipoOp == "Subtração" or tipoOp == "sub":
   result = sub()
   print("Resultado da " + tipoOp + " : " + str(result))
   respF = input("Você deseja fazer mais alguma operação? ")
   repet(respF)
elif tipoOp == "multiplicação" or tipoOp == "Multiplicação" or tipoOp == "mult":
   result = mult()
   print("Resultado da " + tipoOp + " : " + str(result))
   respF = input("Você deseja fazer mais alguma operação? ")
   repet(respF)
elif tipoOp == "divisão" or tipoOp == "Divisão" or tipoOp == "div":
   result = div()
   print("Resultado da " + tipoOp + " : " + str(result))
   respF = input("Você deseja fazer mais alguma operação?  ")
   repet(respF)
else:
   print("Erro ao digitar o tipo de Operação.")