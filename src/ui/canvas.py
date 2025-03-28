import tkinter as tk
import random
from ..core.colonie_fourmis import ColonieFourmis
from ..core.villes import Villes
from ..core.pheromones import PheromoneSystem

class TSPCanvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=800, height=550)
        self.bind('<Button-1>', self.ajout_ville)
        
        # Initialisation des composants de l'algorithme
        self.villes = Villes()
        self.pheromones = PheromoneSystem(0)
        self.colonie_fourmis = None
        self.distances = None  # Ajout de l'initialisation de distances

        
        # Création du frame pour les contrôles
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(fill=tk.X)
        
        # Création du bouton de démarrage
        self.start_button = tk.Button(self.controls_frame, text="Démarrer", command=self.start_algorithm)
        self.start_button.pack(side=tk.LEFT)
    
    def calculate_path_length(self, path):
        """Calcule la longueur totale d'un chemin"""
        if self.distances is None:
            return float('inf')  # Retourne l'infini si pas de distances
            
        total_distance = 0
        for i in range(len(path)-1):
            total_distance += self.distances[path[i]][path[i+1]]
        return total_distance
    
    def ajout_ville(self, event):
        x = event.x
        y = event.y
        self.create_oval(x-3, y-3, x+3, y+3, fill='blue')
        self.villes.add_city(x, y)
        self.pheromones = PheromoneSystem(len(self.villes.positions))
        if len(self.villes.positions) > 0:
            self.colonie_fourmis = ColonieFourmis(self.villes, self.pheromones)
            self.distances = self.villes.get_distance_matrix()  # Mise à jour des distances


    def start_algorithm(self):
        if self.colonie_fourmis:
            # Vérification si l'algorithme est déjà en cours
            if hasattr(self, 'running') and self.running:
                return  # Ne pas démarrer si déjà en cours
                
            self.running = True
            self.iterations = 0
            self.max_iterations = 100
            self.update_interval = 100
            self.update_algorithm()
            
    def stop_algorithm(self):
        self.running = False
        self.delete("path")
        self.delete("fourmi")
        self.iterations = 0
        self.colonie_fourmis = None
        self.villes = Villes()
        self.pheromones = PheromoneSystem(0)
        self.start_button.config(text="Démarrer")
        
    def update_algorithm(self):
        if self.running and self.iterations < self.max_iterations:
            paths = []
            path_lengths = []
            
            for _ in range(len(self.villes.positions)):
                path = []
                visited = set()
                ville_courante = random.randint(0, len(self.villes.positions) - 1)
                visited.add(ville_courante)
                path.append(ville_courante)
                
                while len(visited) < len(self.villes.positions):
                    ville_suivante = self.colonie_fourmis.select_ville_suivante(ville_courante, visited)
                    path.append(ville_suivante)
                    visited.add(ville_suivante)
                    ville_courante = ville_suivante
                
                paths.append(path)
                path_lengths.append(self.calculate_path_length(path))
            
            self.pheromones.update(paths, path_lengths)
            self.draw_best_path(paths, path_lengths)
            self.iterations += 1
            if self.running:
                self.after(self.update_interval, self.update_algorithm)