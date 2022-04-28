class Email:
    __idCuenta= " "
    __dominio= " "
    __tipodominio= " "
    __contrasena= " "
    def __init__(self,idCuenta='',dominio='',tipodominio='',contrasena=''):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipodominio=tipodominio
        self.__contrasena=contrasena
    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipodominio)
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self,correo):
        if type(correo)==str:
            print("se creo la cuenta: "+correo)
    
    def verficarcontrasena(self,con):
       return con==self.__contrasena
          

    def modificarContrasena(self,nueva):
        self.__contrasena=nueva
    def verificarinden(self,iden):
        return iden==self.__idCuenta
    def mostrarDatos(self):
        print("idcuenta:{} dominio:{} tipo:{}".format(self.__idCuenta,self.__dominio,self.__tipodominio))
    def funcionTest(self):
        email2=Email('juan12','gmail','com','1234')
        email4= Email('mica12','yahoo','com','234')
        print(email2.retornaEmail())
        print(email2.getDominio())
        print(email4.retornaEmail())
        print(email4.getDominio())
        print("metodo crear cuenta:")
        email2.crearCuenta(email2.retornaEmail())
        email4.crearCuenta(email4.retornaEmail())
        print("Metodo modificar contrasena:")
        email2.modificarContrasena('234')
        email4.modificarContrasena('mica')
        print("Metodo vericar contrasena:")
        email2.verficarcontrasena('345')
        





        

