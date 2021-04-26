import collections

from graphviz import Digraph
from graphviz import Graph as Graphviz
from pygraph import edge

# Attribute to indicate if is a directed graph
DIRECTED = "DIRECTED"

# Render images graphviz
RENDER = False

# Attribute to inidcate if a vertes has been discovered
DISCOVERED = "DISCOVERED"


class Graph:
    def __init__(self, vertices=None, edges=None, attr={}):
        """__init__ initializes Graph object. Graph stores vertices and edges
           param vertices: Dictionary with vertices
           param edges:    Dictionary with edges
           param attr:     Properties of graph
        """
        if vertices is None:
            vertices = {}
        self.vertices = vertices

        if edges is None:
            edges = {}
        self.edges = edges

        self.attr = attr

    def add_vertex(self, vertex):
        """ add_vertex add vertex to graph's vertices
            if there is not other vertex with same id
            param vertex: vertex to add in graph
        """
        if vertex.id not in self.vertices.keys():
            self.vertices[vertex.id] = vertex

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, id):
        if id in self.vertices.keys():
            return self.vertices[id]
        else:
            return None

    def add_edge(self, edge, directed=False, auto=False):
        """ Add edge to source edges
            if there is no other edge with same source and target
            :param edge: edge to insert
            :param directed: enable graph directed
            :param auto: allow auto-cycle (loops)
        """
        (v1, v2) = edge.get_id()
        if v1 in self.vertices.keys() and v2 in self.vertices.keys():
            if directed:
                if auto:
                    self.edges[edge.get_id()] = edge
                else:
                    if v1 != v2:
                        self.edges[edge.get_id()] = edge
            else:
                if self.edges.get((v2, v1)) is None:
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
            edges.append((key, target))
        return edges

    def get_adjacent_vertices_by_vertex(self, id, type=None):
        """
        Get adjacent vertex of specific vertex
        param id: Vertex identifier in the graph
        param type: Filter
            None - All adjacent vertices
            +    - Output adjacent vertices
            -    - Input adjacent vertices
        """
        vertex = []
        for (source, target) in self.edges.keys():
            if type is None:
                if source == id:
                    vertex.append(target)
                elif target == id:
                    vertex.append(source)
            elif type == '+':
                if source == id:
                    vertex.append(target)
            elif type == '-':
                if target == id:
                    vertex.append(source)

        return vertex

    def get_edges_by_vertex(self, id, type=0):
        """
        Find the edges that are incident in vertex with id paramater
        param id: Vertex identifier in the graph
        param type: Filter output edges
            1 - Output edges
            2 - Input edges
            other - All edges
        return: list of edges
        """
        edges = []
        for (source, target) in self.edges.keys():
            if type == 1:
                if source == id:
                    edges.append((source, target))
            elif type == 2:
                if target == id:
                    edges.append((source, target))
            else:
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
            dot.node(str(n), str(n))
        for e in self.get_edges():
            (s, t) = e
            dot.edge(str(s), str(t))
        file = open("./images/gv/" + file_name + ".gv", "w")
        file.write(dot.source)
        file.close()
        return dot

    def bfs(self, s):
        """
        bfs Breadth-first search (BFS) is an algorithm
        for traversing or searching graph data structures.
        It starts at the s node
        and explores all of the neighbor nodes at the present
        depth prior to moving on to the nodes at the next depth level.
        :param s: root node for traversing
        :return g graph generated according BFS
        """
        g = Graph(attr={DIRECTED: True})
        root = self.get_vertex(s)
        root.attributes[DISCOVERED] = True
        q = collections.deque()
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[DIRECTED] else None
        # Insert root node in graph and queue
        g.add_vertex(root)
        q.append(s)

        while(len(q) > 0):
            v = q.popleft()
            for e in self.get_adjacent_vertices_by_vertex(v, adjacent_type):
                w = self.get_vertex(e)
                if DISCOVERED not in w.attributes or w.attributes[DISCOVERED] is False:
                    w.attributes[DISCOVERED] = True
                    q.append(w.id) 
                    g.add_vertex(w)
                    g.add_edge(edge.Edge(v,e), True)
        return g 

    def dfs(self,s):
        """
        dfs Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
        The algorithm starts at the root node and explores as far as possible along each branch before backtracking.
        :param s: root node for traversing
        :return g graph generated according DFS 
        """
        g = Graph(attr={DIRECTED:True})
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[DIRECTED] else None
        # Insert s root node in stack 
        stack = collections.deque()
        # Initial node does not have origin, it is represented by # 
        stack.append(('#',s))

        while(len(stack) > 0):
            (source, target) = stack.pop()
            w = self.get_vertex(target)
            if DISCOVERED not in w.attributes or w.attributes[DISCOVERED] is False:
                w.attributes[DISCOVERED] = True
                g.add_vertex(w)
                if(source != '#'):
                    g.add_edge(edge.Edge(source,w.id), True)
                for e in self.get_adjacent_vertices_by_vertex(w.id, adjacent_type):
                    stack.append((w.id, e)) 
        return g 


    def dfs_r(self,s):
        """
        dfs Depth-first search (DFS) recursive is an algorithm for traversing or searching tree
        or graph data structures. 
        The algorithm starts at the root node and explores as far as possible along each branch
        before backtracking.
        :param s: root node for traversing
        :return g graph generated according DFS 
        """
        g = Graph(attr={DIRECTED:True})
        return self.dfs_rec(g, ('#',s))
        
    def dfs_rec(self, g, s):
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[DIRECTED] else None
        (source, target) = s
        w = self.get_vertex(target)
        if DISCOVERED not in w.attributes or w.attributes[DISCOVERED] is False:
            w.attributes[DISCOVERED] = True
            g.add_vertex(w)
            if(source != '#'):
                g.add_edge(edge.Edge(source,w.id), True)
            for e in self.get_adjacent_vertices_by_vertex(w.id, adjacent_type):
                self.dfs_rec(g,(w.id,e))
        return g 
