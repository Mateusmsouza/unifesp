
def breadth_first_search(graph, s):
    color = {}
    distance = {}
    pi = {}
    adj = {}
    for adjacency_list in graph:
        vertex = adjacency_list[0]
        color[vertex] = 'white'
        distance[vertex] = -1
        pi[vertex] = None
        adj[vertex] = adjacency_list[1:]
    
    color[s] = 'grey'
    distance[s] = 0
    pi[s] = None

    queue = []
    queue.append(s)

    while queue:
        vertex = queue.pop()
        for neighbor in adj[vertex]:
            if color[neighbor] == 'white':
                color[neighbor] = 'grey'
                distance[neighbor] = distance[vertex] + 1
                pi[neighbor] = vertex
                queue.append(neighbor)
        color[vertex] = 'black'

    return distance, pi

tempo = 0
pi = {}
distance = {}
color = {}
adj = {}
f = {}

def depth_first_search_node(graph, u):
    global tempo
    global pi
    global distance
    global color
    global adj

    color[u] = 'grey'
    tempo += 1
    distance[u] = tempo

    for neighbor in adj[u]:
        if color[neighbor] == 'white':
            pi[neighbor] = u
            depth_first_search_node(graph, neighbor)
    color[u] = 'black'
    tempo += 1
    f[u] = tempo



def depth_first_search(graph, s):
    global tempo
    global pi
    global distance
    global color
    global adj
    global f

    color = {}
    pi = {}
    adj = {}
    for adjacency_list in graph:
        vertex = adjacency_list[0]
        color[vertex] = 'white'
        pi[vertex] = None
        adj[vertex] = adjacency_list[1:]

    for adjacency_list in graph:
        vertex = adjacency_list[0]
        if color[vertex] == 'white':
            depth_first_search_node(graph, vertex)
    return distance, f, pi

def main():
    graph = [
        ['A', 'B', 'I'],
        ['B', 'C', 'D'],
        ['C', 'E', 'F'],
        ['D', 'A', 'E', 'G'],
        ['E', 'F', 'B'],
        ['F', 'H'],
        ['G', 'E', 'J', 'I'],
        ['H', 'E'],
        ['I', 'J'],
        ['J', 'H'],
    ]

    distance0, pi0 = breadth_first_search(graph, 'A')
    print(f'distance: {distance0}')
    print(f'π: {pi0}')
    print('========================')
    distance, f, pi = depth_first_search(graph, 'A')
    print(f'distance: {distance}')
    print(f'f: {f}')
    print(f'π: {pi}')

if __name__ == '__main__':
    main()
