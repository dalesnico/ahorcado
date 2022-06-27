
"""
Ahorcado:
-ingresar una palabra
-contar las letras y restale 2
-Imprimir la primera y la ultima letra de la palabra
-reemplazar letras internas por guiones
###wish list #####si hay mas 2 de palabras y las pabras tienen 2 o 3 letras imprimir solo la primera de ellas
-ejemplo: palabra ingresada es: heladera    mostrar h------a  
hacer loop hasta ahorcar al participante!!! 8 vueltas 
preguntar letra y buscar si esta en la palabra
si esta, mostrar resultado nuevo  
ejemplo: letra ingresada D mostar h---d--a no contar vuelta de loop y Seguir
si no esta contar vuelta de loop (mostar dibujo de que se va ahorcando)
y seguir...
"""
from getpass import getpass
from re import sub
#ver de hacer shadow el ingreso de la palabra
def ahorcado(kl):
    if kl == 9:
        print("ahorcado")
        print("!--------!")
        print("!        !")
        print("!()      !")
        print(" /|\     !")
        print("/ | \    !")
        print(" | |     !     QEPD")
        print("_| |_    !      _!_")
        print("       __!__     |")
        print("      ||___||    |")
    #ahorcado
        print("la palabra era: " + palabra)
    if kl == 8:
        print("Que CABEZAAAAAAA !!!...")
        print("   Q ")
        print("  /|\ ")
        print(" / | \ ")
        print("  | | ")
        print(" _| |_")
    if kl == 7:
        print("Zurditooos!!!...")
        print("  /|\ ")
        print(" / | \ ")
        print("  | | ")
        print(" _| |_")
    if kl == 6:
        print("esa es la mano de dios???...")
        print("  /| ")
        print(" / | ")
        print("  | | ")
        print(" _| |_")

    if kl == 5:    
        print("Que lindo cuerpitoooo para colgar!!!!...")
        print("   | ")
        print("   | ")
        print("  | | ")
        print(" _| |_")
    if kl == 4:
        print("Tenemos las 2 piernas!!!!...")
        print("  | | ")
        print(" _| |_")

    if kl == 3:
        print("Tenemos una pierna ahora!!!!...")
        print("  |  ")
        print(" _| _")
    if kl == 2:
        print("Ya tenemos los 2 pies...")
        print("_ _") 
    if kl == 1:
        print("primero el pie derecho...")
        print("_")  
        
def string(entrada):
    count = len(entrada)-2
    first = entrada[:1]
    last = entrada[-1]
    a = 1
    b = "-"
    #print(contar)
    #print(first)
    #print(last)
    while a != count:
        #print(a)
        b += "-"
        #print(b)
        a += 1
    return {"pri": first, "ult": last, "x": b, "contar": count}
        
def nook(entrada,kill):
    print(entrada + " no esta en la palabra\r\n")
    #print("te quedan ", kill ," vidas\r\n")
    print("".join(pista))
    return kill

def ok(l,x,c,p,cc):
#    print(p + " Palabra") #minuto Palabra
#    print(l + " esta en la palabra") #m esta en la palabra
#    print(x + " letras ocultas") #---- letras ocultas
#    print(c ," contar letras de la palabra") #6  contar letras de la palabra
#    print(cc + " palabra con guiones") #m----o palabra con guiones
    numL = p.count(l)#cantidad de veces que se repite la letra
    nuevalista = [p]
    #print(nuevalista)
    while numL != 0:    
        ps = p.find(l)
#        print(ps)
#        print(numL, " numero de lineas")
        #print(nuevalis8ta[])
        for i, y in enumerate(p):
            if y.lower() == l.lower():
                pista[i] = y
                #print("".join(pista))       
        numL -= 1
    return     
        
        #for j in l    
        #print(j.find())
    
    
#    "subcadena = l

#    indice = palabra.find(subcadena)
#    print(indice)
    
#    print(a.upper())
    
palabra = getpass("participante 1: Ingrese una palabra: \r\n")
pasoUno = string(palabra)
pista = ["-"]*len(palabra)
print("".join(pista) + " <---- aca la palabra que tenes que adividar \r\n")
#print(pasoUno["pri"],pasoUno["x"],pasoUno["ult"])
cuerda = pasoUno["pri"]+pasoUno["x"]+pasoUno["ult"]
#print(cuerda)
#print(pasoUno["ult"])
#print(pasoUno["x"])
#print(pasoUno["contar"])
#print("Participante 2:  PALABRA a ADIVINAR ES:" +  first,b,last)

    
#loop ahorcado
kill = 0
z = ""
while kill < 9 and palabra != z:
    letra = input("ingrese una letra: \r\n")
    if letra in palabra:
        ok(letra,pasoUno["x"],len(palabra),palabra,cuerda)#ir a funcion OK
        print("ZAFASTEEEEE!!!!! pero por esta vez!!!\r\n")
        z = "".join(pista)
        #print(palabra + " palabra")
        print("".join(pista) + "\r\n")
    else:
        nook(letra,kill)#ir a funcion NOOK
        kill = kill + 1
        #print("kill fuera de la funcion ", kill )
        ahorcado(kill)
        #print("te ahorcaste")
        z = "".join(pista)
if palabra == z:
    print("GANASTEEEEEEE \r\n")
else:    
    print("queres la revancha???\r\n")

"""
for i in contar
    a = "-"
    b = a++
print(b)
"""








