from queue import PriorityQueue

numbers = {
        0:'a',
        1:'b',
        2:'c',
        3:'d',
        4:'e',
        5:'f',
        6:'g',
        7:'h',
        8:'i',
        9:'j',
        10:'k',
        11:'l',
        12:'m',
        13:'n',
        14:'o',
        15:'p'}

letters = {
        'a':0,
        'b':1,
        'c':2,
        'd':3,
        'e':4,
        'f':5,
        'g':6,
        'h':7,
        'i':8,
        'j':9,
        'k':10,
        'l':11,
        'm':12,
        'n':13,
        'o':14,
        'p':15}

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
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D, vertex_sequence

if __name__ == '__main__':
    graph = Graph(10)
    graph.add_edge(letters['a'], letters['b'], 6)
    graph.add_edge(letters['a'], letters['i'], 9)
    graph.add_edge(letters['b'], letters['c'], 3)
    graph.add_edge(letters['b'], letters['d'], 3)
    graph.add_edge(letters['c'], letters['e'], 2)
    graph.add_edge(letters['c'], letters['f'], 2)
    graph.add_edge(letters['d'], letters['a'], 4)
    graph.add_edge(letters['d'], letters['e'], 4)
    graph.add_edge(letters['d'], letters['g'], 6)
    graph.add_edge(letters['e'], letters['b'], 1)
    graph.add_edge(letters['e'], letters['f'], 8)
    graph.add_edge(letters['g'], letters['e'], 6)
    graph.add_edge(letters['g'], letters['i'], 2)
    graph.add_edge(letters['g'], letters['j'], 2)
    graph.add_edge(letters['h'], letters['e'], 3)
    graph.add_edge(letters['i'], letters['j'], 1)
    graph.add_edge(letters['j'], letters['h'], 4)

    D, vertex_Sequence = dijkstra(graph, letters['a'])
    print('distâncias:')
    for key in D.keys():
        print(f'Distância de A até {str.upper(numbers[key])} é {D[key]}')

    print('Sequência de vértices visitados:')    
    for i in vertex_Sequence:
        print(str.upper(numbers[i]), end=', ')
