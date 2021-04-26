import unittest
from graphviz import Graph

import pygraph
from pygraph import edge
from pygraph import graph
from pygraph import models
from pygraph import vertex

class TestBFS(unittest.TestCase):

    @unittest.skip
    def test_bfs_simple_10(self):
        g = graph.Graph()
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
        g2 = g.bfs(1)
        dot = g2.create_graphviz('bfs')
        gbase = '''digraph {
	1 [label=1]
	2 [label=2]
	3 [label=3]
	4 [label=4]
	5 [label=5]
	6 [label=6]
	7 [label=7]
	8 [label=8]
	10 [label=10]
	9 [label=9]
	1 -> 2
	1 -> 3
	1 -> 4
	1 -> 5
	2 -> 6
	2 -> 7
	3 -> 8
	5 -> 10
	6 -> 9
}'''
        #dot.render('bfs',view=True)
        self.assertEqual(gbase, str(dot)) 


    @unittest.skip
    def test_bfs_graphviz_10(self):
        g = models.erdos_rengy(10, 10)
        dot = g.create_graphviz('bfs_original_10')
        dot.render('bfs_original_10',view=True)
        g2 = g.bfs(0)
        dot = g2.create_graphviz('bfs_10')
        dot.render('bfs_10',view=True)

    @unittest.skip
    def test_bfs_graphviz_30(self):
        g = models.erdos_rengy(30, 50)
        dot = g.create_graphviz('bfs_original_30')
        dot.render('bfs_original_30',view=True)
        g2 = g.bfs(0)
        dot = g2.create_graphviz('bfs_30')
        dot.render('bfs_30',view=True)


    @unittest.skip
    def test_bfs_graphviz_100(self):
        g = models.erdos_rengy(100, 150)
        dot = g.create_graphviz('bfs_original_100')
        dot.render('bfs_original_100',view=True)
        g2 = g.bfs(0)
        dot = g2.create_graphviz('bfs_100')
        dot.render('bfs_100',view=True)

    @unittest.skip
    def test_bfs_graphviz_500(self):
        g = models.erdos_rengy(500, 950)
        dot = g.create_graphviz('bfs_original_500')
        dot.render('bfs_original_500',view=True)
        g2 = g.bfs(0)
        dot = g2.create_graphviz('bfs_500')
        dot.render('bfs_500',view=True)

