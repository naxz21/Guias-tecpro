import datetime
class Alumno:
    def __init__(self,nombre,dni,fechanacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fechanacimiento = fechanacimiento
    def calcularEdad(self):
        return 1

class Carrera:
    def __init__(self,nombreCarrera):
        self.nombre = nombreCarrera
        self.inscripciones = []

    def agregarinscripcion(self, inscripcion):
        self.inscripciones.append(inscripcion)

    def mostrarAlumnos(self):
        print("Carrera: ",self.nombre)
        for inscripcion in self.inscripciones:
            print("- ",inscripcion.alumno.nombre," - ",inscripcion.fechainscipcion)

class Inscripcion:
    def __init__(self,alumno,fechainscipcion):
        self.fechainscipcion  = fechainscipcion
        self.alumno = alumno

class Facultad:
 
 def __init__(self, nombreFacultad):
        self.nombreFacultad = nombreFacultad
        self.carreras = []

 def agregarCarrera(self,carrera):
    self.carreras.append(carrera)

 def mostrarCarrerasyAlumnos(self):
     print(f"facultad : {self.nombreFacultad}")
     for carrera in self.carreras:
        carrera.mostrarAlumnos()



facultad = Facultad("fich")
informatica = Carrera("II")
recursoshidricos= Carrera("RH")

alumno1 = Alumno("alumno1",1111111,datetime.date(1990,11,11))
alumno2 = Alumno("alumno2",2222222,datetime.date(1990,12,12))

inscripcion1 = Inscripcion(alumno1,datetime.date(2008,10,12))
inscripcion2 = Inscripcion(alumno2,datetime.date(2008,11,12))

informatica.agregarinscripcion(inscripcion1)
informatica.agregarinscripcion(inscripcion2)

facultad.agregarCarrera(informatica)
facultad.agregarCarrera(recursoshidricos)

facultad.mostrarCarrerasyAlumnos()

