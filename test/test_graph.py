import unittest
import graphs
from graphs import graph
from graphs import vertex
from graphs import edge
from graphs import models
from graphviz import Graph

class TestGraph(unittest.TestCase):
    
    def test_initialize_graph(self):
        g = graph.Graph()
    
    def test_initialize_vertex(self):
        v = vertex.Vertex(1)
        self.assertEqual(1,v.id) 

    def test_initialize_edge(self):
        e = edge.Edge(1,2)
        self.assertEqual((1,2),e.get_id())

    def test_add_vertice(self):
        g = graph.Graph() 
        v = vertex.Vertex(1)
        g.add_vertex(v)
        self.assertEqual(1,len(g.vertices))

    def test_add_edge(self):
        g = graph.Graph() 
        v1 = vertex.Vertex(1)
        v2 = vertex.Vertex(2)
        g.add_vertex(v1)
        g.add_vertex(v2)
        e = edge.Edge(1,2)
        g.add_edge(e)
        self.assertEqual(1,len(g.get_edges()))
       

    def test_edges(self):
        g = graph.Graph() 
        v = vertex.Vertex(1)
        g.add_vertex(v)
        v = vertex.Vertex(2)
        g.add_vertex(v)
        e = edge.Edge(1,2)
        g.add_edge(e)
        self.assertEqual([(1,2)],g.get_edges())

    def test_get_by_vertex(self):
        g = graph.Graph() 
        v = vertex.Vertex(1)
        g.add_vertex(v)
        v = vertex.Vertex(2)
        g.add_vertex(v)
        v = vertex.Vertex(3)
        g.add_vertex(v)
        e = edge.Edge(1,2)
        g.add_edge(e)
        self.assertEqual([(1,2)],g.get_edges_by_vertex(1))
        e = edge.Edge(1,3)
        g.add_edge(e)
        self.assertEqual(2,len(g.get_edges_by_vertex(1)))

    # Tests Mesh graph
    def test_mesh(self):
        g = models.mesh(2,2,True)
        self.assertEqual(4,len(g.get_edges()))

    def test_mesh_validation(self):
        self.assertRaises(ValueError, models.mesh, 1, 1, True)

    def test_create_mesh_graphviz_30(self):
        g = models.mesh(10,3)
        dot = g.create_graphviz('Mesh_3x10')

    def test_create_mesh_directed_graphviz_30(self):
        g = models.mesh(10,3, True)
        dot = g.create_graphviz('Mesh_3x10_directed')

    def test_create_mesh_graphviz_100(self):
        g = models.mesh(10,10)
        dot = g.create_graphviz('Mesh_10x10')

    def test_create_mesh_directed_graphviz_100(self):
        g = models.mesh(10,10, True)
        dot = g.create_graphviz('Mesh_10x10_directed')

    def test_create_mesh_graphviz_500(self):
        g = models.mesh(100,5)
        dot = g.create_graphviz('Mesh_100x5')

    def test_create_mesh_directed_graphviz_500(self):
        g = models.mesh(100,5, True)
        dot = g.create_graphviz('Mesh_100x5_directed')


    # Tests Erdos-Rengy graph
    def test_erdos_rengy(self):
        g = models.erdos_rengy(2,2,True)

    def test_erdos_rengy_validation(self):
        self.assertRaises(ValueError, models.erdos_rengy, 0, 1, True)
        self.assertRaises(ValueError, models.erdos_rengy, 5, 3, True)

    def test_create_erdos_graphviz_30(self):
        g = models.erdos_rengy(30,30)
        self.assertEqual(30, len(g.edges))
        dot = g.create_graphviz('Erdos_30')

    def test_create_erdos_graphviz_directed_30(self):
        g = models.erdos_rengy(30,30, True)
        self.assertEqual(30, len(g.edges))
        dot = g.create_graphviz('Erdos_directed_30')

    def test_create_erdos_graphviz_100(self):
        g = models.erdos_rengy(100,100)
        self.assertEqual(100, len(g.edges))
        dot = g.create_graphviz('Erdos_100')

    def test_create_erdos_graphviz_directed_100(self):
        g = models.erdos_rengy(100,100, True)
        self.assertEqual(100, len(g.edges))
        dot = g.create_graphviz('Erdos_directed_100')

    def test_create_erdos_graphviz_500(self):
        g = models.erdos_rengy(500,500)
        self.assertEqual(500, len(g.edges))
        dot = g.create_graphviz('Erdos_500')

    def test_create_erdos_graphviz_directed_500(self):
        g = models.erdos_rengy(500,500, True)
        self.assertEqual(500, len(g.edges))
        dot = g.create_graphviz('Erdos_directed_500')


    # Tests Gilbert graph
    def test_gilbert(self):
        g = models.gilbert(5,0.5)

    def test_gilbert_validation(self):
        self.assertRaises(ValueError, models.gilbert, 0, 0.1)
        self.assertRaises(ValueError, models.gilbert, 5, 0)
        self.assertRaises(ValueError, models.gilbert, 5, 1)
   
    def test_create_gilbert_graphviz_30(self):
        g = models.gilbert(30,0.3)
        dot = g.create_graphviz('Gilbert_30')

    def test_create_gilbert_graphviz_100(self):
        g = models.gilbert(100,0.3)
        dot = g.create_graphviz('Gilbert_100')

    def test_create_gilbert_graphviz_500(self):
        g = models.gilbert(500,0.3)
        dot = g.create_graphviz('Gilbert_500')

   

    # Tests Geo-Simplr graph
    def test_calculate_distance(self):
        v1 = vertex.Vertex(1, {models.COORDINATE_X: 3, models.COORDINATE_Y : 2})
        v2 = vertex.Vertex(2, {models.COORDINATE_X: 9, models.COORDINATE_Y : 7})
        p1 = (v1.attributes[models.COORDINATE_X], v1.attributes[models.COORDINATE_Y])
        p2 = (v2.attributes[models.COORDINATE_X], v2.attributes[models.COORDINATE_Y])
        d = models.calculate_distance(p1, p2)

    def test_geo_simple_validation(self):
        self.assertRaises(ValueError, models.geo_simple, 0, 0.1)
        self.assertRaises(ValueError, models.geo_simple, 5, 1)

    def test_create_geo_simple_graphviz_30(self):
        g = models.geo_simple(30,0.9)
        dot = g.create_graphviz('GeoSimple_30')

    def test_create_geo_simple_graphviz_directed_30(self):
        g = models.geo_simple(30,0.9, True)
        dot = g.create_graphviz('GeoSimple_directed_30')

    def test_create_geo_simple_graphviz_100(self):
        g = models.geo_simple(100,0.9)
        dot = g.create_graphviz('GeoSimple_100')

    def test_create_geo_simple_graphviz_directed_100(self):
        g = models.geo_simple(100,0.9, True)
        dot = g.create_graphviz('GeoSimple_directed_100')


    # Tests Barabasi graph
    def test_create_barabasi_graphviz_30(self):
        g = models.barabasi(30,30)
        dot = g.create_graphviz('Barabasi_30')

    def test_create_barabasi_graphviz_directed_30(self):
        g = models.barabasi(30,30, True)
        dot = g.create_graphviz('Barabasi_directed_30')

    def test_create_barabasi_graphviz_100(self):
        g = models.barabasi(100,100)
        dot = g.create_graphviz('Barabasi_100')

    def test_create_barabasi_graphviz_directed_100(self):
        g = models.barabasi(100,100, True)
        dot = g.create_graphviz('Barabasi_directed_100')

   # def test_create_barabasi_graphviz_500(self):
   #     g = models.barabasi(500,500)
   #     dot = g.create_graphviz('Barabasi_500')

   # def test_create_barabasi_graphviz_directed_500(self):
   #     g = models.barabasi(500,500, True)
   #     dot = g.create_graphviz('Barabasi_directed_500')



    # Tests Dorogovtse Mendes graph
    def test_dorogovtsev_mendes_validation(self):
        self.assertRaises(ValueError, models.dorogovtsev_mendes, 2)

    def test_dorogovtsev_mendes_graphviz_30(self):
        g = models.dorogovtsev_mendes(30)
        dot = g.create_graphviz('Dorogovtsev_30')

    def test_dorogovtsev_mendes_graphviz_directed_30(self):
        g = models.dorogovtsev_mendes(30, True)
        dot = g.create_graphviz('Dorogovtsev_directed_30')

    def test_dorogovtsev_mendes_graphviz_100(self):
        g = models.dorogovtsev_mendes(100)
        dot = g.create_graphviz('Dorogovtsev_100')

    def test_dorogovtsev_mendes_graphviz_directed_100(self):
        g = models.dorogovtsev_mendes(100, True)
        dot = g.create_graphviz('Dorogovtsev_directed_100')

    def test_dorogovtsev_mendes_graphviz_500(self):
        g = models.dorogovtsev_mendes(500)
        dot = g.create_graphviz('Dorogovtsev_500')

    def test_dorogovtsev_mendes_graphviz_directed_500(self):
        g = models.dorogovtsev_mendes(500, True)
        dot = g.create_graphviz('Dorogovtsev_directed_500')




if __name__ == '__main__':
    unittest.main()
