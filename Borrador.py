#Crear una aplicacion que se centre en la organizacion de gastos a traves del sistema 50-30-20.
#•	50% para necesidades esenciales, como vivienda, alimentación y transporte.
#•	30% para deseos o gastos personales, como entretenimiento o compras no esenciales.
#•	20% para ahorro o pago de deudas.

#Paso numero uno: Preguntarle al cliente/usuario, la cantidad de dinera que el posee 
#Paso numero dos: Dividir esos gastos en el sistema
#Paso numero tres: Definir en que distribuira exactamente su dinero en cada seccion 

"""Sueldo=float(input("Ingrese la cantidad de dinero que usted posee: "))
print("La distribucion esta dada por: \n 50% para necesidades esenciales, como vivienda, alimentación y transporte. \n 30% para deseos o gastos personales, como entretenimiento o compras no esenciales. \n 20% para ahorro o pago de deudas.")

distribucion=True
while distribucion is True:
    eleccion=int(input("Digite la opcion a elegir (1-3): "))
    if eleccion == 1:
        print()"""
        
print("Bienvenido/a a PapoiMoney \n Descubre la forma más inteligente y sencilla de manejar tu dinero con el sistema 50-30-20: \n 50% para Necesidades Esenciales (vivienda, comida, transporte). \n 30% para Deseos (entretenimiento, gastos personales). \n 20% para Ahorro. \n Automatiza tu presupuesto, evita gastos innecesarios y toma el control de tu bienestar financiero. ¡Comencemos a planificar!")
Sueldo = float(input("Para empezar ingrese la cantidad de dinero que posee: $"))

Necesidades = []
Deseos = []
Ahorro = []

distribucion=True
while distribucion is True:
    sección = int(input("Secciones: \n 1. Necesidades Esenciales (ej. vivienda, comida, transporte), \n 2. Deseos (entretenimiento, gastos personales). \n 3. Ahorro \n 4. Salir \n Digite la sección a la que desea entrar: "))
    if sección == 4:
        distribucion = False
    elif sección == 1:
            elección = int(input(" \n 1.Agregar categorías, \n 2.Consular categorías, \n 3.Modificar categorías, \n 4. Borrar categorías "))
            if elección == 1:
                Necesidades.append("Ingrese la categoría a agregar: ")
            elif elección == 2:
                print(Necesidades)
            elif elección == 3:
            # nuevo = input("Digite el nombre nuevo: ")
                if len(Necesidades) == 0:
                 print("Actualmente no hay categorías en Necesidades")
            else:
                for v in range(len(Necesidades)):
                    print(f"Actualmente hay {len(Necesidades)} en Necesidades")