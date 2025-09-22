import math
def rectangulo(base, altura):
	area = base * altura
	perimetro = 2 * (base + altura)
	return area, perimetro 

def circulo(radio):
	area = 3.1416 * (radio)*(radio)
	perimetro = 3.1416 * (2*radio)
	return area, perimetro
def triangulo(base, altura):
    area = 0.5 * base * altura
    hipotenusa = math.sqrt((base)*(base) + (altura)*(altura))
    perimetro = base + altura + hipotenusa
    return area, perimetro
