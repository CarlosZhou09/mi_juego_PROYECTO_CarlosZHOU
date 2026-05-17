import tkinter as tk

def abrir(seleccion=None, ventana_anterior=None):
    if ventana_anterior:
        ventana_anterior.destroy()  # cierra la ventana principal

    root = tk.Tk()
    root.title("Juego")
    root.geometry("1500x700")
    root.mainloop()