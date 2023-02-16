#calculadora basica em python
#funções da calculadora
def soma(x,y):
    return int(x) + int(y)
def sub(x,y):
    return int(x) - int(y)
def mult(x,y):
    return int(x) * int(y)
def div(x,y):
    return int(x) / int(y)

#Seleção da Operação que vai ser aplicada
print("Bem-vindo a Calculadora em python, nela realizamos as seguintes operações : ")
print(" -Soma")
print(" -Subtração")
print(" -Multiplicação")
print(" -Divisão")

tipoOp = input("Digite o tipo de operação : ")


if tipoOp == "soma" or tipoOp == "Soma":
   n1 =  input("Digite o primeiro numero ")
   n2 =  input("Digite o segundo numero ")
   result = soma(n1,n2)
   print("Resultado da " + tipoOp + " : " + str(result))
elif tipoOp == "subtração" or tipoOp == "Subtração" or tipoOp == "sub":
   n1 =  input("Digite o primeiro numero ")
   n2 =  input("Digite o segundo numero ")
   result = sub(n1,n2)
   print("Resultado da " + tipoOp + " : " + str(result))
elif tipoOp == "multiplicação" or tipoOp == "Multiplicação" or tipoOp == "mult":
   n1 =  input("Digite o primeiro numero ")
   n2 =  input("Digite o segundo numero ")
   result = mult(n1,n2)
   print("Resultado da " + tipoOp + " : " + str(result))
elif tipoOp == "divisão" or tipoOp == "Divisão" or tipoOp == "div":
   n1 =  input("Digite o primeiro numero ")
   n2 =  input("Digite o segundo numero ")
   result = div(n1,n2)
   print("Resultado da " + tipoOp + " : " + str(result))
