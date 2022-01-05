########################################################
# Sorting Algorithms | GUI + MatPlotLib Chart (Animado)
# Gustavo A. Cahua Carmona - 2021680055
# UPIH | IPN - 2MM6 22-1
# Proyecto | Entrega: Extraordinarios
########################################################
# MatPlotLib + Numpy
########################################################
#           Sort:
# Cocktail Shaker

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import random

def runShaker(nE):
            # Func: Crea un Chart animado y reproduce los cambias en el Array de acuerdo al algoritmo de ordenamiento
            # Func: ejecuta y crea un chart, runBubble(1, numero de elementos en el array)

      class TrackedArray():  # Clase: monitorea los datos cambiante del array para poder crear la animacion

            def __init__(self, arr):  # __init__
                  self.arr = np.copy(arr)  # Copia del arr original por uno creado en la Clase
                  self.reset()

            def reset(self):  # Vacia los valores de los arrays de monitoreo
                  self.indicies = []
                  self.values = []
                  self.access_type = []
                  self.full_copies = []

            def track(self, key, access_type):  # Guarda los valores en los arrays de monitoreo
                  self.indicies.append(key)  # Guarda el valor del elemento que esta moviendose en el chart
                  self.values.append(self.arr[key])  # Guarda el indice del elemento en el arr copia
                  self.access_type.append(access_type)  # Guarda el tipo de accion que se ejecuta en el elemento
                  self.full_copies.append(np.copy(self.arr))  # crea una tercera copia del arr

            def GetActivity(self, idx=None):  # Func: retorna valores procesados del track hacia la animacion
                  if isinstance(idx, type(None)):
                        return [(i, op) in zip(self.indicies, self.access_type)]
                  else:
                        return (self.indicies[idx], self.access_type[idx])

            def __getitem__(self, key):  # Func: para cada valor, si se accede a el, se regresa
                  self.track(key, "get")  # el elemento + el tipo de acceso (get)
                  return self.arr.__getitem__(key)  # <- retorno de tipo de acceso + elemento

            def __setitem__(self, key, value):  # Func: para cada valor, si se cambia de lugar, se regresa
                  self.arr.__setitem__(key, value)  # el elemento + el tipo de acceso (set)
                  self.track(key, "set")  # <- retorno de tipo de acceso + elemento

            def __len__(self):  # Toma la longitud del arr y lo regresa
                  return self.arr.__len__()

      N = nE  # El numero de elementos en el array (N) se toma de los parametros de entra (ne=tempElement)
      arr = np.linspace(0, N, N)  # Array de N elementos, del 0 hasta N
      np.random.shuffle(arr)  # Mueve los valores del arr de forma aleatoria
      arr = TrackedArray(arr)

      #############################################################################
      ############################################################################
      # Algoritmo de ordenamiento Cocktail Shaker
      #https://www.geeksforgeeks.org/cocktail-sort/

      #Each iteration of the algorithm is broken up into 2 stages:

      #     The first stage loops through the array from left to right, just like the Bubble Sort.
      #During the loop, adjacent items are compared and if value on the left is greater than the value on the right, then values are swapped.
      #At the end of first iteration, largest number will reside at the end of the array.

      #     The second stage loops through the array in opposite direction- starting from the item just before
      #the most recently sorted item, and moving back to the start of the array. Here also, adjacent items are
      #compared and are swapped if required.

      sorter = "Coctail Shaker"

      def cocktailSort(arr):
            n = len(arr)
            swapped = True
            start = 0
            end = n - 1
            while (swapped == True):

                  # reset the swapped flag on entering the loop,
                  # because it might be true from a previous
                  # iteration.
                  swapped = False

                  # loop from left to right same as the bubble
                  # sort
                  for i in range(start, end):
                        if (arr[i] > arr[i + 1]):
                              arr[i], arr[i + 1] = arr[i + 1], arr[i]
                              swapped = True

                  # if nothing moved, then array is sorted.
                  if (swapped == False):
                        break

                  # otherwise, reset the swapped flag so that it
                  # can be used in the next stage
                  swapped = False

                  # move the end point back by one, because
                  # item at the end is in its rightful spot
                  end = end - 1

                  # from right to left, doing the same
                  # comparison as in the previous stage
                  for i in range(end - 1, start - 1, -1):
                        if (arr[i] > arr[i + 1]):
                              arr[i], arr[i + 1] = arr[i + 1], arr[i]
                              swapped = True

                  # increase the starting point, because
                  # the last stage would have moved the next
                  # smallest number to its rightful spot.
                  start = start + 1
      cocktailSort(arr)
      ###############################################################################

      # Parametros de estilo del chart
      plt.rcParams["figure.figsize"] = (12, 8)
      plt.rcParams["font.size"] = 16
      plt.rcParams["figure.facecolor"] = "#212946"
      plt.rcParams["axes.facecolor"] = "#212946"
      plt.rcParams['text.color'] = "#BDCBDF"
      plt.rcParams['axes.labelcolor'] = "#BDCBDF"
      plt.rcParams['xtick.color'] = "#BDCBDF"
      plt.rcParams['ytick.color'] = "#BDCBDF"

      fig, ax = plt.subplots()  # Variables para le creacion del plot
      container = ax.bar(np.arange(0, len(arr), 1), arr, align="edge", width=0.5)  # Crea una grafica de barras
      ax.set_xlim(0, N)  # con los parametros de arr
      ax.set(xlabel=f"{N} Elementos ", ylabel='Valor', title=f"{sorter} sort")  # Etiquetas
      txt = ax.text(1, N, "")  # Numero de accesos en arr
      fig.tight_layout()

      def update(frame):  # Func: Actualiza la animacion, colores y tamaños
            txt.set_text(f"Accesos = {frame}")
            for (rectangle, height) in zip(container.patches,
                                           arr.full_copies[frame]):  # Crea las barras para cada elemento
                  rectangle.set_height(height)
                  rectangle.set_color("#3DA2F9")

            idx, op = arr.GetActivity(frame)  # Obtiene la actividad guardada en arr.GetActivity
            if op == "get":  # Cambia el color del elemento si es obteneido(get) a rosa
                  container.patches[idx].set_color("#FE53BB")
            elif op == "set":  # Cambia el color del elemento si es colocada(set) a amarillo
                  container.patches[idx].set_color("#F5D300")
            return (*container, txt)

      # Creacion de la variable que ejecuta la animacion, toma la forma de la grafica creada y todos los frames creados
      anim = FuncAnimation(fig, update, frames=range(len(arr.full_copies)), blit=True, interval=0.1, repeat=False)
      plt.show()  # Abre el plot animado


if __name__=="__main__":      #Puede ejecutar la animacion sin la GUI
      runShaker(32)