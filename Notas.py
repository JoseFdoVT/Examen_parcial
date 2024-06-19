def capturar_notas():
    
    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")
    notas = []

    
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Por favor, ingrese un valor numérico.")

   
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas del estudiante {nombre} con matrícula {matricula} es: {promedio:.2f}")

def main():
    
    while True:
        capturar_notas()
        otra_vez = input("¿Desea ingresar otro estudiante? (sí/no): ").strip().lower()
        if otra_vez != 'sí':
            print("Gracias por usar el sistema.")
            break

if __name__ == "__main__":
    main()

