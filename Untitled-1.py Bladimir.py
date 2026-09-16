nota1 = float(input("ingrse la primera nota"))
nota2 = float(input("ingrese la segunda nota"))
nota3 = float(input("ingrese la tercera nota"))

promedio = (nota1 + nota2 + nota3) / 3
if promedio > 0 and promedio < 2.9:
    print("reprovado")
elif promedio >= 3.0 and promedio < 3.9:
    print("aceptable")
elif promedio > 4.0 and promedio < 4.5:
    print("bueno")
elif promedio >= 4.6 and promedio < 5.0:
    print("excelente")
