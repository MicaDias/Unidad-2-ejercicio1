import csv
from Email import Email
class ManejadorEmail:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    #crearinstancias a partir del archivo.
    def agregar(self,email):
        if type(email)==Email:
            self.__lista.append(email)
        else:
            print("No es de tipo email,por lo tanto no se agrega a la lista")
    def cargardatos(self):
        archivo=open("archivo.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera= True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                separador=fila[0].split('@')
                idCuenta=separador[0]
                separador2=separador[1].split('.')
                dominio=separador2[0]
                tipodedominio=separador2[1]
                email=Email(idCuenta,dominio,tipodedominio)
                self.agregar(email)
        archivo.close()
      

    def buscar_identificador(self,iden):
        i=0
        cant_elementos=len(self.__lista)
        iden_repetido=0
        while iden_repetido<2 and i<cant_elementos:
            if self.__lista[i].verificarinden(iden):
                iden_repetido+=1
            i+=1
         
        if iden_repetido==2:
            print("El identificador{} se repite mas de una vez".format(iden))
        else:
            print("El indentificador {} no se repite".format(iden))
       
    def testmanejador(self):
        print("Test manejador")
        manejador=ManejadorEmail()
        manejador.cargardatos()
        manejador.buscar_identificador('micadias295')
        manejador.buscar_identificador('rocio122')
        manejador.agregar('dias21')
        manejador.agregar(Email('dias295','gmail','com',''))
        
        
    









            
                








        