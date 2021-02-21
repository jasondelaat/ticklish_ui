from dataclasses import dataclass
import math

@dataclass
class Vertex:
    x: int
    y: int
    
@dataclass
class Edge:
    start: Vertex
    end: Vertex
    
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, x, y):
        vertex = Vertex(x, y)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, start, end):
        edge = Edge(start, end)
        self.edges.append(edge)
        return edge

    def find_vertex(self, x, y):
        for v in self.vertices:
            dist = math.sqrt((v.x - x)**2 + (v.y - y)**2)
            if dist <= 6:
                return v
