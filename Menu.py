from Email import Email
import csv
from ManejadorCorreo import ManejadorEmail
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,email):
        #Menu opciones
        if type(email)==Email:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para modificar contraseña.')
                print('-Ingrese 2 para leer un archivo y buscar un identificador.')
                print('-Ingrese 3 para la funcion test.')
                print('-Ingrese 4 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1' or opcion=='3'):
                    ejecutar(email)
                else:
                    ejecutar()
    def opcion1(self,email):
        # punto 2) Cambiar contraseña.
        con1=input("Ingresar la contrasena actual: ")
        if email.verficarcontrasena(con1):
            nueva=input("Ingrese la nueva  contrasena: ")
            email.modificarContrasena(nueva)
            print("La contrasena se modifico")
        else:
            print("Contraseña incorrecta")

    def opcion2(self):
        manejador1=ManejadorEmail()
        manejador1.cargardatos()
        iden=input("Ingrese el identificador a buscar:")
        manejador1.buscar_identificador(iden)

    def opcion3(self,email):
        email.funcionTest()
        manejador2=ManejadorEmail()
        manejador2.testmanejador()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')