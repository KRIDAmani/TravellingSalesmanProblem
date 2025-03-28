import tkinter as tk
from .canvas import TSPCanvas

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Problème du Voyageur de Commerce")
        self.geometry("800x600")
        
        self.canvas = TSPCanvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(fill=tk.X)
        
        self.start_button = tk.Button(self.controls_frame, text="Démarrer", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT)
        
          # Définition de la méthode start_simulation
        self.running = False
        
    def start_simulation(self):
        if not self.running:
            self.running = True
            self.start_button.config(text="Arrêter")
            self.canvas.start_algorithm()
        else:
            self.running = False
            self.start_button.config(text="Démarrer")
            self.canvas.stop_algorithm()
