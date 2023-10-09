from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def addBiEdge(self, f, t, weight = 1):
        self.addEdge(f,t,weight)
        self.addEdge(t,f,weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def shortest_path(self, vertex):
        distances = {v: float('inf') for v in self.vertList}
        distances[vertex.getId()] = 0
        paths = {vertex.getId(): ()}
        queue = deque([(0, vertex)])

        while queue:
            current_distance, current_vertex = queue.popleft()

            if current_distance > distances[current_vertex.getId()]:
                continue

            for neighbor in self.vertList[current_vertex.getId()].getConnections():
                weight = self.vertList[current_vertex.getId()].getWeight(neighbor)
                distance = current_distance + weight

                if distance < distances[neighbor.getId()]:
                    distances[neighbor.getId()] = distance
                    paths[neighbor.getId()] = paths[current_vertex.getId()] + (neighbor.getId(),)
                    queue.append((distance, neighbor))

        shortest_paths = set()
        for v in self.vertList:
            if distances[v] != float('inf') and v != 'Kevin Bacon':
                shortest_paths.add((v, (vertex.getId(), ) + paths[v], distances[v]))
            elif distances[v] != float('inf') and v == 'Kevin Bacon':
                shortest_paths.add((v, paths[v], distances[v]))


        return shortest_paths


