import os
os.system("cls")



menu = '''

        menu
1.-Grabar
2.-Buscar
3.-Listar
4.-Salir

'''
contSobre = 0
contPaq = 0
listaRut = []
listaEncom = []
listaNombre = []
listaPeso = []
listaPrecio = []
listaCiudad = []




def grabarDatos():
    while True:
        try:
            tipoEncom=input("5.- sobre" "\n6.-paquete\n")
            if tipoEncom == 5:
                listaEncom.append("SOBRE")
                contSobre = contSobre +1
                break
            elif tipoEncom == 6:
                listaEncom.append("PAQUETE")
                contPaq = contPaq +1
                break
            else:
                print("error de rango1")
        except:
            print("ha ocurrido una excepcion")
#fin while tipo paquete
    while True:
        try:
            nuevoNomDest = input("ingresa nombre : ")
            if len(nuevoNomDest) >=2 and len(nuevoNomDest) <=30:
                listaNombre.append(nuevoNomDest.upper())
                break
            else:
                ("error de nombre")
        except:
            print("ha ocurrido una excepcion")

#fin while nombre

    while True:
        try:
            NuevoRut = input("ingresa rut: ")
            if len(NuevoRut) >= 9 and NuevoRut[-2] == "-":
                listaRut.append(NuevoRut)
                break
            else:
                print("error de rut")
        except:
            print("ha ocurrido una excepcion")
 #fin while rut y validacion

    while True:
        try:
            PesoProducto=float(input("Cuanto pesa :"))
            if PesoProducto >= 0.1:
                listaPeso.append(PesoProducto)
                break
            else:
                print("peso no valido")

        except:
            print("ha ocurrido una excepcion")
#fin while peso producto

    while True:
        try:
            precioEncom = int(input("PRECIO: "))
            if precioEncom >= 2000:
                listaPrecio.append(precioEncom)
                break
            else:
                print("error en rango2")
        except:
            print("ha ocurrido una excepcion")
#fin while precio
    while True:
        try:
            nuevaCiudad =input("ingrese ciudad: ")
            if len(nuevaCiudad) >= 3:
                listaCiudad.append(nuevaCiudad.upper())
                break
            else:
                print("error de rango , minimo 3 caracteres")
        except:
            print("ha ocurrido una excepcion")

#fin while ciudad destino


def buscarEncomienda ():
    print("opcion 2 - buscar encomienda")
    buscarXrut = (input("ingresa rut a buscar: "))
    print()
    print("             LISTADO            ")
    for i in range(len(listaRut)):
        if buscarXrut == listaRut[i]:
            print("    RUT   | TIPO DE ENCOM      |  NOM DESTINATARIO   |  PESO      | PRECIO        |CIUDAD DESTINO")
            print()
            print("----------+--------------------+---------------------+------------+---------------+-----------------+")
            print(f"{listaRut[i]:10s}, {listaEncom[i]:8s}, {listaNombre[i]:20s}, {listaPeso[i]:5d},{listaPrecio[i]:7d} {listaCiudad[i]:20s}")

#fin buscar por rut encomienda

def listarEncomienda():
    print("opcion 3 - listar encomienda")
    print("                                         LISTADO GENERAL                                                         ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("    RUT   | TIPO DE ENCOM      |  NOM DESTINATARIO   |  PESO      | PRECIO        |CIUDAD DESTINO")
    for i in range(len(listaRut)):
        print()
        print("----------+--------------------+---------------------+------------+---------------+-----------------+")
        print(f"{listaRut[i]:10s}, {listaEncom[i]:8s}, {listaNombre[i]:20s}, {listaPeso[i]:5d}, {listaCiudad[i]:20s}")
        print()
        print(f"La cantidad de Sobres es : {contSobre}, la cantidad de paquetes es : {contPaq}")


#fin listar encomiendas


#comienzo menu main()



while True:
    try:
        opc =int((input(menu)))
        if opc == 4:
            break
        elif opc == 1:
            grabarDatos()
        elif opc == 2:
            buscarEncomienda()
        elif opc == 3:
            listarEncomienda()
        else:
            print("error de rango3")
    except:
        print("ha ocurrido una excepcion")