#Quando preciso que o programa entenda que é uma palavra, eu coloco entre aspas ""
#STR significa string/texto
import math

nome = "Bianca"
idade = 25.1
professora =  True
a = 1
b = -5
c = 1
delta = b*b - 4*a*c
if delta <0:
    print("Não existe raizes")
elif delta ==0:
    x = -b/(2*a)
    print(f"A raiz da equação é: {x}")

def equacao2grau(a, b, c): 
    x1 = -b + math.sqrt(b*b - 4*a*c)/(2*a)
    return x1

def equacao2grau2(a,b,c):
    x2 = -b - math.sqrt(b*b - 4*a*c)/(2*a)
    return x2 


print(f"O resultado de x1 é: {equacao2grau(a, b, c)} e o resultado e x2 é: {equacao2grau2(a,b,c)}")


#PARA IMPORTAR VALORES DE VARIAVEIS DENTRO DO PYTHON, 