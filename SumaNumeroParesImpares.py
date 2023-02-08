"""
Diseñar un programa que solicite un número entero positivo
y retorne la suma de los números pares y retorne la suma de 
los números impares, de acuerdo al rango indicado por el usuario,
si el número indicado por el usuario es menor que cero salir del programa.
"""
print("Digite un Numero entero y positivo ")
Numero=int(input())
i=0
sumaPar=0
sumaImpar=0
while Numero!=i:
    i=i+1
    if i % 2 == 0:
        sumaPar=sumaPar+i        
    else:
        sumaImpar=sumaImpar+i       
print("La sumatoria de los Impares es: "+str(sumaImpar))
print("La sumatoria de los pares es: "+str(sumaPar))
        