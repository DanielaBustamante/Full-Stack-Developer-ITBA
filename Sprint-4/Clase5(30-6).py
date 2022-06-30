

#f = open("archivo.txt", "a+")

#print(f.readlines())
#f.write("abc123")
#f.write("Otra cosa")
#f.writelines("Otra mas") 

def copiar(f1Name,f2Name):
    f1 = open(f1Name, "r")
    f2 = open(f2Name, "w") 

    text = None
    while text != "":
        text = f1.read(10)
        f2.write(text)
    f1.close()
    f2.close()

#copiar("archivo.txt", "copia.max")

f = open("copia.max")
#
#

f.writelines("".join(["Probando\n" for x in range(10)]))