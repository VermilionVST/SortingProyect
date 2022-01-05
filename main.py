########################################################
# Sorting Algorithms | GUI + MatPlotLib Chart (Animado)
# Gustavo A. Cahua Carmona - 2021680055
# UPIH | IPN - 2MM6 22-1
# Proyecto | Entrega: Extraordinarios
########################################################
# MatPlotLib + Tkinter + Numpy
########################################################
# {
#           Sort:
# Bubble
# Cocktail Shaker
# Heap
# Insertion
# Merge
# Quick
# Selection
# Shell
# }


from pygame import mixer
from tkinter import *
from tkinter import font as tkFont
from sortHeapScript import runHeap
from sortQuickScript import runQuick
from sortShellScript import runShell
from sortMergeScript import runMerge
from sortBubbleScript import  runBubble
from sortSelectionScript import runSelection
from sortInsertionScript import runInsertion
from sortCocktailShakerScript import runShaker


# Main Script


########################################################################################################################
tempElements=32 #32 Elementos por defecto
mixer.init() #Inicializacion de sonido

def player(x):          #Func 2 Sonidos
      if x==0:
            mixer.music.load("pesIMGs/WarzoneLegendaryFX.mp3") #Sonido 1
            mixer.music.play(loops=0)
      elif x==1:
            mixer.music.load("pesIMGs/pick.mp3") #Sonido 2
            mixer.music.play(loops=0)


def n32Elements():            #Func Cambio en el numero de elementos (32) + sonido al click en el selector 32
      global tempElements
      tempElements=32
      labelNE['background']="#09EAF0" #Cambio de color del indicador de elementos actuales (azul)
      player(1) #Sonido 2

def n64Elements():            #Func Cambio en el numero de elementos (64) + sonido al click en el selector 64
      global tempElements
      tempElements=64
      labelNE['background'] ="#98FF6A" #Cambio de color del indicador de elementos actuales (verde)
      player(1) #Sonido 2

def n128Elements():           #Func Cambio en el numero de elementos (128) + sonido al click en el selector 128
      global tempElements
      tempElements=128
      labelNE['background'] ="#F5D300" #Cambio de color del indicador de elementos actuales (amarillo)
      player(1) #Sonido 1

def n256Elements():           #Func Cambio en el numero de elementos (256) + sonido al click en el selector 256
      global tempElements
      tempElements=256
      labelNE['background'] ="#FF4900" #Cambio de color del indicador de elementos actuales (rojo)
      player(0) #Sonido 1

########################################################################################################################

def callBackQuickSort():            #Call - scrip | Quick sort (sortQuickScript.py)
      player(1)  # Sonido 2
      runQuick(tempElements)      #1 (Llave) + nElementos (tempElements)


def callBackBubbleSort():           #Call - scrip | Bubble sort (sortBubbleScript.py)
      player(1)  # Sonido 2
      runBubble(tempElements)

def callBackShellSort():            #Call - scrip | Shell sort (sortShellScript.py)
      player(1)  # Sonido 2
      runShell(tempElements)

def callBackSelectionSort():        #Call - scrip | Selection sort (sortSelectionScript.py)
      player(1)  # Sonido 2
      runSelection(tempElements)

def callBackMergeSort():            #Call - scrip | Merge sort (sortMergeScript.py)
      player(1)  # Sonido 2
      runMerge(tempElements)

def callBackInsertion():            #Call - scrip | Insertion sort (sortInsertionScript.py)
      player(1)  # Sonido 2
      runInsertion(tempElements)

def callBackCocktailSahkerSort():   #Call - scrip | CocktailShaker sort (sortCocktailShakerScript.py)
      player(1)  # Sonido 2
      runShaker(tempElements)

def callBackHeapSort():             #Call - scrip | Heap sort (sortHeapScript.py)
      player(1)  # Sonido 2
      runHeap(tempElements)

########################################################################################################################

def setPOS():           #Func Toma resolucion de pantalla, ubica centro, posiciona GUI al centro
      xPos = int((mainWD.winfo_screenwidth() / 2) - (1280 / 2))   #Coordenada x     |x_y---------|
      yPos = int((mainWD.winfo_screenheight() / 2) - (720 / 2))   #Coordenada y     |------------|
                                                                        #           |------------| <- Main Window
      mainWD.geometry(f'1280x720+{xPos}+{yPos}')      #Set Geometry: HDres (1280x720) -> Posicion:
      mainWD.config(bg="#2F313D")                           #     |--------------------------------|
                                                            #     |     |°x_y---  <- Main Window   |
                                                            #     |     |          |          |    |
                                                            #     |     |       --°--(xPos , yPos) |
                                                            #     |     |         |           |    |
                                                            #     |     |---------------------|    |
                                                            #     |--------------------------------| <- Tu pantalla
mainWD = Tk() #Main Window en variable
setPOS()

font = tkFont.Font(family="roboto", size=12,weight='bold')              #Font 1
fontElements = tkFont.Font(family="roboto", size=8, weight='bold')      #Font 2

########################################################################################################################

