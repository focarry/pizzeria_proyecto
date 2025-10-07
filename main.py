import datetime

#1 registrar la identidad de pizza y algunas funciones 
class Pizza():
    next_id= 0
    lista_de_pizzas= []
    precio= 7000
    
    def __init__(self):
        
        
        #global next_id

        
        self.idpizza= Pizza.next_id
        Pizza.next_id+=1  #se le suma 1 al id para que sea otro diferente para otra pizza
        
        Pizza.lista_de_pizzas.append(self.idpizza) #se añade el id de la pizza a la lista de pizzas
    def cantidad_de_pizzas():
        return len(Pizza.lista_de_pizzas) #devuelve la cantidad de pizzas en total
    def monto_total_pizzas():
        return len(Pizza.lista_de_pizzas)* Pizza.precio #multiplica cantidad de pizas por el precio para saber el monto total

#definimos un "comprador"
class Comprador():
    next_id=0
    compradores= {

    }
    
    def __init__(self,nombre):
        self.nombre= nombre
        self.idcomprador= Comprador.next_id #se añade un id al comprador nuevo 
        Comprador.compradores[self.idcomprador]= [nombre]  #añade id + nombre y apellido al diccionario
        Comprador.next_id+=1 #se cambia el proximo id a añadir
        
#definimos un "envio"
class Envios():
    precio_de_envio=500
    next_id= 0
    envios=[]
    def __init__(self):
        self.id_envio= Envios.next_id #añade un id al envio
        Envios.next_id+=1 #cambia id proximo a añadir
        Envios.envios.append(self.id_envio)

# definir una compra 
class Compra():
    next_id=0
    compras= {}
    def __init__(self):
        self.idcompra=Compra.next_id #añade id de compra
        Compra.compras[self.idcompra]=[] #se añade el id de compra al diccionario de compras
        Compra.next_id+=1 #cambia siguiente id a añadir
    def registrar_comprador(self,nombre):
        Compra.compras[self.idcompra]=[nombre]
    def generar_envio(self, respuesta):
        if respuesta ==True:
            return True    
        else:
            return False
    
        

class Pagos():
    efectivo=[]
    transferencia=[]
    def RegistrarPago(self, monto,tipo):
        match tipo:
            case 1:
                self.efectivo.append(monto)
            case 2:
                self.transferencia.append(monto)

class Registros():
    cantidad_de_compradores= {
    }
    cantidaddepizzas=Pizza.lista_de_pizzas
    cantidad_de_compras= Compra.compras
    
    def guardar_compra(self,id_de_compra,id_de_pizzas,id_cliente,nombredecliente):
        if id_cliente not in Registros.cantidad_de_compradores:
            Registros.cantidad_de_compradores[id_cliente]={
                'nombre':nombredecliente,
                "compras":{
                }
            }
        Registros.cantidad_de_compradores[id_cliente]["compras"][id_de_compra]={
            "pizzas":id_de_pizzas
        }
        
    def guardar_envio(self,id_decliente,id_decompra,id_de_envio,monto_de_envio):
        tiempo=datetime.datetime.now()
        tiempo=tiempo.strftime('%H:%M')
        dia=datetime.date.today()
        
        Registros.cantidad_de_compradores[id_decliente]["compras"][id_decompra].setdefault(
            "envio",{id_de_envio:{}})
        Registros.cantidad_de_compradores[id_decliente]["compras"][id_decompra]["envio"][id_de_envio].setdefault(
            "Monto",monto_de_envio)
        Registros.cantidad_de_compradores[id_decliente]["compras"][id_decompra]["envio"][id_de_envio].setdefault(
            "Hora",tiempo)
        Registros.cantidad_de_compradores[id_decliente]["compras"][id_decompra]["envio"][id_de_envio].setdefault(
            "Fecha",dia)
    
    def guardar_pago(self, idcliente,id_compra,modo_de_pago,monto_de_pago):
        if modo_de_pago==1:
            modo_de_pago="Efectivo"
        elif modo_de_pago==2:
            modo_de_pago="Transferencia"
        Registros.cantidad_de_compradores[idcliente]["compras"][id_compra].setdefault(
            "Modo de pago",modo_de_pago)
        Registros.cantidad_de_compradores[idcliente]["compras"][id_compra].setdefault(
            "Monto",monto_de_pago)
    
    def mostrar_datos_de_comprador(idcomprador):
        return Registros.cantidad_de_compradores[idcomprador]
    
    def mostrar_compra(idcomprador,idcompra):
        return Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]
    def mostrar_envio(idcomprador, idcompra,idenvio):
        
        monto=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["envio"][idenvio]["Monto"]
        hora=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["envio"][idenvio]["Hora"]
        fecha=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["envio"][idenvio]["Fecha"]
        return f"el monto del envío es ${monto} \n-Fue realizado a las {hora} el {fecha}"
    def mostrar_pizzas(idcomprador,idcompra):
        idpizzas=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["pizzas"]
        cantidad=len(Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["pizzas"])
        if cantidad==1:
            return f"-La compra tiene {cantidad} pizza comprada. \n-El id de la pizza es {idpizzas}"
        else:
            return f"-La compra tiene {cantidad} pizzas compradas.  \n Los id son {idpizzas}"
    def mostrar_pagos(idcomprador,idcompra):
        modo=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["Modo de pago"]
        monto=Registros.cantidad_de_compradores[idcomprador]["compras"][idcompra]["Monto"]
        return f"-El modo de pago fue en {modo}.\n-El monto de esta compra fue de ${monto}."
