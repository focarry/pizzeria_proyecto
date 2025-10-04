from main import *
class Inicio:
    hacer=int(input("|||||Hola, Bienvenido a la pizzeria Luigi!||||| " \
    "\n-Que deseas hacer?" \
    "\n'1' Comprar " \
    "\n'2' Consultar " \
    "\n-Quiero: "))
    print()
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
        "\n")

iniciar=Inicio()