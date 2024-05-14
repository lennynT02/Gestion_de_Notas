# ----------------------------------------------------------------------------------------
def login(user, pasw):
    while True:
        user1 = str(input("USUARIO: "))
        pasw1 = str(input("CONTRASEÑA: "))
        if user1 != user:
            print("\nUsuario Incorrecto")
        elif pasw1 != pasw:
            print("\nContraseña Incorrecta")
        else:
            return user1

def menu(opciones, mensaje):
    while True:
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}.- {opcion}")
        opcion = int(input(mensaje))
        if 1 <= opcion <= len(opciones):
            return opcion
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar():
    seguir = "si"
    while seguir == "si":
        id_estudiante = random.randint(1000, 9999)
        while any(estudiante["id"] == id_estudiante for estudiante in estudiantes):
            id_estudiante = random.randint(1000, 9999)

        nombre_estudiantes = input("\nIngrese los Datos del Estudiante\n\nNOMBRE: ")
        apellido_estudiante = input("APELLIDO: ")
        correo = input("CORREO: ")

        while True:
            nota1 = input("NOTA 1: ")
            nota2 = input("NOTA 2: ")
            if nota1.isdigit() and nota2.isdigit():
                nota1 = float(nota1)
                nota2 = float(nota2)
                if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                    break
                else:
                    print("\n!!Fuera del Limite!!")
                    print("!!Notas sobre (10)!!\n" if nota1 > 10 or nota2 > 10 else "")
                    print("!!Notas menores (0)!!\n" if nota1 < 0 or nota2 < 0 else "")
            else:
                print("\nValor ingresado !INCORECTO!\nIngresar un numero entre (0-10)\n")

        estudiante = {
            "id": id_estudiante,
            "nombre": nombre_estudiantes,
            "apellido": apellido_estudiante,
            "correo": correo,
            "nota1": round(nota1, 2),
            "nota2": round(nota2, 2),
            "total": round((nota1 + nota2), 2),
        }

        for key, value in estudiante.items():
            estudiante_txt[key].append(value)

        estudiantes.append(estudiante) 

        seguir = ""
        while seguir not in ["no", "si"]:
            seguir = input("\nDesea ingresar otro estudiante(si/no): ").lower()

    with open("reportes.txt", "w") as reporte:
        data = pd.DataFrame(estudiante_txt)
        reporte.write(f"COLEGIO O UNIVERSIDAD: {docente['unidad_educativa']}\nANIO LECTIVO O SEMESTRE: {docente['anio_lectivo']}")
        reporte.write(f"\nDOCENTE: {docente['nombre']}\nMATERIA: {docente['materia']}\n{data[1:]}")

    total = sum(estudiante["total"] for estudiante in estudiantes)
    con = len(estudiantes)
    con_aprobados = sum(1 for estudiante in estudiantes if 14 <= estudiante["total"] <= 20)
    con_suspenso = sum(1 for estudiante in estudiantes if 9 <= estudiante["total"] <= 13)
    con_reprobados = sum(1 for estudiante in estudiantes if 1 <= estudiante["total"] <= 8)

    with open("calificaciones.txt", "w") as calificaciones:
        calificaciones.write(
            f"\t\t\t\t\t\t\t\tCOLEGIO O UNIVERSIDAD: {docente['unidad_educativa']}"
            f"\n\t\t\t\t\t\t\t\t\tREPORTE DE CALIFICACIONES\n\nAño lectivo o Semestre: {docente['anio_lectivo']}"
            f"\nMateria: {docente['materia']}\n\n{data[1:]}"
            f"\n\nRESUMEN\nPromedio del curso: {round((total / con), 2)}"
            f"\n*Aprobados (14-20): {con_aprobados}"
            f"\n*Suspenso (09-13): {con_suspenso}"
            f"\n*Reprobados (01-08): {con_reprobados}"
            f"\n\n\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\tDocente\n\t\t\t\t\t\t\t\t\t\t{docente['nombre']}"
        )
