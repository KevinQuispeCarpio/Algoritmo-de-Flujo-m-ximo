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

# Solicitamos al usuario ingresar el número de nodos
n = int(input("Ingrese el número de nodos: "))

# Creamos una matriz de adyacencia inicialmente vacía
graph = []
for i in range(n):
    # Solicitamos al usuario que ingrese los valores para cada fila de la matriz
    row = list(map(int, input(f"Ingrese los valores para la fila {i+1}, separados por espacios: ").split()))
    graph.append(row)

# Creamos el grafo a partir de la matriz de adyacencia
g = Graph(graph)

# Solicitamos al usuario que ingrese el nodo fuente y el nodo sumidero
source = int(input("Ingrese el nodo fuente: "))
sink = int(input("Ingrese el nodo sumidero: "))

# Mostramos el resultado
print ("El flujo máximo posible es %d " % g.FordFulkerson(source, sink))