def butonStyle(w,h,x,y,text,bcolor,fcolor,cmd,k):           #Func crea botones y ls estiliza dea acuerdo a los

                                                                  #parametros de entrada
      def on_enter(e):        #Func(e) que cambia los colores del boton cuando MouseOver
            myButton['background']=bcolor       #Parametro Color 1
            myButton['foreground']=fcolor       #Parametro Color 2

      def on_leave(e):        #Func(e) que cambia los colores del boton cuando MouseOut
            myButton['background']=fcolor       #Parametro Color 2
            myButton['foreground']=bcolor       #Parametro Color 1

      myButton = Button(mainWD, width=w, height=h, text=text,     #Creacion de boton(Tkinter) + set Parametros
                                    fg=bcolor,
                                    bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=cmd,
                                    cursor="hand2")

      if k==0:                                  #Para botones de k==0 (Botones nElementos)
            myButton["font"]=fontElements       #Font2
      elif k==1:                                #Para botones de k==1 (Botones Sorts)
            myButton["font"] = font             #Font1

      myButton.bind("<Enter>", on_enter)        #Call: MouseOver Func(e)
      myButton.bind("<Leave>",on_leave)         #Call: MouseOut Func(e)
      myButton.place(x=x,y=y)

########################################################################################################################

global allIMGs, count         #Variables para carrusel de imagenes
count = -1                    #Ultima posicion en lista
allIMGs= [                                            #Lista de imagenes (PIL.ImageTK)
            PhotoImage(file="pesIMGs/bubbleIMG.png"),
            PhotoImage(file="pesIMGs/heapIMG.png"),
            PhotoImage(file="pesIMGs/insertionIMG.png"),
            PhotoImage(file="pesIMGs/mergeIMG.png"),
            PhotoImage(file="pesIMGs/quickIMG.png"),
            PhotoImage(file="pesIMGs/selectionIMG.png"),
            PhotoImage(file="pesIMGs/shakerIMG.png"),
            PhotoImage(file="pesIMGs/shellIMG.png")
      ]

canvaGalelry = Canvas(mainWD,width=870, height=680,highlightthickness=0)      #Canvas carrusel
canvaGalelry.place(x=300,y=20)
canvaGalelry.create_image(0, 0, image=allIMGs[0], anchor="nw")                #Inicia con Img1

def   next():           #Func carrusel de imgs

      global count
      if count==7:      #Cuando count == ultima posicion, reset count
            canvaGalelry.create_image(0, 0, image=allIMGs[0], anchor="nw")    #Set imagen
            count=0
      else:             #Cambiar a la sig img
            canvaGalelry.create_image(0, 0, image=allIMGs[count+1], anchor="nw")    #Set imagen
            count+=1

      mainWD.after(1500,next) #Para cada ciclo, dormir 1500ms + llamada recursiva
next()

########################################################################################################################

labelNE=Label(mainWD,text="N Elementos")        #Label: Indicador de elementos actuales
labelNE['background'] = "#09EAF0"               #Colro por defecto: azul (32 Elementos)
labelNE.place(x=1199,y=598)

      #Palette {              #Paleta de 4 colores
palBP1_1="#51dbff"
palBP1_2="#cf6dde"
palBP1_3="#00ecc2"
palBP1_4="#ffc606"
      # }

      #Variables de cracion de botones con parametros de diseño
      # = butonStyle (ancho, alto, xPos, yPos, texto, bcolor, fcolor, funcion,tipo de boton)

      #Botones de seleccion de numero de elementos
button32=butonStyle(6,3,1190,624,"32","#09EAF0","#474A5C",n32Elements,0)
button64 = butonStyle(6,3,1235, 624, "64", "#98FF6A", "#474A5C", n64Elements,0)
button128 = butonStyle(6,3,1190, 672, "128", "#F5D300", "#474A5C", n128Elements,0)
button256 = butonStyle(6,3,1235, 672, "256", "#FF4900", "#474A5C", n256Elements,0)

      #Botones mostar Sorts
btn_QuickSort= butonStyle(30,4,0,0,"Quick Sort",palBP1_1,"#474A5C",callBackQuickSort,1)
btn_Bubble = butonStyle(30,4,0, 90, "Bubble Sort", palBP1_2, "#474A5C", callBackBubbleSort,1)
btn_Shell = butonStyle(30,4,0, 90*2, "Shell Sort", palBP1_3, "#474A5C", callBackShellSort,1)
btn_Selection = butonStyle(30,4,0, 90 * 3, "Selection Sort", palBP1_4, "#474A5C", callBackSelectionSort,1)
btn_Merge = butonStyle(30,4,0, 90 * 4, "Merge Sort", palBP1_1, "#474A5C", callBackMergeSort,1)
btn_Insertion = butonStyle(30,4,0, 90 * 5, "Insertion Sort", palBP1_2, "#474A5C", callBackInsertion,1)
btn_Shaker = butonStyle(30,4,0, 90 * 6, "Cocktail Shaker Sort", palBP1_3, "#474A5C", callBackCocktailSahkerSort,1)
btn_Heap = butonStyle(30,4,0, 90 * 7, "Heap Sort", palBP1_4, "#474A5C", callBackHeapSort,1)

if __name__=="__main__":
      mainWD.mainloop()       #Loop de eventos