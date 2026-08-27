# KNE_U1P1---GUI-Git
Análisis de Algoritmos
import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Karol Nungaray"
    lbl.config(text=f"Hola Compa, {nombre} ")

root = tk.Tk()
root.title("Saludador de Compas")
root.geometry("360x220")

lbl = tk.Label(root, text="Eh compa, Escribe tu nombre y presiona el botón")
lbl.pack(pady=10)

entrada = tk.Entry(root)
entrada.pack(pady=5)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

root.mainloop()
