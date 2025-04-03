import datetime
import hashlib

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento,password):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nacimiento
        self.password_hash = self.encriptar_password(password)
    def _calcular_edad(self):
       return int(((datetime.date.today() - self.fecha_nac )).days / 365)

    def _diasemana(self):
        print(datetime.date(2025,self.fecha_nac.month,self.fecha_nac.day).strftime('%A'))
    
    def _mostrar_password(self):
        print("password:",self.password_hash)
    
    def validar_password(self,password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def encriptar_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()


    def _mostrar(self):
        print(self.nombre,", ", self.apellido,": ",self._calcular_edad(), " años") 

anio = int(input("año: "))
mes = int(input("mes: "))
dia = int(input("dia: "))



ejemplo = Persona("Ignacio", "Larocca", datetime.date(anio, mes, dia),"pelotilla")
ejemplo._mostrar()
ejemplo._diasemana()
if ejemplo.validar_password("pelotilla1"):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
