from Email import Email
from Menu import Menu
import re
import csv

if __name__ == "__main__": 
    
    nombre=input("Ingrese el nombre:")
    correo=input("Ingrese su correo:")
    
  #crear instancia con el correo ingresado
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        contra=input("Ingrese la contrasena:")
        lista=correo.split('@')
        idCuenta=lista[0]
        lista2=lista[1].split('.')
        dominio=lista2[0]
        tipodedominio=lista2[1]
        email1=Email(idCuenta,dominio,tipodedominio,contra)
        email1.crearCuenta(email1.crearCuenta(email1.retornaEmail()))
        #punto1
        print("Estimado {} te enviaremos tus mensajes a la direccion {} ".format(nombre,email1.retornaEmail()))
        #print(email1.retornaEmail())
        menu=Menu()
        menu.lanzarMenu(email1)
    else:
        print("Correo no valido")

    
    





