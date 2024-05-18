
class CuentaBancaria:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        self.__saldo = 0
    
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, valor):
        self.__saldo = valor
    
    def Ingresar(self,ingreso):
        if (ingreso>0):
            self.__saldo=self.__saldo+ingreso
        else:
            print("El ingreso debe ser positivo")

    def RetirarSaldo(self,retiro):
        if retiro>self.__saldo:
            print("Saldo Insuficiente")
        else:
            self.__saldo-=retiro    
    
    def __str__(self):
        return f"Titular {self.Nombre} tu saldo es: {self.__saldo}"

Nueva=CuentaBancaria("Pedro")
Nueva.Ingresar(100)


print(Nueva)