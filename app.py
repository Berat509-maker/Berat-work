import tkinter as tk
from tkinter import ttk, messagebox

# Functions for menu actions
def new_file():
    messagebox.showinfo("New", "Dosje e re krijuar!")

def save_file():
    # Accessing the data from the entry fields and text box
    pacient_id = pacient_id_var.get()
    emri = emri_var.get()
    data_lindjes = data_lindjes_var.get()
    grupi_gjakut = grupi_gjakut_var.get()
    numri_kontrolleve = numri_kontrolleve_var.get()
    data_vizites = data_vizites_var.get()
    diagnoza_kodi = diagnoza_kodi_var.get()
    diagnoza_pershkrimi = diagnoza_pershkrimi_var.get()
    shenime = shenime_text.get("1.0", tk.END)
    medikament = medikament_var.get()
    doza = doza_var.get()
    frekuenca = frekuenca_var.get()

    # Display the collected data for demonstration
    print(f"Pacient ID: {pacient_id}")
    print(f"Emri: {emri}")
    print(f"Data e Lindjes: {data_lindjes}")
    print(f"Grupi i Gjakut: {grupi_gjakut}")
    print(f"Numri i Kontrolleve: {numri_kontrolleve}")
    print(f"Data e Vizitës: {data_vizites}")
    print(f"Diagnoza Kodi: {diagnoza_kodi}")
    print(f"Diagnoza Përshkrimi: {diagnoza_pershkrimi}")
    print(f"Shënime: {shenime}")
    print(f"Medikament: {medikament}")
    print(f"Doza: {doza}")
    print(f"Frekuenca: {frekuenca}")

    messagebox.showinfo("Ruaj", "Të dhënat u ruajtën me sukses!")

def print_file():
    messagebox.showinfo("Print", "Po printohet dosja...")

def close_app():
    root.quit()

# Main window setup
root = tk.Tk()
root.title("Forma Mjekësore UI")
root.geometry("1000x750")  # Default window size

# Configure grid weights to allow resizing
root.columnconfigure(0, weight=1)  # Enable resizing for column 0
root.rowconfigure([0, 1, 2, 3], weight=1)  # Enable resizing for rows

# Applying a modern style to the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11), padding=5)
style.configure("TButton", font=("Arial", 11), padding=5)
style.configure("TFrame", padding=10)

# Creating a menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="E Re", command=new_file)
file_menu.add_command(label="Ruaj", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Printo", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Dalje", command=close_app)

menu_bar.add_cascade(label="Dosje", menu=file_menu)

# Adding the menu to the window
root.config(menu=menu_bar)

# Variables for storing user input
pacient_id_var = tk.StringVar()
emri_var = tk.StringVar()
data_lindjes_var = tk.StringVar()
grupi_gjakut_var = tk.StringVar()
numri_kontrolleve_var = tk.StringVar()
data_vizites_var = tk.StringVar()
diagnoza_kodi_var = tk.StringVar()
diagnoza_pershkrimi_var = tk.StringVar()
medikament_var = tk.StringVar()
doza_var = tk.StringVar()
frekuenca_var = tk.StringVar()

# Patient info frame (Informacioni i Pacientit)
pacient_frame = ttk.LabelFrame(root, text="Informacioni i Pacientit")
pacient_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Patient labels and entries
ttk.Label(pacient_frame, text="ID e Pacientit:").grid(row=0, column=0, sticky='e')
ttk.Entry(pacient_frame, textvariable=pacient_id_var, width=25).grid(row=0, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(pacient_frame, text="Emri:").grid(row=0, column=2, sticky='e')
ttk.Entry(pacient_frame, textvariable=emri_var, width=25).grid(row=0, column=3, padx=10, pady=5, sticky='ew')

ttk.Label(pacient_frame, text="Data e Lindjes:").grid(row=1, column=0, sticky='e')
ttk.Entry(pacient_frame, textvariable=data_lindjes_var, width=25).grid(row=1, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(pacient_frame, text="Grupi i Gjakut:").grid(row=1, column=2, sticky='e')
ttk.Entry(pacient_frame, textvariable=grupi_gjakut_var, width=25).grid(row=1, column=3, padx=10, pady=5, sticky='ew')

ttk.Label(pacient_frame, text="Numri i Kontrolleve:").grid(row=2, column=0, sticky='e')
ttk.Entry(pacient_frame, textvariable=numri_kontrolleve_var, width=25).grid(row=2, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(pacient_frame, text="Data e Vizitës:").grid(row=2, column=2, sticky='e')
ttk.Entry(pacient_frame, textvariable=data_vizites_var, width=25).grid(row=2, column=3, padx=10, pady=5, sticky='ew')

# Allow the pacient_frame to resize with the window
pacient_frame.columnconfigure([1, 3], weight=1)

# Diagnosis frame (Diagnoza)
diagnoza_frame = ttk.LabelFrame(root, text="Diagnoza")
diagnoza_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Diagnosis labels and entries
ttk.Label(diagnoza_frame, text="Kodi i Diagnozës:").grid(row=0, column=0, sticky='e')
ttk.Entry(diagnoza_frame, textvariable=diagnoza_kodi_var, width=25).grid(row=0, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(diagnoza_frame, text="Përshkrimi i Diagnozës:").grid(row=0, column=2, sticky='e')
ttk.Entry(diagnoza_frame, textvariable=diagnoza_pershkrimi_var, width=50).grid(row=0, column=3, padx=10, pady=5, sticky='ew')

# Enlarged Notes Textbox (Shënime)
ttk.Label(diagnoza_frame, text="Shënime:").grid(row=1, column=0, sticky='ne')
shenime_text = tk.Text(diagnoza_frame, height=12, width=60)  # Enlarged text box
shenime_text.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky='nsew')

# Make sure diagnosis fields resize properly
diagnoza_frame.columnconfigure([1, 3], weight=1)
diagnoza_frame.rowconfigure(1, weight=1)  # Allow the notes textbox to expand vertically

# Treatment frame (Trajtimi)
trajtimi_frame = ttk.LabelFrame(root, text="Trajtimi")
trajtimi_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

ttk.Label(trajtimi_frame, text="Medikament:").grid(row=0, column=0, sticky='e')
ttk.Entry(trajtimi_frame, textvariable=medikament_var, width=25).grid(row=0, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(trajtimi_frame, text="Doza:").grid(row=1, column=0, sticky='e')
ttk.Entry(trajtimi_frame, textvariable=doza_var, width=25).grid(row=1, column=1, padx=10, pady=5, sticky='ew')

ttk.Label(trajtimi_frame, text="Frekuenca:").grid(row=2, column=0, sticky='e')
ttk.Entry(trajtimi_frame, textvariable=frekuenca_var, width=25).grid(row=2, column=1, padx=10, pady=5, sticky='ew')

# Allow treatment frame to resize properly
trajtimi_frame.columnconfigure(1, weight=1)

# Action buttons with modern design
button_frame = ttk.Frame(root)
button_frame.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

ttk.Button(button_frame, text="Ruaj", command=save_file).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Mbyll", command=close_app).grid(row=0, column=1, padx=5, pady=5)

# Make the button frame and window responsive
button_frame.columnconfigure([0, 1], weight=1)
root.columnconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()
