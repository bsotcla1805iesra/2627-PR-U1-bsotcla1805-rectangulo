def calcular_medidas(base: float, altura: float):
    """
    Calcula el área y el perímetro

    :param base: Base del rectángulo
    :param altura: Altura del rectángulo

    :return: Devuelve el área y el perímetro
    """
    area: float = base * altura
    perimetro: float = 2 * (base + altura)

    return area, perimetro
    
def determinar_forma(base: float, altura: float):
    """
    Determina la forma del rectángulo

    :param base: Base del rectángulo
    :param altura: Altura del rectángulo
    
    :return: Devuelve la forma del rectángulo
    """
    if base == altura:
        return str("Cuadrado")
    if base > altura:
        return str("Horizontal")
    if base < altura:
        return str("Vertical")

def main():
    base: float = float(input("Introduce la base del rectángulo en cm: "))
    while base < 0 or base == 0:
        print("Introduce un valor mayor que 0")
        base: float = float(input("Introduce la base del rectángulo en cm: "))
    altura: float = float(input("Introduce la altura del rectángulo en cm: "))
    while altura < 0 or altura == 0:
            print("Introduce un valor mayor que 0")
            altura: float = float(input("Introduce la altura del rectángulo en cm: "))
    resultado = calcular_medidas(base, altura)
    forma = determinar_forma(base, altura)
    print(f"Forma: {forma}")
    print(f"Área: {resultado[0]} cm²")
    print(f"Perímetro: {resultado[1]} cm")

if __name__ == "__main__":
    main()