# ------------------------------------------------------------------------------------
def almacenar_mostrar(estudiantes, opcion2):
    metodo = " "
    if opcion2 == 1:
        metodo = "Burbuja"
    elif opcion2 == 2:
        metodo = "Insercion"
    elif opcion2 == 3:
        metodo = "Seleccion"
    elif opcion2 == 4:
        metodo = "MergeSort"
    elif opcion2 == 5:
        metodo = "QuickSort"
    ordenado = {
        "    ID": [1],
        "Nombre": [1],
        "Apellido": [1],
        "Correo": [1],
        "Nota 1": [1],
        "Nota 2": [1],
        "Total": [1],
    }
    for estudiante in estudiantes:
        ordenado["Nombre"].append(estudiante.get("nombre", ""))
        ordenado["    ID"].append(estudiante.get("id", ""))
        ordenado["Apellido"].append(estudiante.get("apellido", ""))
        ordenado["Correo"].append(estudiante.get("correo", ""))
        ordenado["Nota 1"].append(estudiante.get("nota1", ""))
        ordenado["Nota 2"].append(estudiante.get("nota2", ""))
        ordenado["Total"].append(estudiante.get("total", ""))
    with open("ordenamiento.txt", "w") as ordenamiento:
        data1 = pd.DataFrame(ordenado)
        ordenamiento.write(
            "\t\t\t\t\t\t\t\tCOLEGIO O UNIVERSIDAD: "
            + docente["unidad_educativa"]
            + "\n\t\t\t\t\t\t\t\t\tREPORTE DE CALIFICACIONES\n\nCalificaciones Ordenadas\n\nALGORITMO: "
            + str(metodo)
            + " \n\n"
            + str(data1[1:])
            + "\n\n\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\tDocente\n\t\t\t\t\t\t\t\t\t\t"
            + docente["nombre"]
        )
    ##MOSTRAR ARCHIVO
    with open("ordenamiento.txt", "r") as ordenamiento:
        contenido = ordenamiento.read()
        print(contenido)

# FUNCIONES DE ORDENAR---------------------------------------------------------------------
def funciones_ordenamiento(algoritmo):
    if algoritmo == 1:
        for i in range(len(estudiantes)):
            for j in range(len(estudiantes) - 1):
                if estudiantes[j]["total"] > estudiantes[j + 1]["total"]:
                    temporal = estudiantes[j]
                    estudiantes[j] = estudiantes[j + 1]
                    estudiantes[j + 1] = temporal

    elif algoritmo == 2:
        for i in range(1, len(estudiantes)):
            valor_arreglar = estudiantes[i]
            j = i - 1
            while j >= 0 and valor_arreglar["total"] < estudiantes[j]["total"]:
                estudiantes[j + 1] = estudiantes[j]
                j -= 1
            estudiantes[j + 1] = valor_arreglar

    elif algoritmo == 3:
        for i in range(len(estudiantes)):
            menor = estudiantes[i]["total"]
            ind_me = i
            for j in range(i + 1, len(estudiantes)):
                if estudiantes[j]["total"] < menor:
                    menor = estudiantes[j]["total"]
                    ind_me = j
            tem = estudiantes[i]
            estudiantes[i] = menor
            estudiantes[ind_me] = tem

    elif algoritmo == 4:
        mergesort(estudiantes)
    elif algoritmo == 5:
        quicksort(estudiantes)

##MERGESORT
def mergesort(estudiantes):
    if len(estudiantes) == 1:
        return estudiantes
    else:
        # DIVIDIR ARREGLO-----round(len(arreglo/2),0)
        indice_medio = len(estudiantes) // 2
        indice_medio = int(indice_medio)
        mitad_izquierda = estudiantes[:indice_medio]
        mitad_derecha = estudiantes[indice_medio:]
        mitad_izquierda = mergesort(mitad_izquierda)
        mitad_derecha = mergesort(mitad_derecha)
        return combinar(mitad_izquierda, mitad_derecha)

def combinar(izquierda, derecha):
    resultado = []
    indice_izq = 0
    indice_der = 0
    # COMPARAR
    while indice_izq < len(izquierda) and indice_der < len(derecha):
        if izquierda[indice_izq]["total"] > derecha[indice_der]["total"]:
            resultado.append(izquierda[indice_izq])
            indice_izq += 1
        else:
            resultado.append(derecha[indice_der])
            indice_der += 1
    ##Agregar Faltantes
    if indice_der == len(derecha):
        resultado.extend(izquierda[indice_izq:])
    else:
        resultado.extend(derecha[indice_der:])

    return resultado

