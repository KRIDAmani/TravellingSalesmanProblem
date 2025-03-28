import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from src.ui.main_window import MainWindow

def main():
    root = MainWindow()
    root.mainloop()

if __name__ == "__main__":
    main()