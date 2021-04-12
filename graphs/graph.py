from graphviz import Digraph
from graphviz import Graph as Graphviz

# Attribute to indicate if is a directed graph
DIRECTED = "DIRECTED"

# Render images graphviz
RENDER = False

class Graph:
    def __init__(self, vertices = None, edges = None, attr = {}):
        """__init__ initializes Graph object. Graph stores vertices and edges
           param vertices: Dictionary with vertices
           param edges:    Dictionary with edges
           param attr:     Properties of graph
        """
        if vertices == None:
            vertices = {} 
        self.vertices = vertices

        if edges == None:
            edges = {} 
        self.edges = edges

        self.attr = attr

    
    def add_vertex(self, vertex):
        """ add_vertex add vertex to graph's vertices if there is not other vertex with same id
            param vertex: vertex to add in graph
        """
        if vertex.id not in self.vertices.keys():
            self.vertices[vertex.id] = vertex 
    
    def get_vertices(self):
        return self.vertices
    
    def get_vertex(self, id):
        return self.vertices[id]

    def add_edge(self, edge, directed = False, auto = False):
        """ Add edge to source edges if there is no other edge with same source and target
            :param edge: edge to insert
            :param directed: enable graph directed
            :param auto: allow auto-cycle (loops)
        """
        (v1,v2) = edge.get_id()
        if v1 in self.vertices.keys() and v2 in self.vertices.keys():
            if directed:
                if auto:
                    self.edges[edge.get_id()] = edge
                else:
                    if v1 != v2:
                        self.edges[edge.get_id()] = edge
            else:
                if self.edges.get((v2,v1)) is None:
                    if auto:
                        self.edges[edge.get_id()] = edge
                    else:
                        if v1 != v2:
                            self.edges[edge.get_id()] = edge

    def get_edges(self):
        """ edges create edges of the grap
        """
        edges = []
        for (key, target) in self.edges.keys():
            edges.append((key,target))
        return edges
    
    def get_edges_by_vertex(self, id):
        """ 
        Find the edges that are incident in vertex with id paramater
        param id: Vertex identifier in the graph
        return: list of edges
        """
        edges = []
        for (source, target) in self.edges.keys():
            if source == id or target == id:
                edges.append((source, target))
        return edges


    def create_graphviz(self, file_name):
        dot = Graphviz()

        # Review attribute directed of graph
        if DIRECTED in self.attr:
            if self.attr[DIRECTED]: 
                dot = Digraph()
            else:
                dot = Graphviz()

        # Map graph to graphviz structure    
        for n in list(self.vertices.keys()):
           dot.node(str(n),str(n))
        for e in self.get_edges():
            (s,t) = e
            dot.edge(str(s),str(t))
        file = open("./images/gv/"+file_name+".gv", "w")
        file.write(dot.source)
        file.close()
        return dot

