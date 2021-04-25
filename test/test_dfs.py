import unittest
from graphviz import Graph

import pygraph
from pygraph import edge
from pygraph import graph
from pygraph import models
from pygraph import vertex

class TestDFS(unittest.TestCase):

    def test_dfs_simple_10(self):
        g = graph.Graph(attr={graph.DIRECTED:True})
        for i in range(1, 11):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e = edge.Edge(1, 2)
        g.add_edge(e)
        e = edge.Edge(1, 3)
        g.add_edge(e)
        e = edge.Edge(1, 4)
        g.add_edge(e)
        e = edge.Edge(1, 5)
        g.add_edge(e)
        e = edge.Edge(2, 6)
        g.add_edge(e)
        e = edge.Edge(2, 7)
        g.add_edge(e)
        e = edge.Edge(6, 9)
        g.add_edge(e)
        e = edge.Edge(9, 10)
        g.add_edge(e)
        e = edge.Edge(3, 7)
        g.add_edge(e)
        e = edge.Edge(3, 8)
        g.add_edge(e)
        e = edge.Edge(4, 8)
        g.add_edge(e)
        e = edge.Edge(5, 10)
        g.add_edge(e)
        g2 = g.dfs(1)
        dot = g2.create_graphviz('dfs')
        gbase = '''digraph {
	1 [label=1]
	5 [label=5]
	10 [label=10]
	4 [label=4]
	8 [label=8]
	3 [label=3]
	7 [label=7]
	2 [label=2]
	6 [label=6]
	9 [label=9]
	1 -> 5
	5 -> 10
	1 -> 4
	4 -> 8
	1 -> 3
	3 -> 7
	1 -> 2
	2 -> 6
	6 -> 9
}'''
        #dot.render('dfs',view=True)
        self.assertEqual(gbase, str(dot))

    def test_dfs_simple_8(self):
        g = graph.Graph(attr={graph.DIRECTED:True})
        for i in range(1, 9):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e = edge.Edge(1, 2)
        g.add_edge(e)
        e = edge.Edge(1, 3)
        g.add_edge(e)
        e = edge.Edge(1, 4)
        g.add_edge(e)
        e = edge.Edge(2, 5)
        g.add_edge(e)
        e = edge.Edge(5, 7)
        g.add_edge(e)
        e = edge.Edge(7, 8)
        g.add_edge(e)
        e = edge.Edge(3, 6)
        g.add_edge(e)
        e = edge.Edge(6, 8)
        g.add_edge(e)
        e = edge.Edge(6, 7)
        g.add_edge(e)
        g2 = g.dfs(1)
        dot = g2.create_graphviz('dfs')
        gbase = '''digraph {
	1 [label=1]
	4 [label=4]
	3 [label=3]
	6 [label=6]
	7 [label=7]
	8 [label=8]
	2 [label=2]
	5 [label=5]
	1 -> 4
	1 -> 3
	3 -> 6
	6 -> 7
	7 -> 8
	1 -> 2
	2 -> 5
}'''
       # dot.render('dfs',view=True)
        self.assertEqual(gbase, str(dot))


    def test_dfs_r_simple_8(self):
        g = graph.Graph(attr={graph.DIRECTED:True})
        for i in range(1, 9):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e = edge.Edge(1, 2)
        g.add_edge(e)
        e = edge.Edge(1, 3)
        g.add_edge(e)
        e = edge.Edge(1, 4)
        g.add_edge(e)
        e = edge.Edge(2, 5)
        g.add_edge(e)
        e = edge.Edge(5, 7)
        g.add_edge(e)
        e = edge.Edge(7, 8)
        g.add_edge(e)
        e = edge.Edge(3, 6)
        g.add_edge(e)
        e = edge.Edge(6, 8)
        g.add_edge(e)
        e = edge.Edge(6, 7)
        g.add_edge(e)
        g2 = g.dfs_r(1)
        dot = g2.create_graphviz('dfs')
        print(dot)
        gbase = '''digraph {
	1 [label=1]
	2 [label=2]
	5 [label=5]
	7 [label=7]
	8 [label=8]
	3 [label=3]
	6 [label=6]
	4 [label=4]
	1 -> 2
	2 -> 5
	5 -> 7
	7 -> 8
	1 -> 3
	3 -> 6
	1 -> 4
}'''
    
        #dot.render('dfs_r',view=True)
        self.assertEqual(gbase, str(dot))

