import tkinter as tk
from tkinter import ttk, messagebox
from models import GameStat
import database

# --- Functions (CRUD operations) ---

# Refreshes the table
def refresh_table():
    for i in tree.get_children():
        tree.delete(i)
    stats = database.read_all_game_stats()
    for stat in stats:
        tree.insert("", "end", values=(stat.id, stat.party_name, stat.favorite_character, stat.achievements, stat.time_played, stat.levels_reached))

# Adds to the table
def add_record():
    stat = GameStat(
        party_name=party_name_var.get(),
        favorite_character=fav_char_var.get(),
        achievements=int(achievements_var.get() or 0),
        time_played=time_played_var.get(),
        levels_reached=int(levels_var.get() or 0)
    )
    database.create_game_stat(stat)
    refresh_table()
    messagebox.showinfo("Success", "Record added successfully!")

# Deletes the selected record from the database
def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    stat_id = tree.item(selected[0])['values'][0]
    database.delete_game_stat(stat_id)
    refresh_table()
    messagebox.showinfo("Deleted", "Record deleted.")

# Updates the selected record
def update_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to update")
        return
    stat_id = tree.item(selected[0])['values'][0]
    stat = GameStat(
        id=stat_id,
        party_name=party_name_var.get(),
        favorite_character=fav_char_var.get(),
        achievements=int(achievements_var.get() or 0),
        time_played=time_played_var.get(),
        levels_reached=int(levels_var.get() or 0)
    )
    database.update_game_stat(stat)
    refresh_table()
    messagebox.showinfo("Updated", "Record updated successfully!")

# --- Setup Database ---
database.create_table()

# --- Setup Tkinter Window ---
root = tk.Tk()
root.title("Expedition 33 - Game Stats Dashboard")
root.geometry("900x500")
root.configure(bg="#121212")

# --- Style Configuration ---
style = ttk.Style(root)
style.theme_use("clam")

# Customize widget appearance
style.configure("TLabel", background="#121212", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#1E1E1E", foreground="white", font=("Segoe UI", 10), padding=5)
style.map("TButton", background=[("active", "#333333")])
style.configure("Treeview", background="#1E1E1E", foreground="white", fieldbackground="#1E1E1E", rowheight=25)
style.map("Treeview", background=[("selected", "#333333")])
style.configure("Treeview.Heading", background="#333333", foreground="white", font=("Segoe UI", 10, "bold"))

# --- Input Fields ---
# Variation to store user input
party_name_var = tk.StringVar()
fav_char_var = tk.StringVar()
achievements_var = tk.StringVar()
time_played_var = tk.StringVar()
levels_var = tk.StringVar()

# Create form frame
frame_form = tk.Frame(root, bg="#121212")
frame_form.pack(pady=10)

# Cenerates form lables and entries
labels = ["Party Name", "Favorite Character", "Achievements", "Time Played", "Levels Reached"]
vars = [party_name_var, fav_char_var, achievements_var, time_played_var, levels_var]

for i, (label, var) in enumerate(zip(labels, vars)):
    ttk.Label(frame_form, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame_form, textvariable=var, width=30).grid(row=i, column=1, padx=10, pady=5)

# --- Buttons (Create, Update, Delete) ---
frame_buttons = tk.Frame(root, bg="#121212")
frame_buttons.pack(pady=10)

ttk.Button(frame_buttons, text="Create", command=add_record).grid(row=0, column=0, padx=10)
ttk.Button(frame_buttons, text="Update", command=update_record).grid(row=0, column=1, padx=10)
ttk.Button(frame_buttons, text="Delete", command=delete_record).grid(row=0, column=2, padx=10)

# --- Table View ---
cols = ("ID", "Party Name", "Favorite Character", "Achievements", "Time Played", "Levels Reached")
tree = ttk.Treeview(root, columns=cols, show="headings", style="Treeview")

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=140, anchor="center")

tree.pack(fill="both", expand=True, padx=10, pady=10)

# --- Populate ---
refresh_table()

# --- Pre-filled example record ---
if not database.read_all_game_stats():
    example_stat = GameStat(
        party_name="Expedition 33",
        favorite_character="Verso",
        achievements=55,
        time_played="70+ hours",
        levels_reached=99
    )
    database.create_game_stat(example_stat)
    refresh_table()

# --- Runs the app ---
root.mainloop()

