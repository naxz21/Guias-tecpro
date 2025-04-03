import datetime

class Empresa :
    def __init__(self,nombre_empresa,tipo):
        self.nombre_empresa = nombre_empresa 
        self.tipo = tipo
        self.facturas = []
    def agregar_factura(self,factura):
        self.facturas.append(factura)
    def mostrar_facturas(self):
        print("Nombre empresa: ",self.nombre_empresa,"-",self.tipo)
        for factura in self.facturas:
            print("Factura nro: ",factura.nro)
            print("Cliente: ",factura.cliente.nombre,"-",factura.cliente.nro_cuit)
            print("Fecha: ",factura.fecha)
            print("Total: ",factura.total)
            cont = 1
            for detalle in factura.detalles:
                detalle.mostrar_detalle(cont)
                cont = cont + 1

class Factura :
    def __init__(self,nro,fecha,total,cliente):
        self.nro = nro
        self.fecha = fecha 
        self.total = total
        self.detalles = []
        self.cliente = cliente
    def agregar_detalle(self,detalle):
        self.detalles.append(detalle)
        
class Detalle : 
    def __init__(self, nombre,total,unidad):
        self.nombre = nombre
        self.total = total
        self.unidad = unidad
    def mostrar_detalle(self,num):
        print("Detalle ",num,":",self.nombre," ",self.unidad," unid."," Total item: ",self.total)

class Cliente : 
    def __init__(self, nro_cuit, nombre):
        self.nro_cuit = nro_cuit
        self.nombre = nombre 

cliente = Cliente("30-12345678-1","Gilcomat SRL")
empresa = Empresa("Mayorista S.A","IVA Monotributo")
factura = Factura("0001 0100",datetime.date(2015,1,5),1000,cliente)
detalle1 = Detalle("Porcelanato 45x45",600,100)
detalle2 = Detalle("Grifería FV 6 piezas",400,1)

factura.agregar_detalle(detalle1)
factura.agregar_detalle(detalle2)
empresa.agregar_factura(factura)

empresa.mostrar_facturas()