
"""
Ahorcado:
2 participantes,
participante 1 ingresa palabra para que sea adivinada
participante 2 debera ingresar las letras para evitar ser ahorcado.
"""
from getpass import getpass
from re import sub
#ver de hacer shadow el ingreso de la palabra
def ahorcado(kl):
    if kl == 9:
        print("PERDISTEEEE TE AHORCASTE.... \r\n")
        print("!--------!")
        print("!        !")
        print("!()      !")
        print(" /|\     !")
        print("/ | \    !")
        print(" | |     !     QEPD")
        print("_| |_    !      _!_")
        print("       __!__     |")
        print("      ||___||    |")
        print("la palabra era: " + palabra + "\r\n")
    if kl == 8:
        print("Ya tenemos la CABEZA!!!... \r\n")
        print("  () ")
        print("  /|\ ")
        print(" / | \ ")
        print("  | | ")
        print(" _| |_ \r\n")
    if kl == 7:
        print("Que linda manito que tengo yo...  \r\n")
        print("  /|\ ")
        print(" / | \ ")
        print("  | | ")
        print(" _| |_ \r\n")
    if kl == 6:
        print("esa es la mano de dios???... \r\n")
        print("  /| ")
        print(" / | ")
        print("  | | ")
        print(" _| |_ \r\n")

    if kl == 5:    
        print("Que lindo cuerpitoooo para colgar!!!!... \r\n")
        print("   | ")
        print("   | ")
        print("  | | ")
        print(" _| |_ \r\n")
    if kl == 4:
        print("Tenemos las 2 piernas!!!!... \r\n")
        print("  | | ")
        print(" _| |_ \r\n")

    if kl == 3:
        print("Tenemos una pierna ahora!!!!... \r\n")
        print("  |  ")
        print(" _| _   \r\n")
    if kl == 2:
        print("Ya tenemos los 2 pies... \r\n \r\n")
        print("_ _ \r\n") 
    if kl == 1:
        print("primero el pie derecho... \r\n \r\n")
        print("_ \r\n")  
        
def string(entrada):
    count = len(entrada)-2
    first = entrada[:1]
    last = entrada[-1]
    a = 1
    b = "-"
    while a != count:
        b += "-"
        a += 1
    return {"pri": first, "ult": last, "x": b, "contar": count}
        
def nook(entrada,kill):
    print(entrada + " no esta en la palabra\r\n")
    print("".join(secreto))
    return kill

def ok(l,x,c,p,cc):
    numL = p.count(l)
    nuevalista = [p]
    while numL != 0:    
        ps = p.find(l)
        for i, y in enumerate(p):
            if y.lower() == l.lower():
                secreto[i] = y       
        numL -= 1
    return     
        
        
#comienzo del Juego 
   
palabra = getpass("participante 1: Ingrese una palabra: \r\n")
pasoUno = string(palabra)
secreto = ["-"]*len(palabra)
print("".join(secreto) + " <---- aca la palabra que tenes que adividar \r\n")
cuerda = pasoUno["pri"]+pasoUno["x"]+pasoUno["ult"]

    
#loop ahorcado
kill = 0
z = ""
while kill < 9 and palabra != z:
    letra = input("ingrese una letra: \r\n")
    if letra in palabra:
        ok(letra,pasoUno["x"],len(palabra),palabra,cuerda)#ir a funcion OK
        print("ZAFASTE!!!!! pero por esta vez!!!\r\n")
        z = "".join(secreto)
        print("".join(secreto) + "\r\n")
    else:
        nook(letra,kill)#ir a funcion NOOK
        kill = kill + 1
        ahorcado(kill)
        z = "".join(secreto)
if palabra == z:
    print("GANASTEEEEEEE \r\n")
else:    
    print("queres la revancha???\r\n")