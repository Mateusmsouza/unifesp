
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
        ['a', 'b', 'e'],
        ['b', 'a', 'c', 'f'],
        ['c', 'b', 'd'],
        ['d', 'c', 'g', 'h'],
        ['e', 'a', 'f'],
        ['f', 'b', 'e', 'g', 'j'],
        ['g', 'c', 'f', 'h', 'k'],
        ['h', 'd', 'g', 'l'],
        ['i', 'e', 'j', 'm'],
        ['j', 'f', 'i', 'k', 'n'],
        ['k', 'g', 'j', 'l', 'o'],
        ['l', 'h', 'k', 'p'],
        ['m', 'i', 'n'],
        ['n', 'm', 'j', 'o'],
        ['o', 'n', 'k', 'p'],
        ['p', 'o', 'l']
    ]

    #distance, pi = breadth_first_search(graph, 'a')
    distance, f, pi = depth_first_search(graph, 'a')
    print(f'distance: {distance}')
    print(f'f: {f}')
    print(f'π: {pi}')

