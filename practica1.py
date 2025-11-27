
class Pizza():
    next_id= 0
    precio= 7000
    def __init__(self):
        #global next_id
        self.idpizza= Pizza.next_id
        Pizza.next_id+=1  #se le suma 1 al id para que sea otro diferente para otra pizza
        self.preciodepizza=Pizza.precio
class Envio():
    precio=500
    next_id= 0
    def __init__(self):
        self.id_envio= Envio.next_id #añade un id al envio
        Envio.next_id+=1 #cambia id proximo a añadir
        self.precio_de_envio=Envio.precio
class Pago():
    def __init__(self, monto,tipo):
        self.monto=monto
        self.tipo=tipo
class Compra():
    def __init__(self,pizzas,monto,tipodepago):
        self.idpizzas=[]
        for i in range(pizzas):
            pizza=Pizza()
            self.idpizzas.append(pizza.idpizza)
        self.pago=Pago(monto,tipodepago)
compra1=Compra(3,21000,"transferencia")
print(compra1.idpizzas)
print(compra1)