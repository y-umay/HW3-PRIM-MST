import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        num_vertices = len(self.adj_mat)
        self.mst = np.zeros((num_vertices, num_vertices))

        visited = [False] * num_vertices
        neighbors = []
        
        heapq.heappush(neighbors, (0, 0, 0))
        # note this assumes graph is fully connected
        # won't work if graph is not fully connected
        while len(neighbors) > 0:
            edge_weight, parent, unvisited = heapq.heappop(neighbors)
            
            if visited[unvisited]:
                continue
            
            visited[unvisited] = True
            self.mst[unvisited, parent] = edge_weight
            self.mst[parent, unvisited] = edge_weight
            
            for vertex in range(num_vertices):
                if self.adj_mat[unvisited, vertex] > 0 and not visited[vertex]:
                    edge_weight = self.adj_mat[unvisited, vertex]
                    heapq.heappush(neighbors,
                                   (edge_weight, unvisited, vertex))

    # self.mst = None
