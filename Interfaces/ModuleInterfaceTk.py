import tkinter as tk
from tkinter import messagebox, Toplevel, Scrollbar, ttk
import Classes.ClassTodo as ct

# Objeto de la Clase Todo
todo = ct.Todo()

def showHomeworks():
    # Ventana que muestra las tareas
    revealWindow = Toplevel()
    revealWindow.title("Listado de Tareas")

    # Mustra las tareas en una tabla
    newTree = ttk.Treeview(revealWindow, columns=("Tareas", "Fecha Asignacion", "Fecha Entrega", "Estado", "Prioridad"), show="headings")
    newTree.heading("Tareas", text="Tareas")
    newTree.heading("Fecha Asignacion", text="Fecha Asignación")
    newTree.heading("Fecha Entrega", text="Fecha Entrega")
    newTree.heading("Estado", text="Estado")
    newTree.heading("Prioridad", text="Prioridad")

    # Llenar el arbol con las tareas programadas
    for titleHw, newValues in todo.homeworks.items():
        newTree.insert("", "end", values=(titleHw, newValues["Inicio"], newValues["Final"], newValues["Estado"], newValues["Prioridad"]))

    # Agregar barra de desplazamiento
    scroll_y = Scrollbar(revealWindow, orient="vertical", command=newTree.yview)
    newTree.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")
    newTree.pack(padx=10, pady=10)


def addHomework():
    def addHomework():
        try:
            titleHw = title_entry.get()
            initDate = str(init_date.get())
            finalDate = str(final_date.get())
            homeworkStatus = str(hw_status.get())
            hwPriority = str(hw_priority.get())
            if titleHw != '' and initDate != '' and finalDate != '' and homeworkStatus != '' and hwPriority != '':
                addHwForm.destroy()
                messagebox.showinfo("Success", todo.add_homework(titleHw, initDate, finalDate, homeworkStatus, hwPriority))
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, una fecha valida.")
    
    # Formulario
    addHwForm = Toplevel()
    addHwForm.title("Agregar Nueva Tarea")
    addHwForm.config(padx=30, pady=30)
    addHwForm.geometry("470x260")
    addHwForm.minsize(470, 300)
    addHwForm.maxsize(500, 350)

    tk.Label(addHwForm, text="Nueva Tarea").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(addHwForm, text="Fecha Inicio").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(addHwForm, text="Fecha Entrega").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(addHwForm, text="Estado").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(addHwForm, text="Prioridad").grid(row=4, column=0, padx=10, pady=10)

    title_entry = tk.Entry(addHwForm)
    init_date = tk.Entry(addHwForm)
    final_date = tk.Entry(addHwForm)
    hw_status = tk.Entry(addHwForm)
    hw_priority = tk.Entry(addHwForm)

    title_entry.config(width=50)
    init_date.config(width=50)
    final_date.config(width=50)
    hw_status.config(width=50)
    hw_priority.config(width=50)

    title_entry.focus()

    title_entry.grid(row=0, column=1)
    init_date.grid(row=1, column=1)
    final_date.grid(row=2, column=1)
    hw_status.grid(row=3, column=1)
    hw_priority.grid(row=4, column=1)

    tk.Button(addHwForm, text="Agregar", command=addHomework, padx=17, pady=3, background="#005a6c", foreground="#ffffff", font=('Arial', 10)).grid(row=5, column=1, columnspan=3)
    tk.Button().pack(side='right')

def delHomework():
    def hwDelete():
        hwTitle = titleEntry.get()
        delForm.destroy()
        messagebox.showinfo("Info", todo.remove_homework(hwTitle))
    
    delForm = Toplevel()
    delForm.title("Eliminar Tarea")
    delForm.config(padx=30, pady=30)

    tk.Label(delForm, text="Titulo de la Tarea").grid(row=0, column=0, padx=10, pady=10)
    titleEntry = tk.Entry(delForm)
    titleEntry.grid(row=0, column=1)

    titleEntry.config(width=50)
    titleEntry.focus()

    tk.Button(delForm, text="Eliminar", command=hwDelete, padx=17, pady=3, background="#991616", foreground="#ffffff", font=('Arial', 10)).grid(row=4, column=1, columnspan=3)

def pushHomework():
    def hwUpdate():
        try:
            titleHw = title_entry.get()
            initDate = str(init_date.get())
            finalDate = str(final_date.get())
            homeworkStatus = str(hw_status.get())
            homeworkPriority = str(hw_priority.get())
            if titleHw != '' and initDate != '' and finalDate != '' and homeworkStatus != '' and homeworkPriority != '':
                pushHwForm.destroy()
                messagebox.showinfo("Success", todo.push_homework(titleHw, initDate, finalDate, homeworkStatus, homeworkPriority))
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, una fecha valida.")
    
    # Formulario
    pushHwForm = Toplevel()
    pushHwForm.title("Actualizar Tarea")
    pushHwForm.config(padx=30, pady=30)
    pushHwForm.geometry("470x260")
    pushHwForm.minsize(470, 300)
    pushHwForm.maxsize(500, 350)

    tk.Label(pushHwForm, text="Tarea").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(pushHwForm, text="Fecha Inicio").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(pushHwForm, text="Fecha Entrega").grid(row=2, column=0, padx=10, pady=10)
    tk.Label(pushHwForm, text="Estado").grid(row=3, column=0, padx=10, pady=10)
    tk.Label(pushHwForm, text="Prioridad").grid(row=4, column=0, padx=10, pady=10)

    title_entry = tk.Entry(pushHwForm)
    init_date = tk.Entry(pushHwForm)
    final_date = tk.Entry(pushHwForm)
    hw_status = tk.Entry(pushHwForm)
    hw_priority = tk.Entry(pushHwForm)

    title_entry.config(width=50)
    init_date.config(width=50)
    final_date.config(width=50)
    hw_status.config(width=50)
    hw_priority.config(width=50)

    title_entry.focus()

    title_entry.grid(row=0, column=1)
    init_date.grid(row=1, column=1)
    final_date.grid(row=2, column=1)
    hw_status.grid(row=3, column=1)
    hw_priority.grid(row=4, column=1)

    tk.Button(pushHwForm, text="Actualizar", command=hwUpdate, padx=17, pady=3, background="#007449", foreground="#ffffff", font=('Arial', 10)).grid(row=5, column=1, columnspan=3)

def importHomeworks():
    messagebox.showinfo("Cargar CSV", todo.load_csv())

def exportHomeworks():
    messagebox.showinfo("Exportar CSV", todo.xport_csv())
