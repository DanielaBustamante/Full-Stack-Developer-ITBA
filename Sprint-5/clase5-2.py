class Ejemplo:
    __atributo = "Soy privado"
    
    def __metodo_privado(self):
        print("metodo privado")

e = Ejemplo()
print(e._Ejemplo__metodo_privado)
