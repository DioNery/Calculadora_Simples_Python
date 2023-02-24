#calculadora basica em python
#funções da calculadora

def soma():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    soma = 0
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
    while cont <= quant:
        visor = cont + 1
        valores.append(int(input("Digite o " + str(visor)+"° valor : "))) 
        if cont == 1:
            sub = valores[cont] - valores[cont]
        if cont == (quant - 1):
            return sub
        else:
            cont = cont + 1
def mult():
    quant = int(input("Digite a quantidade de numeros : "))
    valores = []
    cont = 0
    mult = 1
    while cont <= quant:
        visor = cont + 1
        valores.append(int(input("Digite o " + str(visor)+"° valor : "))) 
        mult = mult * valores[cont]
        if cont == (quant - 1):
            return mult
        else:
            cont = cont + 1
def div(x,y):
    return int(x) / int(y)

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
         n1 =  input("Digite o primeiro numero : ")
         n2 =  input("Digite o segundo numero : ")
         result = div(n1,n2)
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
   n1 =  input("Digite o primeiro numero : ")
   n2 =  input("Digite o segundo numero : ")
   result = div(n1,n2)
   print("Resultado da " + tipoOp + " : " + str(result))
   respF = input("Você deseja fazer mais alguma operação?  ")
   repet(respF)
else:
   print("Erro ao digitar o tipo de Operação.")