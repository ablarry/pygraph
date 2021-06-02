import unittest

from random import randint
from pygraph import edge
from pygraph import graph
from pygraph import models
from pygraph import vertex


class TestKruskal(unittest.TestCase):

    def test_kruskalD(self):
        g = graph.Graph()
        for i in range(0, 6):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e1 = edge.Edge(0, 1, {"WEIGHT": 4})
        g.add_edge(e1)
        e2 = edge.Edge(0, 2, {"WEIGHT": 1})
        g.add_edge(e2)
        e3 = edge.Edge(0, 3, {"WEIGHT": 5})
        g.add_edge(e3)
        e4 = edge.Edge(1, 3, {"WEIGHT": 2})
        g.add_edge(e4)
        e5 = edge.Edge(1, 4, {"WEIGHT": 3})
        g.add_edge(e5)
        e6 = edge.Edge(1, 5, {"WEIGHT": 3})
        g.add_edge(e6)
        e7 = edge.Edge(2, 3, {"WEIGHT": 2})
        g.add_edge(e7)
        e8 = edge.Edge(2, 4, {"WEIGHT": 8})
        g.add_edge(e8)
        e9 = edge.Edge(3, 4, {"WEIGHT": 1})
        g.add_edge(e9)
        e10 = edge.Edge(4, 5, {"WEIGHT": 3})
        g.add_edge(e10)
        kg = g.KruskalD()
        amount = 0
        for k in kg.edges:
            amount = amount + kg.edges[k].attr["WEIGHT"]
        self.assertEqual(amount, 9)

    def test_kruskal(self):
        g = graph.Graph()
        for i in range(0, 6):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e1 = edge.Edge(0, 1, {"WEIGHT": 4})
        g.add_edge(e1)
        e2 = edge.Edge(0, 2, {"WEIGHT": 1})
        g.add_edge(e2)
        e3 = edge.Edge(0, 3, {"WEIGHT": 5})
        g.add_edge(e3)
        e4 = edge.Edge(1, 3, {"WEIGHT": 2})
        g.add_edge(e4)
        e5 = edge.Edge(1, 4, {"WEIGHT": 3})
        g.add_edge(e5)
        e6 = edge.Edge(1, 5, {"WEIGHT": 3})
        g.add_edge(e6)
        e7 = edge.Edge(2, 3, {"WEIGHT": 2})
        g.add_edge(e7)
        e8 = edge.Edge(2, 4, {"WEIGHT": 8})
        g.add_edge(e8)
        e9 = edge.Edge(3, 4, {"WEIGHT": 1})
        g.add_edge(e9)
        e10 = edge.Edge(4, 5, {"WEIGHT": 3})
        g.add_edge(e10)
        kg = g.Kruskal()
        amount = 0
        for k in kg.edges:
            amount = amount + kg.edges[k].attr["WEIGHT"]
        self.assertEqual(amount, 9)

    def test_prim(self):
        g = graph.Graph()
        for i in range(0, 6):
            v = vertex.Vertex(i)
            g.add_vertex(v)
        e1 = edge.Edge(0, 1, {"WEIGHT": 4})
        g.add_edge(e1)
        e2 = edge.Edge(0, 2, {"WEIGHT": 1})
        g.add_edge(e2)
        e3 = edge.Edge(0, 3, {"WEIGHT": 5})
        g.add_edge(e3)
        e4 = edge.Edge(1, 3, {"WEIGHT": 2})
        g.add_edge(e4)
        e5 = edge.Edge(1, 4, {"WEIGHT": 3})
        g.add_edge(e5)
        e6 = edge.Edge(1, 5, {"WEIGHT": 3})
        g.add_edge(e6)
        e7 = edge.Edge(2, 3, {"WEIGHT": 2})
        g.add_edge(e7)
        e8 = edge.Edge(2, 4, {"WEIGHT": 8})
        g.add_edge(e8)
        e9 = edge.Edge(3, 4, {"WEIGHT": 1})
        g.add_edge(e9)
        e10 = edge.Edge(4, 5, {"WEIGHT": 3})
        g.add_edge(e10)
        primg = g.Prim()
        amount = 0
        for k in primg.edges:
            amount = amount + primg.edges[k].attr["WEIGHT"]

        self.assertEqual(amount, 9)

    @unittest.skip
    def test_KruskalD_simple_50(self):
        g = models.erdos_rengy(50, 100)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('KruskalD_50_original',
                                attr_label_edge="WEIGHT")
        dot.render('KruskalD_50', view=True)
        result = g.KruskalD()
        dot = result.create_graphviz('KruskalD_50_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('KruskalD_50_calculado', view=True)

    @unittest.skip
    def test_KruskalD_simple_200(self):
        g = models.erdos_rengy(200, 400)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('KruskalD_200_original',
                                attr_label_edge="WEIGHT")
        dot.render('KruskalD_200', view=True)
        result = g.KruskalD()
        dot = result.create_graphviz('KruskalD_200_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('KruskalD_200_calculado', view=True)

    @unittest.skip
    def test_Kruskal_simple_50(self):
        g = models.erdos_rengy(50, 100)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('Kruskal_50_original',
                                attr_label_edge="WEIGHT")
        dot.render('Kruskal_50', view=True)
        result = g.Kruskal()
        dot = result.create_graphviz('Kruskal_50_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('Kruskal_50_calculado', view=True)

    @unittest.skip
    def test_Kruskal_simple_200(self):
        g = models.erdos_rengy(200, 400)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('Kruskal_200_original',
                                attr_label_edge="WEIGHT")
        dot.render('Kruskal_200', view=True)
        result = g.Kruskal()
        dot = result.create_graphviz('Kruskal_200_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('Kruskal_200_calculado', view=True)

    @unittest.skip
    def test_Prim_simple_50(self):
        g = models.erdos_rengy(50, 100)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('Prim_50_original',
                                attr_label_edge="WEIGHT")
        dot.render('Prim_50', view=True)
        result = g.Prim()
        dot = result.create_graphviz('Prim_50_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('Prim_50_calculado', view=True)

    @unittest.skip
    def test_Prim_simple_200(self):
        g = models.erdos_rengy(200, 400)
        for e in g.edges.values():
            e.attr["WEIGHT"] = randint(1, 10)
        dot = g.create_graphviz('Prim_200_original',
                                attr_label_edge="WEIGHT")
        dot.render('Prim_200', view=True)
        result = g.Prim()
        dot = result.create_graphviz('Prim_200_calculado', attr_label_edge="WEIGHT", source=0)
        dot.render('Prim_200_calculado', view=True)
