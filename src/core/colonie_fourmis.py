import numpy as np
import random  # Ajout de l'import manquant

class ColonieFourmis:
    def __init__(self, villes, pheromone_system, alpha=1.0, beta=1.0):
        self.villes = villes
        self.pheromones = pheromone_system
        self.alpha = alpha
        self.beta = beta
        self.n_fourmis = len(villes.positions)
        self.distances = villes.get_distance_matrix()

    def select_ville_suivante(self, ville_courante, visited):
        probabilites = []
        total_prob = 0
        
        for ville_suivante in range(len(self.villes.positions)):
            if ville_suivante not in visited:
                # Ajout d'une petite valeur pour éviter la division par zéro
                dist = max(0.1, self.distances[ville_courante][ville_suivante])
                phero = self.pheromones.pheromones[ville_courante][ville_suivante]**self.alpha
                prob = phero * (1/dist)**self.beta
                probabilites.append(prob)
                total_prob += prob
                
        if total_prob == 0:
            return random.choice([v for v in range(len(self.villes.positions)) if v not in visited])   
        
        r = random.random() * total_prob
        sum_prob = 0
        
        for i, prob in enumerate(probabilites):
            sum_prob += prob
            if sum_prob >= r:
                return list(set(range(len(self.villes.positions))) - visited)[i]