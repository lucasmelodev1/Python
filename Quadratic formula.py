import math

def calcularDelta(a,b,c):
    delta=b**2-4*a*c
    return delta
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
calcularDelta(a,b,c)
def calcularBhaskara(a,b):
    x1=(-b+math.sqrt(calcularDelta(a,b,c)))/(2*a)
    x2=(-b-math.sqrt(calcularDelta(a,b,c)))/(2*a)
    return x1, x2
print(calcularDelta(a,b,c))
if calcularDelta(a,b,c) >=0:
    print(calcularBhaskara(a,b))
elif calcularDelta(a,b,c) <0:
    print("Não possui raízes reais")
