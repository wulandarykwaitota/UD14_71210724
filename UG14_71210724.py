class Node: 
    def __init__(self,name, value):
        self._name = name 
        self._value = value

class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    #menambah vertex (Node) baru ke dalam Graph
    def addVertex(self, name, value):
        if name not in self._data:
            self._data[name] = set()
        node = Node(name, value)
        if name not in self._data.keys():
            setEdge = set()
            listData = [setEdge, node]
            self._data[name] = listData

    def vertex(self):
        print("\n== Seluruh Node == ")
        for key, value in self._data.items():
            print(key, value)
        print()

    def addEdge(self, x, y):
       if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)
    

    def edge(self):
        print("== Seluruh Edge == ")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key + item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge :
            print(item, end= ' ')
        print("\n")
    
    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        print("Traversing BFS = ", end = "")
        visited = []
        listQueue = []
        visited.append(node)
        listQueue.append(node)

        while listQueue:
            n = listQueue.pop(0)
            for item in self._data[n]:
                if item not in visited:
                    visited.append(item)
                    listQueue.append(item)
            print(n, end = ' ')
        print("\n")

graph = Graph()
graph.addVertex("a", 2)
graph.addVertex("b", 2)
graph.addVertex("c", 4)
graph.addVertex("d", 3)
graph.addVertex("e", 4)
graph.addVertex("f", 3)
graph.addVertex("g", 3)
graph.addVertex("h", 3)

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('d', 'e')
graph.addEdge('f', 'h')
graph.addEdge('g', 'f')

graph.vertex()
graph.edge()

graph.bfs('a')