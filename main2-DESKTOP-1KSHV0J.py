

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
        if tipo==True:
            self.efectivo.append(monto)
        else:
            self.transferencia.append(monto)

class Registros():
    cantidad_de_compradores= Comprador.compradores
        
    def guardar_compra(self,id_de_compra,id_de_pizzas,id_cliente,nombredecliente):
        
        Registros.cantidad_de_compradores[id_cliente]["compras"][id_de_compra]={"pizzas":[id_de_pizzas]}
    def guardar_envio(self,id_decliente,id_decompra,id_de_envio):
        Registros.cantidad_de_compradores[id_decliente]["compras"][id_decompra]={"envio":id_de_envio}
    cantidaddepizzas=Pizza.lista_de_pizzas
    cantidad_de_compras= Compra.compras
    
    
class Venta():
    modo_depago=True
    def registrar_compra(self, nombrecomprador,cantidadpizza,envio,mododepago,idcliente):
        
        #registra el comprador con su id
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
        
        costoenvio=0
        idenvio= ""
        
        #registra compra con envio
        if envio==True:
            registrar.guardar_compra(idcompra,idpizzas,idcliente,nombrecomprador)
            #si hay envio se crea, primero se genera la compra y demas, luego el envio para no sobrescribir
            envio1=Envios()
            costoenvio=envio1.precio_de_envio
            idenvio=envio1.id_envio
            registrar.guardar_envio(idcliente,idcompra,idenvio)
        #registra compra sin envio
        else:
            registrar.guardar_compra(idcompra,idpizzas,idcliente,nombrecomprador)
        
        
        #registra un tipo de pago
        pago1=Pagos()
        monto=costodepizzas+costoenvio
        pago1.RegistrarPago(monto,mododepago)

        print(f"El cliente: {nombrecomprador}",
              "\n-------------------------------------------"
              f"\nTiene la cantidad de: {cantidadpizza} pizzas",
              "\n-------------------------------------------"
              f"\nEl total a pagar es: {monto}",
              "\n-------------------------------------------"
              f"\nSu id de compra es: {idcompra}"
              "\n-------------------------------------------"
              f"\nSu id de comprador es: {idcliente}"
              "\n-------------------------------------------"
              f"\nEl id de su/sus pizza/s es: {idpizzas}"
              "\n-------------------------------------------")
        if envio==True:
            print(f"El id de su envio es {idenvio}",
                  "\n|||||||||||||||||||||||||||||||||||||")


compra1=Venta()
compra1.registrar_compra("yoel flores",2,False,False,'')
compra2=Venta()
compra2.registrar_compra("Pepe trulepe",3,True,True,"")
compra3=Venta()
compra3.registrar_compra("yoel flores",1,True,False,1)


print (f"la cantida de compradores con sus id son {Registros.cantidad_de_compradores}"
        f"\n la cantidad de Compras son {Registros.cantidad_de_compras}")