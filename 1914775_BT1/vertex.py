class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
    
    def add_neighbor(self, neighbor, weight):
        # if isinstance(neighbor, Vertex):
        if neighbor.name not in self.neighbors:
            if neighbor.name != self.name:
                self.neighbors.append({neighbor.name:weight})
                # neighbor.neighbors.append({neighbor.name:weight})
            # self.neighbors = sorted(self.neighbors)
            # neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                print('may ngu')
                
        # else:
        #     return False
        
    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False
            
    def __repr__(self):
        return str(self.neighbors)
    
