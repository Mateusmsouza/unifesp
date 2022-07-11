from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight



def dijkstra(graph, start_vertex):
    vertex_sequence = []
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        vertex_sequence.append(current_vertex)
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        print(f'cost to go from {current_vertex} to {neighbor} is {new_cost}, better than {old_cost}')
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D, vertex_sequence

if __name__ == '__main__':
    psp = 1
    ouriversaria = 0

    graph = Graph(15)
    graph.add_edge(psp, 13, 10)
    graph.add_edge(psp, 2, 8)
    graph.add_edge(13, 12, 13)
    graph.add_edge(12, 11, 8)

    graph.add_edge(2, 14, 7)
    graph.add_edge(2, 3, 10)
    graph.add_edge(14, 13, 6)
    graph.add_edge(14, 6, 8)
    
    graph.add_edge(3, 5, 9)
    graph.add_edge(5, 6, 4)
    graph.add_edge(5, 7, 3)
    graph.add_edge(3, 4, 12)
    graph.add_edge(7, 6, 5)
    
    graph.add_edge(4, 8, 14)
    graph.add_edge(8, 7, 9)
    graph.add_edge(8, ouriversaria, 10)
    graph.add_edge(9, ouriversaria, 9)
    graph.add_edge(11, 10, 11)
    graph.add_edge(11, 9, 16)
    graph.add_edge(10, 9, 4)

    D, vertex_Sequence = dijkstra(graph, psp)

    print('distâncias:')
    print(D)
    2 > 14
    #for key in D.keys():
    #   print(f'Distância de psp até {"ouriversaria" if key == ouriversaria else key} é {D[key]}')