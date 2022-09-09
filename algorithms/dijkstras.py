import sys
from graph.graph import Graph, GraphType


# Dijkstras Algorithm
# @note: This algorithm helps to find the shortest path between all the nodes in the graph
# from the source node by creating the shortest path tree.
# Time Complexity: O((V +E)log V) [V -> Vertices, E -> Edges]
class DijkstrasAlgorithm:

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
    
    def __find_next_min_distance_vertex(self, distance: dict[int, int], spt_vertices: set[int]):
        """
        This is a helper method to find the vertex that has min distance from the source node
        that is added to distance dictionary and not yet added to the shortest path tree
        :param distance: Dictionary of vertex distance from source
        :param spt_vertices: set of vertices that added to the shortest path tree
        :return: Next Min distance vertex to check 
        """
        next_min_distance_vertex = None
        for __vertex in self.graph.vertices:
            if __vertex not in spt_vertices and (
                    next_min_distance_vertex is None or
                    distance.get(__vertex, sys.maxsize) < distance[next_min_distance_vertex]
            ):
                next_min_distance_vertex = __vertex
        return next_min_distance_vertex

    def __resolve(self, starting_vertex) -> (dict[int, int], dict[int, list[int]]):
        """
        This is an internal method which resolves the problem by finding the shortest distances and paths.
        @step1 -> Initiate the found distances and shortest path with source vertex
        @step2 -> use __find_next_min_distance_vertex to get the next vertex
              -> (at first it returns the starting_index we are initiating with)
        @step3 -> iterate over the edges of min_distance_vertex to update the distance of each found vertex
        @step4 -> repeat step2 & step3 until all the vertices add to the spt (shortest path tree)
        :param starting_vertex: Source vertex
        :return: (Distance of all vertices from the source, the Shortest Path of all vertices from the source)
        """
        distance: dict[int, int] = dict()
        spt_vertices: set[int] = set()
        shortest_path: dict[int, list[int]] = dict()

        distance[starting_vertex] = 0
        shortest_path[starting_vertex] = [starting_vertex, ]

        for _ in range(self.graph.total_vertices):
            min_distance_vertex_index = self.__find_next_min_distance_vertex(distance, spt_vertices)
            spt_vertices.add(min_distance_vertex_index)

            for edge in self.graph.edges[min_distance_vertex_index]:
                to_vertex_distance = distance[min_distance_vertex_index] + edge.weight
                if edge.to_vertex not in spt_vertices and \
                        to_vertex_distance < distance.get(edge.to_vertex, sys.maxsize):
                    distance[edge.to_vertex] = to_vertex_distance
                    shortest_path[edge.to_vertex] = shortest_path[min_distance_vertex_index] + [edge.to_vertex]

        return distance, shortest_path

    def find_shortest_path(self, from_vertex, to_vertex):
        """
        This method is class endpoint to get the distance and path of source and end vertex
        :param from_vertex: source vertex
        :param to_vertex: end vertex
        :return: (distance, path)
        """
        distance, shortest_path = self.__resolve(from_vertex)
        return distance[to_vertex], shortest_path[to_vertex]


if __name__ == "__main__":
    # Creating a graph
    g: Graph = Graph(GraphType.BI_DIRECTIONAL, {1, 2, 3, 4, 5, 6})
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 5, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(3, 5, 7)
    g.add_edge(4, 6, 1)
    g.add_edge(5, 6, 1)

    for vertex in g.vertices:
        d, p = DijkstrasAlgorithm(g).find_shortest_path(1, vertex)
        print(f"Distance from vertex({1}) to vertex({vertex}): {d}")
        print(f"Path is [{' -> '.join(map(str, p))}]\n")
