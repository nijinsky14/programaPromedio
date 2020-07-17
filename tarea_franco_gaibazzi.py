nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")
def notas():
    nota1 = int(input("Ingrese la nota de Matemática: "))
    nota2 = int(input("Ingrese la nota de Literatura: "))
    nota3 = int(input("Ingrese la nota de Fisica: "))
    return nota1 + nota2 + nota3

suma = notas()
promedio = (suma / 3)

if promedio >= 6 and promedio < 9:
    print("El promedio del alumno "+ nombre + " " + apellido + " es: Aprobado " + "/ " + str(promedio))
elif promedio < 4:
    print("El promedio del alumno "+ nombre + " " + apellido + " es: Insuficiente " + "/ " + str(promedio))
elif promedio >= 4 and promedio < 6:
    print("El promedio del alumno "+ nombre + " " + apellido + " es: A Recuperatorio " + "/ " + str(promedio))  
elif promedio <= 9:
    print("El promedio del alumno "+ nombre + " " + apellido + " es: Alumno Destacado " + "/ " + str(promedio))       
else:
    print("Valor invalido")









