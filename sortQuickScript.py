########################################################
# Sorting Algorithms | GUI + MatPlotLib Chart (Animado)
# Gustavo A. Cahua Carmona - 2021680055
# UPIH | IPN - 2MM6 22-1
# Proyecto | Entrega: Extraordinarios
########################################################
# MatPlotLib + Numpy
########################################################
#           Sort:
# Quick
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import random

def runQuick(nE):
            #Func: Crea un Chart animado y reproduce los cambias en el Array de acuerdo al algoritmo de ordenamiento
            #Func: ejecuta y crea un chart, runBubble(1, numero de elementos en el array)

      class TrackedArray():         #Clase: monitorea los datos cambiante del array para poder crear la animacion

            def __init__(self, arr):            #__init__
                  self.arr = np.copy(arr)       #Copia del arr original por uno creado en la Clase
                  self.reset()

            def reset(self):                    #Vacia los valores de los arrays de monitoreo
                  self.indicies = []
                  self.values = []
                  self.access_type = []
                  self.full_copies = []

            def track(self, key, access_type):        #Guarda los valores en los arrays de monitoreo
                  self.indicies.append(key)           #Guarda el valor del elemento que esta moviendose en el chart
                  self.values.append(self.arr[key])   #Guarda el indice del elemento en el arr copia
                  self.access_type.append(access_type)      #Guarda el tipo de accion que se ejecuta en el elemento
                  self.full_copies.append(np.copy(self.arr)) #crea una tercera copia del arr

            def GetActivity(self, idx=None):          #Func: retorna valores procesados del track hacia la animacion
                  if isinstance(idx, type(None)):
                        return [(i, op) in zip(self.indicies, self.access_type)]
                  else:
                        return (self.indicies[idx], self.access_type[idx])

            def __getitem__(self, key):               #Func: para cada valor, si se accede a el, se regresa
                  self.track(key, "get")              #el elemento + el tipo de acceso (get)
                  return self.arr.__getitem__(key)    #<- retorno de tipo de acceso + elemento

            def __setitem__(self, key, value):        #Func: para cada valor, si se cambia de lugar, se regresa
                  self.arr.__setitem__(key, value)    #el elemento + el tipo de acceso (set)
                  self.track(key, "set")              #<- retorno de tipo de acceso + elemento

            def __len__(self):            #Toma la longitud del arr y lo regresa
                  return self.arr.__len__()

      N = nE            #El numero de elementos en el array (N) se toma de los parametros de entra (ne=tempElement)
      arr = np.linspace(0, N, N)          #Array de N elementos, del 0 hasta N
      np.random.shuffle(arr)              #Mueve los valores del arr de forma aleatoria
      arr = TrackedArray(arr)

      #############################################################################
      #Algoritmo de ordenamiento Quick
      #https://www.geeksforgeeks.org/quick-sort/?ref=lbp

      #Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
      #It picks an element as pivot and partitions the given array around the picked pivot.
      #There are many different versions of quickSort that pick pivot in different ways.

      #The key process in quickSort is partition(). Target of partitions is, given an array
      #and an element x of array as pivot, put x at its correct position in sorted array and
      #put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
      #All this should be done in linear time.

      sorter = "Quick"

      def partition(start, end, array):

                  # Initializing pivot's index to start
            pivot_index = start
            pivot = array[pivot_index]

                  # This loop runs till start pointer crosses
                  # end pointer, and when it does we swap the
                  # pivot with element on end pointer
            while start < end:

                        # Increment the start pointer till it finds an
                        # element greater than  pivot
                  while start < len(array) and array[start] <= pivot:
                        start += 1

                        # Decrement the end pointer till it finds an
                        # element less than pivot
                  while array[end] > pivot:
                        end -= 1

                        # If start and end have not crossed each other,
                        # swap the numbers on start and end
                  if (start < end):
                        array[start], array[end] = array[end], array[start]

                  # Swap pivot element with element on end pointer.
                  # This puts pivot on its correct sorted place.
            array[end], array[pivot_index] = array[pivot_index], array[end]

                  # Returning end pointer to divide the array into 2
            return end

            # The main function that implements QuickSort
      def quick_sort(start, end, array):

            if (start < end):
                        # p is partitioning index, array[p]
                        # is at right place
                  p = partition(start, end, array)

                        # Sort elements before partition
                        # and after partition
                  quick_sort(start, p - 1, array)
                  quick_sort(p + 1, end, array)

      quick_sort(0, len(arr) - 1, arr)
      ###############################################################################

      #Parametros de estilo del chart
      plt.rcParams["figure.figsize"] = (12, 8)
      plt.rcParams["font.size"] = 16
      plt.rcParams["figure.facecolor"] = "#212946"
      plt.rcParams["axes.facecolor"] = "#212946"
      plt.rcParams['text.color'] = "#BDCBDF"
      plt.rcParams['axes.labelcolor'] = "#BDCBDF"
      plt.rcParams['xtick.color'] = "#BDCBDF"
      plt.rcParams['ytick.color'] = "#BDCBDF"

      fig, ax = plt.subplots()      #Variables para le creacion del plot
      container = ax.bar(np.arange(0, len(arr), 1), arr, align="edge", width=0.5)   #Crea una grafica de barras
      ax.set_xlim(0, N)                                                             #con los parametros de arr
      ax.set(xlabel=f"{N} Elementos ", ylabel='Valor', title=f"{sorter} sort")      #Etiquetas
      txt = ax.text(1, N, "")                                                       #Numero de accesos en arr
      fig.tight_layout()

      def update(frame):            #Func: Actualiza la animacion, colores y tamaños
            txt.set_text(f"Accesos = {frame}")
            for (rectangle, height) in zip(container.patches, arr.full_copies[frame]): #Crea las barras para cada elemento
                  rectangle.set_height(height)
                  rectangle.set_color("#3DA2F9")

            idx, op = arr.GetActivity(frame)    #Obtiene la actividad guardada en arr.GetActivity
            if op == "get":                     #Cambia el color del elemento si es obteneido(get) a rosa
                  container.patches[idx].set_color("#FE53BB")
            elif op == "set":                   #Cambia el color del elemento si es colocada(set) a amarillo
                  container.patches[idx].set_color("#F5D300")
            return (*container, txt)

      #Creacion de la variable que ejecuta la animacion, toma la forma de la grafica creada y todos los frames creados
      anim = FuncAnimation(fig, update, frames=range(len(arr.full_copies)), blit=True, interval=0.1, repeat=False)
      plt.show()        #Abre el plot animado

if __name__=="__main__":
      runQuick(32)