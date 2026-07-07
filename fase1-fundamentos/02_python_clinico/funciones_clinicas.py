def calcular_imc(peso_kg, altura_m):
    imc = peso_kg / (altura_m ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return round(imc, 1), categoria


def calcular_TA(presion_sist, presion_diast):
    if presion_sist <= 0 or presion_diast <= 0:
        return None, None, "Error: valores deben ser mayores a cero"
    if presion_sist < 120 and presion_diast < 80:
        categoria = "Normal"
    elif presion_sist < 130 and presion_diast < 80:
        categoria = "Elevada"
    elif presion_sist < 140 or presion_diast < 90:
        categoria = "Hipertension grado 1"
    else:
        categoria = "Hipertension grado 2"
    return presion_sist, presion_diast, categoria
from funciones_clinicas import calcular_TA

