import unittest
from random import randint

from pygraph import edge
from pygraph import graph
from pygraph import models
from pygraph import vertex


class TestDijkstra(unittest.TestCase):

    @unittest.skip
    def test_dijkstra_simple_3(self):
        g = graph.Graph()
        for i in range(1, 6):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e = edge.Edge(1, 2, {"WEIGHT": 1})
        g.add_edge(e)
        e = edge.Edge(2, 4, {"WEIGHT": 1})
        g.add_edge(e)
        e = edge.Edge(4, 5, {"WEIGHT": 1})
        g.add_edge(e)
        e = edge.Edge(1, 3, {"WEIGHT": 5})
        g.add_edge(e)
        e = edge.Edge(3, 4, {"WEIGHT": 3})
        g.add_edge(e)
        dot = g.create_graphviz('dijkstra_original_3',
                                attr_label_edge="WEIGHT")
        dot.render('dijkstra_3_original', view=True)
        result = g.dijkstra(1, 5)
        print(result)
        dot = result.create_graphviz('dijkstra_calculado_3', "WEIGHT", 1)
        # dot.render('dijkstra_3_calculado',view=True)

    @unittest.skip
    def test_dijkstra_simple_50(self):
        g = models.erdos_rengy(50, 50)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('dijkstra_50_original',
                                attr_label_edge="WEIGHT")
        dot.render('dijkstra_50', view=True)
        result = g.dijkstra(0, 38)
        dot = result.create_graphviz('dijkstra_50_calculado', "WEIGHT", 0)
        dot.render('dijkstra_50_calculado', view=True)

    @unittest.skip
    def test_dijkstra_simple_500(self):
        g = models.erdos_rengy(500, 500)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('dijkstra_500_original',
                                attr_label_edge="WEIGHT")
        dot.render('dijkstra_500', view=True)
        result = g.dijkstra(0, 440)
        dot = result.create_graphviz('dijkstra_500_calculado', "WEIGHT", 0)
        dot.render('dijkstra_500_calculado', view=True)
