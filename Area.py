x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
pi = 3.14159;
rectangled = (a*c)/2
circle = pi*(c*c)
trapezium = ((a+b)*c)/2
square = b*b
rectangle = a*b
print('TRIANGULO: %.3f' %rectangled)
print('CIRCULO: %.3f' %circle)
print('TRAPEZIO: %.3f' %trapezium)
print('QUADRADO: %.3f' %square)
print('RETANGULO: %.3f' %rectangle)