import numpy as np

class PheromoneSystem:
    def __init__(self, n_villes):
        self.pheromones = np.ones((n_villes, n_villes))
        self.evaporation_rate = 0.1
        
    def update(self, paths, distances):
        # Évaporation des phéromones existantes
        self.pheromones *= (1 - self.evaporation_rate)
        
        # Dépôt de nouvelles phéromones
        for path, distance in zip(paths, distances):
            for i in range(len(path)-1):
                city_i = path[i]
                city_j = path[i+1]
                self.pheromones[city_i][city_j] += 1/distance
                self.pheromones[city_j][city_i] += 1/distance