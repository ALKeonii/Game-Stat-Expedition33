import tkinter as tk

# Data for Dashboard
game_data = {
    "Favorite Characters" : "Gustav" + " & Monoco",
    "Favorite Chapter" : "Act 2",
    "Favorite Boss" : "Simon"
}

# Crea la ventana Principal
ventana = tk.Tk()
ventana.title("Game Stat")
ventana.geometry("780x360")
ventana.resizable(False, False)

# Background color:
ventana.configure(bg="#2b2b2b")

# Titulo del Label
title_label = tk.Label(ventana, text="Game Dashboard", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#2b2b2b")
title_label.pack(pady=10)

# Funcion para crear filas etiquetada
def create_info_row(parent, label_text, value_text):
    frame = tk.Frame(parent, bg ="#2b2b2b")
    frame.pack(pady=5, fill="x", padx=20)

    label = tk.Label(frame, text =label_text + ":", font=("Helvetica", 18, "bold" ), fg = "#ffffff", bg = "#2b2b2b", anchor= "w")
    label.pack(side="left")

    value = tk.Label(frame, text=value_text, font=("Helvetica", 12), fg="#ffffff", bg="#2b2b2b", anchor="w")
    value.pack(side="left" , padx=10)

# Agrega filas para cada pieza de datos
for key, value in game_data.items():
    create_info_row(ventana, key, str(value))

# Mantiene la pantall corriendo
ventana.mainloop()