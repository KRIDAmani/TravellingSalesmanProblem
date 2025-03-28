import numpy as np

class Villes:
    def __init__(self):
        self.positions = []
        
    def add_city(self, x, y):
        self.positions.append((x, y))
        
    def get_distance_matrix(self):
        n = len(self.positions)
        distances = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                pos_i = np.array(self.positions[i])
                pos_j = np.array(self.positions[j])
                distances[i][j] = np.linalg.norm(pos_i - pos_j)
        return distances
