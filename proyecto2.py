#Clase de programacion
#Proyecto: 2
#Autoras: Carredano Ochoa Elisa - Alvarado Morales Yenny Lluviza
#Carnet:      16285-20                    15196-20
#Fecha: 29 de octubre 2020
#Haremos un programa que permita al usuario reordenar una 
#palabra descompuesta y adivinar la palabra que corresponda
#TypeShift.
#   / '.        .--.                           A____A
#   |   \     .'-,  |                         |・ㅅ・|
#   \    \___/    \_/                         |っ　ｃ| 
#     '._.'   '._.'                           |　　　|  
#       /  . .  \          PROYECTO 2         |　　　| /
#       |=  Y  =|                             |　º　 |/
#       \   ^   /                             |　　　|
#        `'---'`                               U￣￣U

from random import randint
from screen import clear
from time import sleep


#Damos la bienvenida al usuario.
inicio = ("♥♥♥♥ Bienvenido a este embrollo, la finalidad de este juego es desafiar a tu cerebro, para encontrar palabras que aunque se encuentren en  desorden tu cerebro sea capaz de captar la palabra oculta!!. No olvides compartir con tus amigos y guarda este programa, te aseguramos     horas de diversión! ♥♥♥♥")

inicio_1 = inicio.format(inicio = inicio).center(139)
print("-" * 139)
print(inicio_1)
print("-" * 139)
sleep(20)
clear()

inicio.format(inicio = inicio).center(80)
frase = " TipeShift "
frase_1 = frase.strip().center(80, "*")
print(frase_1)

#Solicitamos el nombre
nombre = input('Escribe tu nombre (｡♥‿ ♥｡): ')
sleep(1.5)
clear()

#Colocamos un arreglo con palabras para cada nivel
palabras_facil = ["carro", "circo", "torre", "madre", "libro", "vista", "silla", "comer", "cantar", "cobre", "salto", "angel", "arbol", "vivir", "disco", "playa", "rayos", "mayas", "joyas", "cuadro", "loros"]

palabras_medio = ["fabulas", "corazon", "jabalis", "tenedor", "ubicada", "cuchara", "ucrania", "camisas", "barbero", "sandia", "bananas", "mascara", "caballo", "cortina", "dibujos", "cortina", "gallina", "galleta", "objetos", "manzana"]

palabras_dificil = ["japones", "camaras", "ardilla", "biblias", "brillos", "anillos", "cubetas", "pulsera", "fabrica", "maracas", "granero", "objetos", "macabro", "abrazar", "aceites", "acabado", "adivino", "asiento", "maletas", "colibri"]

print("¿Que nivel deseas jugar amiguito? ٩(^‿^)۶")
print("""
1. Facil
2. Medio
3. Dificil
""")
eleccion_nivel = input("Indicanos el numero: ")

#Refrescamos la pantalla
clear()

nombre_1 = "Okaaaay: \"{nombre}\""
nivel_2 = "Este es tu nivel: \"{eleccion_nivel}\""

formato = nombre_1.format(nombre = nombre).center(80)
formato_2 = nivel_2.format(eleccion_nivel = eleccion_nivel).center(80)
print("-" * 80)
print(formato)
print(formato_2)
print("-" * 80)

#Nivel facil
if eleccion_nivel == "1":
    print("Comencemos con el nivel facil (◍ •ᴗ•◍)❤")
    sleep(5)
    clear()
    
    niveles = True

    #Hacemos un arreglo y lo mostramos
    while niveles:
        palabra_pc = randint(0, 19)
        palabra_selec = palabras_facil[palabra_pc]
        total_letras = len(palabra_selec)
        intentos = 7
        fallos = 0 
        letra = []
        aciertos = 0

        while intentos > 0:

            #Mostamos las letras separadas por comas
            descompuestas = sorted(palabra_selec)
            print(*letra, sep=" ")
            print(*descompuestas, sep=" - ")
            palabra_real = input("¿Que palabra has encontrado?: ")

            #Evaluamos las letras de la palabra
            if palabra_real != palabra_selec:
                intentos -= 1
                print("Ufff has fallado amigo ᕙ ༼*◕_◕*༽ᕤ ")
                print("Te quedan", +intentos, "intentos")

            #Si estan las letras, entoces mostramos la palabra
            else:
                print("Excelente has encontrado la palabra (｡♥‿♥｡)")
                aciertos += palabra_selec.count(palabra_real)
                for i in range(total_letras):
                    if palabra_selec [i] == palabra_real:
                        palabra_selec[i] = palabra_real
            
                print("La palabra correcta es -", palabra_selec, "-", "꒰⑅•ᴗ•⑅꒱")
                sleep(5)
                clear()
                break
            if aciertos == 0:
                print("Has perdido !!")
                print("La palabra correcta era: ", palabra_selec, "(✖╭╮✖)")
            sleep(4)
            clear()

        #Preguntamos al usuariosi desea continuar con el juego
        pregunta = input("¿Deseas seguir jugando? si / no: ")
        if pregunta == "si":
            print("Enhorabuena sigamos adivinando palabras ٩(^‿^)۶")
        else:
            print("¡Ah que Sad! see you later (✖╭╮✖)")
            sleep(4)
            clear()
            break

