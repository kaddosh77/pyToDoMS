import tkinter as tk
from tkinter.ttk import *
import Interfaces.ModuleInterfaceTk as mi

## Ventana Principal
mainWin = tk.Tk()
mainWin.title("Gestion de Tareas")
w, h = 1200, 600
mainWin.geometry(f"{w}x{h}")
mainWin.wm_minsize(1200, 600)
mainWin.wm_maxsize(1200, 600)
mainWin.config(bg="#f0f0f0")

# Titulo
mainTitle = tk.Label(mainWin, text="Menú de Tareas", font=("Arial", 16), bg="#000974", fg="#ffffff", width=99, pady=14, padx=0)
mainTitle.pack(pady=2, side=tk.TOP)

topPanel = tk.PanedWindow(bg="#497d99")
topPanel.pack(side=tk.TOP, pady=0, padx=0)

leftPanel = tk.PanedWindow(topPanel, width=1000, height=500, bg="#497d99")
leftPanel.pack(side=tk.RIGHT, pady=10, padx=10)

btnStyle = {"width": 18, "height": 2, "bg": "#04177a", "fg": "#ffffff", "font": ("Arial", 12)}
tk.Button(topPanel, text="Ver Tareas", command=mi.showHomeworks, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Agregar Tarea", command=mi.addHomework, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Anular Tarea", command=mi.delHomework, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Actualizar Tarea", command=mi.pushHomework, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Importar Tareas", command=mi.importHomeworks, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Exportar Tareas 'CSV'", command=mi.exportHomeworks, **btnStyle).pack(pady=0)
tk.Button(topPanel, text="Salir", command=mainWin.quit, **btnStyle).pack(pady=0)

# Inicia la interfaz grafica
mainWin.mainloop()
