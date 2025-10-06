from main import *
def iniciar():
    while True:
        hacer=int(input("|||||Hola, Bienvenido a la pizzeria Luigi!||||| " \
        "\n-Que deseas hacer?" \
        "\n1. Comprar " \
        "\n2. Consultar" \
        "\n3. Salir" \
        "\n-Quiero: "))
    
        if hacer==1:
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            id_del_comprador=input("-Tienes algun id? escribelo\n(de lo contrario press enter): ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            nombre=input("-Cual es tu nombre?: ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            pizzas=int(input("-Cuantas pizzas deseas comprar?: "))
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            envio=int(input("-Quisieras un delivery?: \nPresiona 1 para SI o 2 para NO \nRespuesta: "))
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            mododepago=int(input("-Como deseas pagar?: \n 1 Efectivo o 2 Transferencia \nRespuesta: "))
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            venta1=Venta()
            venta1.registrar_compra(nombre,pizzas,envio,mododepago,id_del_comprador)
        elif hacer==2:
            print("|||||||||||||||||||||||||||||||||||||")
            consulta=input("Que deseas consultar?:" \
            "\n 1. Datos generales de un comprador" 
            "\n 2. Datos especificos" 
            "\nRespuesta: ")
            if consulta ==1:
                id_del_comprador=int(input("Ingrese el id del cliente: "))
                print(Registros.mostrar_datos_de_comprador(id_del_comprador))
            elif consulta ==2:
                traer=int(input("Que deseas consultar?" \
                "1. Una venta en general" \
                "2. Un envio" \
                "3. Una/s pizza/s de una compra especifica"
                "\nRespuesta: "))
                if traer== 1:
                    idcomprador=int(input("Ingrese el id del cliente: "))
                    idcompra=int(input("Ingrese el id de la compra: "))
                    print(Registros.mostrar_compra(idcomprador,idcompra))
        else:
            print("Ha finalizado el programa, Arrivederci!")
            break
iniciar()