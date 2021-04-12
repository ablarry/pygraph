![workflow](https://github.com/ablarry/pygraph.git/actions/workflows/python-publish/badge.svg
)

# pygraph
pygraph is a library to work with graphs and render with [graphviz](https://graphviz.org/) 

### Random Graphs Models
Creation of random graphs with models:

- **Mesh model**

  Graph of m*n nodes representing a meshing model.


  ![Mesh 10*10 nodes](images/png/Mesh_10x10_directed.png)


- **Erdős–Rényi model** 
  
  In the G(n,p) model, a graph is constructed by connecting labeled nodes randomly. Each edge is included in the graph with probability p, independently from every other edge.
  

  ![Erdős–Rényi 30 nodes](images/png/Erdos_directed_100_Black.png) 

- **Gilbert model**
  
  A random graph obtained by starting with a set of n isolated vertices and adding successive edges between them at random.


  ![Gilbert 30 nodes](images/png/Gilbert_30.png)

- **Geographic model**

  Create a random graph with simple method geographic.


  ![Geographic 30 nodes](images/png/GeoSimple_30_Black.png)


- **Barabási-Albert**
  
  The graph begins with an initial connected network of m0 nodes.
  New nodes are added to the network one at a time. Each new node is connected to m < m0 existing nodes with a probability that is proportional to the number of links that the existing nodes already have.


  ![Barabási-Albert 30 nodes](images/png/Barabasi_directed_30.png)

- **Dorogovtsev-Mendes**

  A graph with edge set E, and denote the degree of a vertex v (that is, the number of edges incident to v) by deg(v).
  

  ![Dorogovtsev Mendes 100 nodes](images/png/Dorogovtsev_directed_100_Black.png)

  [View all images model](images/png)
### Installation 

```
git clone https://github.com/ablarry/pygraph.git
```
### Quickstart
```
Available commands:
	make install			 Install dependencies.
	make test			     Run tests.	
```

### References:
- [Mesh model](https://en.wikipedia.org/wiki/Mesh_generation)
- [Erdős–Rényi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)
- [Gilbert model](https://en.wikipedia.org/wiki/Random_graph)
- [Barabási-Albert](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model#Algorithm)
- [Dorogovtsev-Mendes](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model#Algorithm)
