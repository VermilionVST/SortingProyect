########################################################
# Sorting Algorithms | GUI + MatPlotLib Chart (Animado)
# Gustavo A. Cahua Carmona - 2021680055
# UPIH | IPN - 2MM6 22-1
# Proyecto | Entrega: Extraordinarios
########################################################
# MatPlotLib + Numpy
########################################################
#           Sort:
# Merge
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import random

def runMerge(nE):
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
      #Algoritmo de ordenamiento Merge
      #https://www.geeksforgeeks.org/merge-sort/

      #Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
      #It divides the input array into two halves, calls itself for the two halves,
      #and then merges the two sorted halves.

      sorter = "Merge"

      def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m
            L = [0] * (n1)
            R = [0] * (n2)

            for i in range(0, n1):
                  L[i] = arr[l + i]

            for j in range(0, n2):
                  R[j] = arr[m + 1 + j]

            i = 0  # Initial index of first subarray
            j = 0  # Initial index of second subarray
            k = l  # Initial index of merged subarray

            while i < n1 and j < n2:
                  if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                  else:
                        arr[k] = R[j]
                        j += 1
                  k += 1

            while i < n1:
                  arr[k] = L[i]
                  i += 1
                  k += 1

            while j < n2:
                  arr[k] = R[j]
                  j += 1
                  k += 1

      def mergeSort(arr, l, r):
            if l < r:
                        # Same as (l+r)//2, but avoids overflow for
                        # large l and h
                  m = l + (r - l) // 2

                        # Sort first and second halves
                  mergeSort(arr, l, m)
                  mergeSort(arr, m + 1, r)
                  merge(arr, l, m, r)

      mergeSort(arr, 0, N - 1)
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
      runMerge(32)