def quicksort(estudiantes):
    if len(estudiantes) <= 1:
        return estudiantes
    else:
        # Seleccion del pivote
        pivoteo_dic = estudiantes[-1]
        pivoteo = pivoteo_dic["total"]

        # Creación de grupos
        menor = []
        mayor = []

        for estudiante in estudiantes[:-1]:
            if estudiante["total"] < pivoteo:
                menor.append(estudiante)
            else:
                mayor.append(estudiante)

        # Dividir en partes de manera recursiva
        menorcom = quicksort(menor)
        mayorcom = quicksort(mayor)

        return menorcom + [pivoteo_dic] + mayorcom

# -------------------------------------------------------------------------------------------
def almacenar_mostrar1(encontrado, opcion3, elemento_buscar, estudiantes):
    if encontrado:
        metodo = " "
        if opcion3 == 1:
            metodo = "Lineal"
        elif opcion3 == 2:
            metodo = "Binaria"
        elif opcion3 == 3:
            metodo = "Interpolacion"
        encontrado1 = {
            "    ID": [1],
            "Nombre": [1],
            "Apellido": [1],
            "Correo": [1],
            "Nota 1": [1],
            "Nota 2": [1],
            "Total": [1],
        }
        for estudiante in estudiantes:
            if estudiante["total"] == elemento_buscar:
                encontrado1["Nombre"].append(estudiante.get("nombre", ""))
                encontrado1["    ID"].append(estudiante.get("id", ""))
                encontrado1["Apellido"].append(estudiante.get("apellido", ""))
                encontrado1["Correo"].append(estudiante.get("correo", ""))
                encontrado1["Nota 1"].append(estudiante.get("nota1", ""))
                encontrado1["Nota 2"].append(estudiante.get("nota2", ""))
                encontrado1["Total"].append(estudiante.get("total", ""))
        with open("buscar.txt", "w") as encontrados:
            data3 = pd.DataFrame(encontrado1)
            encontrados.write(
                "\t\t\t\t\t\t\t\tCOLEGIO O UNIVERSIDAD: "
                + docente["unidad_educativa"]
                + "\n\t\t\t\t\t\t\t\t\tREPORTE DE CALIFICACIONES\n\nBusqueda de Calificaciones\n\nALGORITMO: "
                + str(metodo)
                + " \n\n"
                + str(data3[1:])
                + "\n\n\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\tDocente\n\t\t\t\t\t\t\t\t\t\t"
                + docente["nombre"]
            )
        with open("buscar.txt", "r") as encontrados:
            contenido = encontrados.read()
            print(contenido)
    else:
        print("El elemento no esta en la lista")

# FUNCIONES DE BUSCAR----------------------------------------------------------------------
def funciones_busqueda(opcion3, elemento_buscar):
    if opcion3 == 1:
        encontrado = False
        for i in range(len(estudiantes)):
            if elemento_buscar == estudiantes[i]["total"]:
                encontrado = True
        return encontrado
    elif opcion3 == 2:
        inicio = 0
        fin = len(estudiantes) - 1
        while inicio <= fin:
            indice_medio = (inicio + fin) // 2
            valor_medio = estudiantes[indice_medio]["total"]
            if elemento_buscar == valor_medio:
                return True
            elif elemento_buscar < valor_medio:
                fin = indice_medio - 1
            elif elemento_buscar > valor_medio:
                inicio = indice_medio + 1
        return False

    elif opcion3 == 3:
        inicio = 0
        fin = len(estudiantes) - 1
        while (
            inicio <= fin
            and estudiantes[inicio]["total"]
            <= elemento_buscar
            <= estudiantes[fin]["total"]
        ):
            indice_estimado = inicio + (
                (elemento_buscar - estudiantes[inicio]["total"])
                / (estudiantes[fin]["total"] - estudiantes[inicio]["total"])
            ) * (fin - inicio)
            indice_estimado = int(indice_estimado)
            valor_medio = estudiantes[indice_estimado]["total"]
            if elemento_buscar == valor_medio:
                return True
            elif elemento_buscar < valor_medio:
                fin = indice_estimado - 1
            elif elemento_buscar > valor_medio:
                inicio = indice_estimado + 1
    return True

