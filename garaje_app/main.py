import tkinter as tk
import sys
import os

# Permite importar módulos del proyecto sin importar desde dónde se ejecute
sys.path.insert(0, os.path.dirname(__file__))

from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter


def main():
    """Punto de entrada de la aplicación de gestión de garaje."""
    servicio = GarajeServicio()
    root = tk.Tk()
    AppTkinter(root, servicio)
    root.mainloop()


if __name__ == "__main__":
    main()