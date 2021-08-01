# minDistance for vertex: Vertex: id:2 name:City2 minDistance:68 previousVertex:Vertex: id:1 name:City1 minDistance:53 previousVertex:Vertex: id:3 name:City3 minDistance:29 previousVertex:Vertex: id:0 name:City0 minDistance:0 previousVertex:None edges:[, ]


class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float("inf")
        self.previousVertex = None


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        source = self.getTarget(sourceId)
        source.minDistance = 0
        vertexesStack = [source]

        while len(vertexesStack) > 0:
            vertex = vertexesStack.pop(0)
            for edge in vertex.edges:
                targetVertex = edge.target
                for vert in self.vertexes:
                    if (targetVertex == vert.id and (vertex.minDistance + edge.weight) < vert.minDistance):
                        vert.minDistance = vertex.minDistance + edge.weight
                        vert.previousVertex = vertex
                        vertexesStack.append(vert)

    def getTarget(self, targetVertexId):
        for vertex in self.vertexes:
            if vertex.id == targetVertexId:
                return vertex

    def getShortestPathTo(self, targetId):
        targetVertex = self.getTarget(targetId)
        vertexes = []
        while True:
            if targetVertex is None:
                break
            vertexes.append(targetVertex)
            targetVertex = targetVertex.previousVertex
        return vertexes[::-1]


    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        for edge in edgesToVertexes:
            for vertex in self.vertexes:
                if vertex.id is edge.source:
                    vertex.edges.append(edge)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.previousVertex = None
            vertex.minDistance = float("inf")

    def getVertexes(self):
        return self.vertexes