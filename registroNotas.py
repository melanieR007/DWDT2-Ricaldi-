class alumnos:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombreAlumno=nombre
        self.apellidoAlumno=apellido
        self.edadAlumno=edad
        self.notaAlumno=''
        self.nacionalidadAlumno=nacionalidad

    def registrarNota(self, notaAlumno):
        self.notaAlumno=notaAlumno

if __name__=='__main__':
    alumnosSistema = []
    comandosSistema = ['R','C','P','S', 'X']
    print("“Bienvenidos al registro de notas")
    while True:
        comandoInformacion = input("Ingrese comando : ")
        print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion == 'R':
                print("Se registrara un nuevo alumno : ")
                nombreAlumno = input("Ingrese el Nombre del alumno : ")
                apellidoAlumno = input("Ingrese el Apellido del alumno : ")
                edadAlumno = input("Ingrese el Edad del alumno : ")

                nacionalidadAlumno = input("Ingrese el Nacionalidad del alumno : ")
                objAlumno = alumno(nombreAlumno,apellidoAlumno, edadAlumno, nacionalidadAlumno)
                productosSistema.append(objAlumno)
            elif comandoInformacion == 'C':
                print("Se calificara a los alumnos")
                for alumnosInfo in alumnosSistema:
                    if alumnosInfo. == '':
                        notaAlumno = input(f"Ingrese la nota del alumno {alumnosInfo.nombreAlumno} : ")
                        alumnosInfo.registrarNota(notaAlumno)
            elif comandoInformacion == 'P':
                print("Se mostrara el promedio de todos los alumnos registrados")
                i = 0
                sumaNotas=0
                for alumnosInfo in productosSistema:
                    sumaNotas= sumaNotas+alumnosInfo.notaAlumno
                    i = i + 1
                prom=sumaNotas/i
                print(f"El promedio de notas para {i} cant. de alumnos es : {prom}\n")

            elif comandoInformacion == 'S':
                print("Se mostrara la suma de notas de todos los alumnos registrados:")
                i = 0
                sumaNotas=0
                for alumnosInfo in productosSistema:
                    sumaNotas= sumaNotas+alumnosInfo.notaAlumno
                    i = i + 1
                print(f"La suma de notas de < {i} cant. de alumnos es : {sumaNotas}\n")

            else:
                print("Comando de finalizacion")
                break
        else:
            print('Comando incorrecto, ingresar nuevamente')