# FUNCION DE ELIMINAR-----------------------------------------------------------------------
def eliminar(eliminado):
    print(estudiantes)
    encontrado=False
    elimina=None
    for i in range (len(estudiante_txt["    ID"])):
        if estudiante_txt["    ID"][i] == eliminado:
            print("hola")
            encontrado=True
            elimina=i
    if encontrado is False:
        print("Estudianto no Registrado")  
    else:
        
        estudiante_txt["    ID"].pop(elimina)
        estudiante_txt["Apellido"].pop(elimina)
        estudiante_txt["Correo"].pop(elimina)
        estudiante_txt["Nombre"].pop(elimina)
        estudiante_txt["Nota 1"].pop(elimina)
        estudiante_txt["Nota 2"].pop(elimina)
        estudiante_txt["Total"].pop(elimina)
        estudiantes.pop(elimina-1)
        print(elimina,"\n",estudiante_txt)
        with open("reportes.txt", "w") as reporte:
            data = pd.DataFrame(estudiante_txt)
            reporte.write("COLEGIO O UNIVERSIDAD: "+ docente["unidad_educativa"]+ "\nANIO LECTIVO O SEMESTRE: "+ docente["anio_lectivo"])
            reporte.write("\nDOCENTE: "+ docente["nombre"]+ "\nMATERIA: "+ docente["materia"]+ "\n"+ str(data[1:]))

# PROGRAMA PRINCIPAL---------------------------------------------------------------------------
# from tabulate import tabulate ------- Otra libreria para tabular mediante TUPLAS
import pandas as pd
import random
import os

user1 = "user@"
pasw1 = "1234"
estudiantes = []
opcion = 1
docente = {}
estudiante_txt = {
    "    ID": [1],
    "Nombre": [1],
    "Apellido": [1],
    "Correo": [1],
    "Nota 1": [1],
    "Nota 2": [1],
    "Total": [1],
}

opciones1 = ["Registrar Profesor", "Ordenar y Mostrar Calificaciones", "Buscar Calificacion", "Eliminar un estudiante", "Salir"]
opciones2 = ["Burbuja", "Insercion", "Seleccion", "MergeSort", "QuickSort", "Salir"]
opciones3 = ["Lineal", "Binaria", "Interpolacion", "Salir"]

mensaje = "\nElija una opcion: "

print("\tSISTEMA DE GESTIÓN DE CALIFICACIONES\n")
name_user = login(user1, pasw1)
indice_name = user1.find("@")
print("\nBienvenido ¡", user1[0:indice_name].upper(), "!")
while opcion != 5:
    opcion = menu(opciones1, mensaje)
    if opcion == 1:
        if len(docente) == 0:
            nombre_docente = input("Ingrese sus Datos\n\nNOMBRE Y APELLIDO: ")
            materia = input("MATERIA: ")
            unidad_educativa = input("COLEGIO O UNIVERSIDAD: ")
            grado = input("AÑO LECTIVO O SEMESTRE: ")
            docente = {
                "nombre": nombre_docente,
                "materia": materia,
                "unidad_educativa": unidad_educativa,
                "anio_lectivo": grado,
            }
        agregar()
        print(estudiante_txt)

    elif opcion == 2 and len(estudiantes) > 0:
        opcion2 = 1
        while opcion2 != 6:
            opcion2 = menu(opciones2, mensaje)
            funciones_ordenamiento(int(opcion2))
            if 1 <= opcion2 <= 5:
                almacenar_mostrar(estudiantes, int(opcion2))
            elif opcion2 > 6 or opcion2 < 1:
                print("Opcion Incorrecta")

    elif opcion == 3 and len(estudiantes) > 0:
        opcion3 = 1
        while opcion3 != 4:
            opcion3 = menu(opciones3, mensaje)
            if 1 <= opcion3 <= 3:
                elemento_buscar = float(input("Ingrese la Nota que desea buscar: "))
                respuesta = funciones_busqueda(int(opcion3), float(elemento_buscar))
                almacenar_mostrar1(respuesta, opcion3, elemento_buscar, estudiantes)
            elif opcion3 > 4 or opcion3 < 1:
                print("Opcion Incorrecta")
    elif opcion == 4:
        eliminado = int(input("Ingrese el ID del estudiante a eliminar: "))
        eliminar(eliminado)
    elif opcion != 5 and len(estudiantes) == 0:
        print("\nIngrese mas Estudiantes")
    elif opcion == 5:
        pass
    else:
        print("\nNo escojiste una opcion valida")
# --------------------------------------------------------------------------------------------------
