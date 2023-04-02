import tkinter as tk
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph # grafo residual
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
    
    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

# Crear una ventana
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Máximo flujo en un grafo")

# Crear una etiqueta para el número de nodos
label_n = tk.Label(ventana, text="Ingrese el número de nodos:")
label_n.grid(column=0, row=0)

# Crear un campo de entrada para el número de nodos
entrada_n = tk.Entry(ventana)
entrada_n.grid(column=1, row=0)

# Crear una etiqueta para la matriz de adyacencia
label_matriz = tk.Label(ventana, text="Ingrese la matriz de adyacencia:")
label_matriz.grid(column=0, row=1)

# Crear un campo de entrada para la matriz de adyacencia
entrada_matriz = tk.Entry(ventana)
entrada_matriz.grid(column=1, row=1)

# Crear una etiqueta para el nodo fuente
label_source = tk.Label(ventana, text="Ingrese el nodo fuente:")
label_source.grid(column=0, row=2)

# Crear un campo de entrada para el nodo fuente
entrada_source = tk.Entry(ventana)
entrada_source.grid(column=1, row=2)

# Crear una etiqueta para el nodo sumidero
label_sink = tk.Label(ventana, text="Ingrese el nodo sumidero:")
label_sink.grid(column=0, row=3)

# Crear un campo de entrada para el nodo sumidero
entrada_sink = tk.Entry(ventana)
entrada_sink.grid(column=1, row=3)

# Crear una etiqueta para el resultado
resultado = tk.Label(ventana, text="")
resultado.grid(column=0, row=4, columnspan=2)

# Crear una función para calcular el flujo máximo y mostrarlo en una etiqueta
def calcular_flujo():
    n = int(entrada_n.get())
    graph = []
    matriz_entrada = entrada_matriz.get()
    for i in range(n):
        row = list(map(int, matriz_entrada.split()[i*n:(i+1)*n]))
        graph.append(row)

    g = Graph(graph)
    source = int(entrada_source.get())
    sink = int(entrada_sink.get())
    flujo = g.FordFulkerson(source, sink)
    
    resultado.configure(text="Flujo máximo: {}".format(flujo))

# Crear un botón para calcular el flujo máximo
boton_calcular = tk.Button(ventana, text="Calcular flujo máximo", command=calcular_flujo)
boton_calcular.grid(column=0, row=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()
