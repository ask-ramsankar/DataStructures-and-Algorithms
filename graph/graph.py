from enum import Enum


class GraphType(Enum):
    UNI_DIRECTIONAL = 0
    BI_DIRECTIONAL = 1


class Edge:
    def __init__(self, vertex1: int, vertex2: int, weight: int = 1):
        self.from_vertex = vertex1
        self.to_vertex = vertex2
        self.weight = weight


class Graph:

    def __init__(self, graph_type: GraphType, vertices: set[int]):
        self.vertices: set[int] = vertices
        self.total_vertices: int = len(vertices)
        self.edges: dict[int, list[Edge]] = dict()
        self.graph_type: GraphType = graph_type
        assert self.total_vertices > 1, "Total vertices should be greater than 1"

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int = 1):
        if self.graph_type == GraphType.UNI_DIRECTIONAL:
            self.edges[from_vertex] = self.edges.get(from_vertex, list()) + [Edge(from_vertex, to_vertex, weight)]
        elif self.graph_type == GraphType.BI_DIRECTIONAL:
            self.edges[from_vertex] = self.edges.get(from_vertex, list()) + [Edge(from_vertex, to_vertex, weight)]
            self.edges[to_vertex] = self.edges.get(to_vertex, list()) + [Edge(to_vertex, from_vertex, weight)]
        else:
            raise TypeError("Invalid graph type")