class Venta():
    modo_depago=True
    def registrar_compra(self, nombrecomprador,cantidadpizza,envio,mododepago,idcliente):
        
        #registra el comprador con su id
        if idcliente.strip() == "":
                idcliente = None
        else:
            try:
                idcliente = int(idcliente)
            except ValueError:
                print("El ID debe ser un número, se creará un nuevo cliente."
                )
                idcliente= None
        if idcliente not in Registros.cantidad_de_compradores:
            comprador1=Comprador(nombrecomprador)
            idcliente=comprador1.idcomprador
        
        #registra una pizza con su id
        idpizzas=[]     
        costodepizzas=0
        for i in range(cantidadpizza):
            pizza1=Pizza()
            idpizzas.append(pizza1.idpizza)
            costodepizzas+=pizza1.precio
            
        #registra la compra conm su id y nombre de comprador
        venta1=Compra()
        idcompra=venta1.idcompra
        registrar=Registros()
        
        #registra compra con envio
        costoenvio=0
        idenvio=''
        
        if envio==True:
            registrar.guardar_compra(idcompra,idpizzas,idcliente,nombrecomprador)
            #si hay envio se crea, primero se genera la compra y demas, luego el envio para no sobrescribir
            envio1=Envios()
            costoenvio=envio1.precio_de_envio
            idenvio=envio1.id_envio
            registrar.guardar_envio(idcliente,idcompra,idenvio,costoenvio)
            
        #registra compra sin envio
        else:
            registrar.guardar_compra(idcompra,idpizzas,idcliente,nombrecomprador)
        #registra el pago
        pago1=Pagos()
        monto=costodepizzas+costoenvio
        pago1.RegistrarPago(monto,mododepago)
        registrar.guardar_pago(idcliente,idcompra,mododepago,monto)

        #Impresion de Ticket
        print(f"El cliente: {nombrecomprador}",
              "\n-------------------------------------------"
              f"\nTiene la cantidad de: {cantidadpizza} pizza/s",
              "\n-------------------------------------------"
              f"\nEl id de esta compra es: {idcompra}"
              "\n-------------------------------------------"
              f"\nSu id de comprador es: {idcliente}"
              "\n-------------------------------------------"
              f"\nEl id de su/s pizza/s es: {idpizzas}"
              "\n-------------------------------------------")
        if envio==True:
            print(f"El id de su envio es {idenvio}",
                  "\n|||||||||||||||||||||||||||||||||||||")
        print(f"TOTAL A PAGAR: ${monto}")
#interfaz "grafica" por el momento xd
"""compra1=Venta()
compra1.registrar_compra("yoel flores",2,False,False,'')    
compra2=Venta()
compra2.registrar_compra("Pepe trulepe",3,True,True,"")
compra3=Venta()
compra3.registrar_compra("yoel flores",1,True,False,0)
compra4=Venta()
compra4.registrar_compra("Pepe trulepe",1,True,False,1)

print (f"la cantidad de compradores con sus id son {Registros.cantidad_de_compradores}"
        f"\n la cantidad de Compras son {len(Registros.cantidad_de_compras)}")
print(f"el comprador {Registros.cantidad_de_compradores[0]["nombre"]}"
      f"\ntiene {len(Registros.cantidad_de_compradores[0]["compras"][0]["pizzas"])} pizzas compradas:{Registros.cantidad_de_compradores[0]["compras"][0]["pizzas"]}") 
      """