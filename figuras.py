import math
def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro 

def triangulo(base, altura):
    area = 0.5 * base * altura
    hipotenusa = (base**2 + altura**2)**0.5
    perimetro = base + altura + hipotenusa
    return area, perimetro

def circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro
