import tkinter as tk
from tkinter import messagebox

# ======================= MODELO =======================
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True


# ======================= SERVICIO =======================
class TareaServicio:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        if descripcion.strip():
            self.tareas.append(Tarea(descripcion))

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].marcar_completada()

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas.pop(index)


# ======================= UI =======================
class App:
    def __init__(self):
        self.servicio = TareaServicio()

        self.root = tk.Tk()
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        self.entrada = tk.Entry(self.root, width=30)
        self.entrada.pack(pady=10)

        self.btn_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_tarea)
        self.btn_agregar.pack()

        self.lista = tk.Listbox(self.root, width=40)
        self.lista.pack(pady=10)

        self.btn_completar = tk.Button(self.root, text="Completar", command=self.completar_tarea)
        self.btn_completar.pack()

        self.btn_eliminar = tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # ================= ATALLOS =================
        self.root.bind("<Return>", lambda e: self.agregar_tarea())
        self.root.bind("c", lambda e: self.completar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def agregar_tarea(self):
        texto = self.entrada.get()
        self.servicio.agregar_tarea(texto)
        self.entrada.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.completar_tarea(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            estado = "✔" if tarea.completada else "✗"
            self.lista.insert(tk.END, f"[{estado}] {tarea.descripcion}")

    def run(self):
        self.root.mainloop()


# ======================= MAIN =======================
if __name__ == "__main__":
    app = App()
    app.run()
