class Todo:
    def __init__(self):
        self.homeworks = {}

    def add_homework(self, titleHomework, initDate, finalDate, homeworkStatus, hwPriority):
        if self.validateHomework(titleHomework):
            return(f"La tarea {titleHomework} ya ha sido programada")
        else:
            self.homeworks[titleHomework] = {"Inicio": initDate, "Final": finalDate, "Estado": homeworkStatus, "Prioridad": hwPriority}
            return(f"La tarea: '{titleHomework}', ha sido agregada satisfactoriamente.")

    def validateHomework(self, titleHomework):
        if titleHomework in self.homeworks:
            return True
        return False

    def remove_homework(self, hwTitle):
        if self.validateHomework(hwTitle):
            del self.homeworks[hwTitle]
            return(f"La tarea {hwTitle} se ha eliminado.")
        else:
            return(f"No se encontro la tarea '{hwTitle}'")

    def push_homework(self, hwTitle, initDate, finalDate, homeworkStatus, hwPriority):
        if self.validateHomework(hwTitle):
            self.homeworks[hwTitle]['Inicio'] = initDate
            self.homeworks[hwTitle]['Final'] = finalDate
            self.homeworks[hwTitle]['Estado'] = homeworkStatus
            self.homeworks[hwTitle]['Prioridad'] = hwPriority
            return(f"La tarea: '{hwTitle}', se ha actualizado satisfactoriamente.")
        else:
            return(f"No se encontro la tarea '{hwTitle}'")


    def load_csv(self, filename='cargarTareas.csv'):
        import csv
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                readFile = csv.DictReader(file)
                for linea in readFile:
                    self.homeworks[linea['Tarea']] = {
                        "Inicio": str(linea["Inicio"]),
                        "Final": str(linea['Final']),
                        "Estado": str(linea['Estado']),
                        "Prioridad": str(linea['Prioridad'])
                    }
            return(f"Tareas cargadas desde el archivo '{filename}'.")
        except FileNotFoundError:
            return(f"El archivo {filename} no fue encontrado")
        except ValueError:
            return(f"Error en el formato del archivo {filename}")
        except KeyError:
            return(f"Error con la llave principal {KeyError}")

    def xport_csv(self, filename='exportartareas.csv'):
        import csv
        with open(filename, mode='w', encoding='utf-8') as file:
            writeFile = csv.writer(file)
            writeFile.writerow(['Tarea', 'Inicio', 'Final', 'Estado', 'Prioridad'])
            for tarea, datos in self.homeworks.items():
                writeFile.writerow([tarea, datos['Inicio'], datos['Final'], datos['Estado'], datos['Prioridad']])
        return(f"Listado de tareas exportado a '{filename}'")
