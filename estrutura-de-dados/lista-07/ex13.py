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
    graph = Graph(12)
    start = 0

    graph.add_edge(0, 1, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 3, 6)

    graph.add_edge(0, 4, 7)
    graph.add_edge(1, 5, 8)
    graph.add_edge(2, 6, 6)
    graph.add_edge(3, 7, 8)

    graph.add_edge(4, 5, 8)
    graph.add_edge(5, 6, 6)
    graph.add_edge(6, 7, 8)

    graph.add_edge(4, 8, 2)
    graph.add_edge(5, 9, 3)
    graph.add_edge(6, 10, 1)
    graph.add_edge(7, 11, 8)

    graph.add_edge(8, 9, 3)
    graph.add_edge(9, 10, 1)
    graph.add_edge(10, 8, 11)

    D, vertex_Sequence = dijkstra(graph, start)

    print('distâncias:')
    print(D)
    #for key in D.keys():
    #   print(f'Distância de psp até {"ouriversaria" if key == ouriversaria else key} é {D[key]}')