#Nivel medio
if eleccion_nivel == "2":
    print("Comencemos con el nivel medio (◍ •ᴗ•◍)❤")
    sleep(5)
    clear()

    niveles = True

    #Hacemos un arreglo y lo mostramos
    while niveles:
        palabra_pc = randint(0, 19)
        palabra_selec = palabras_medio[palabra_pc]
        total_letras = len(palabra_selec)
        intentos = 5
        fallos = 0 
        letra = []
        aciertos = 0

        while intentos > 0:

            #Mostamos las letras separadas por comas
            descompuestas = sorted(palabra_selec)
            print(*letra, sep=" ")
            print(*descompuestas, sep=" - ")
            palabra_real = input("¿Que palabra has encontrado?:")

            #Evaluamos las letras de la palabra
            if palabra_real != palabra_selec:
                intentos -= 1
                print("Ufff has fallado amigo ᕙ ༼*◕_◕*༽ᕤ ")
                print("Te quedan", +intentos, "intentos")

            #Si estan las letras, entoces mostramos la palabra
            else:
                print("Excelente has encontrado la palabra (｡♥‿♥｡)")
                aciertos += palabra_selec.count(palabra_real)
                for i in range(total_letras):
                    if palabra_selec[i] == palabra_real:
                        palabra_selec[i] = palabra_real
            
                print("La palabra correcta es -", palabra_selec, "-", "꒰⑅•ᴗ•⑅꒱")
                sleep(5)
                clear()
                break
            if aciertos == 0:
                print("Has perdido!!")
                print("La palabra correcta era ", palabra_selec, "(✖╭╮✖)")
            sleep(4)
            clear()

        #Preguntamos al usuario si desea continuar con el juego
        pregunta = input("¿Deseas seguir jugando? si / no: ")
        if pregunta == "si":
            print("Enhorabuena sigamos adivinando palabras ٩(^‿^)۶")
        else:
            print("¡Ah que Sad! see you later (✖╭╮✖)")
            sleep(4)
            clear()
            break

#Nivel dificil
if eleccion_nivel == "3":
    print("Comencemos con el nivel dificil (◍ •ᴗ•◍)❤")
    sleep(5)
    clear()

    niveles = True

    #Hacemos un arreglo y lo mostramos
    while niveles:
        palabra_pc = randint(0, 19)
        palabra_selec = palabras_dificil[palabra_pc]
        total_letras = len(palabra_selec)
        intentos = 3
        fallos = 0 
        letra = []
        aciertos = 0

        while intentos > 0:

            #Mostamos las letras separadas por comas
            descompuestas = sorted(palabra_selec)
            print(*letra, sep=" ")
            print(*descompuestas, sep=" - ")
            palabra_real = input("¿Que palabra has encontrado?:")

            #Evaluamos las letras de la palabra
            if palabra_real != palabra_selec:
                intentos -= 1
                print("Ufff has fallado amigo ᕙ ༼*◕_◕*༽ᕤ ")
                print("Te quedan", +intentos, "intentos")

            #Si estan las letras, entoces mostramos la palabra
            else:
                print("Excelente has encontrado la palabra (｡♥‿♥｡)")
                aciertos += palabra_selec.count(palabra_real)
                for i in range(total_letras):
                    if palabra_selec[i] == palabra_real:
                        palabra_selec[i] = palabra_real
            
                print("La palabra correcta es -", palabra_selec, "-", "꒰⑅•ᴗ•⑅꒱")
                sleep(5)
                clear()
                break
            if aciertos == 0:
                print("Has perdido!!")
                print("La palabra correcta era ", palabra_selec, "(✖╭╮✖)")
            sleep(4)
            clear()

        #Preguntamos al usuariosi desea continuar con el juego
        pregunta = input("¿Deseas seguir jugando? si / no: ")
        if pregunta == "si":
            print("Enhorabuena sigamos adivinando palabras ٩(^‿^)۶")
        else:
            print("¡Ah que Sad! see you later (✖╭╮✖)")    
            sleep(2)
            clear()  
            break             