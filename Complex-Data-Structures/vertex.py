# This class is responsible for storing information about individual vertices in our graph. 
# An instance of Vertex will store data and a Python dictionary which tracks other Vertex instances connected to self
class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())
