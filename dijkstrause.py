from dijkstra import *

# minDistance for vertex(Vertex(id:2 name:City2 minDistance:68 previousVertex:Vertex(id:1 name:City1 minDistance:53 previousVertex:Vertex(id:3 name:City3 minDistance:29 previousVertex:Vertex(id:0 name:City0 minDistance:0 previousVertex:None edges:[, ]

# vertexes = [
#     Vertex(0, 'City0'),
#     Vertex(1, 'City1'),
#     Vertex(2, 'City2'),
#     Vertex(3, 'City3'),
#     Vertex(4, 'City4'),
#     Vertex(5, 'City5'),
#     Vertex(6, 'City6')
# ]
# edges = [
#     Edge(0, 3, 29),
#     Edge(0, 5, 58),
#     Edge(1, 6, 43),
#     Edge(1, 0, 48),
#     Edge(1, 2, 15),
#     Edge(1, 3, 3),
#     Edge(1, 4, 10),
#     Edge(2, 3, 28),
#     Edge(2, 5, 23),
#     Edge(3, 5, 99),
#     Edge(3, 6, 68),
#     Edge(3, 1, 24),
#     Edge(3, 0, 20),
#     Edge(4, 3, 43),
#     Edge(5, 1, 8),
#     Edge(5, 0, 96),
#     Edge(5, 4, 11),
#     Edge(5, 2, 48),
#     Edge(6, 4, 58),
#     Edge(6, 5, 84)
# ]
# Test graph
vertexes = [
    Vertex(0, "Redville"),
    Vertex(1, "Blueville"),
    Vertex(2, "Greenville"),
    Vertex(3, "Orangeville"),
    Vertex(4, "Purpleville"),
]
edges = [
    Edge(0, 1, 5),
    Edge(0, 2, 10),
    Edge(0, 3, 8),
    Edge(1, 0, 5),
    Edge(1, 2, 3),
    Edge(1, 4, 7),
    Edge(2, 0, 10),
    Edge(2, 1, 3),
    Edge(3, 0, 8),
    Edge(3, 4, 2),
    Edge(4, 1, 7),
    Edge(4, 3, 2),
]
# New Dijkstra created
dijkstra = Dijkstra()
# Graph created
dijkstra.createGraph(vertexes, edges)
# Getting all vertexes
dijkstraVertexes = dijkstra.getVertexes()
# Computing min distance for each vertex in graph
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print("Printing min distance from vertex:" + str(vertexToCompute.name))
    # Print minDitance from current vertex to each other
    for vertex in dijkstraVertexes:
        print("Min distance to:" + str(vertex.name) + " is " + str(vertex.minDistance))
    # Reset Dijkstra between counting
    dijkstra.resetDijkstra()
# Distance with path
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print("Printing min distance from vertex:" + str(vertexToCompute.name))
    # Print minDitance and path from current vertex to each other
    for vertex in dijkstraVertexes:
        print(":Min distance to " + str(vertex.name) + " is " + str(vertex.minDistance))
        print("Path is:", end=" ")
        # Get shortest path to target vertex
        path = dijkstra.getShortestPathTo(vertex.id)
        for vertexInPath in path:
            print(str(vertexInPath.name), end=" ")
        print()
    # Reset Dijkstra between counting
    dijkstra.resetDijkstra()