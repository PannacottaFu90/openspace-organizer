from utils.openspace import Openspace
import pandas as pd
import tkinter as tk
import os
from tkinter import filedialog


"""names = [
    "Mario",
    "Luigi",
    "Peach",
    "Daisy",
    "Yoshi",
    "Yuji",
    "Todo",
    "Gojo",
    "Geto",
    "Rosalia",
    "Super Ape",
    "Dennis Brown",
    "Bob",
    "Enzo Dong",
    "ALi",
    "Rox",
    "Kirby",
    "Fox",
    "pippo",
    "mango",
    "cocco",
    "Yellowman",
    "Marth",
    "Nancy",
    "edo",
    "tommy",
]"""

# Nasconde la finestra principale di tkinter
root = tk.Tk()
root.withdraw()

print(
    "Seleziona il file delle presenze dalla finestra che si è aperta.\nInput files: *.xlsx *.xls, *.csv  \nAssicurati che non ci siano intestazioni \n Se carichi un file excel, i nomi devono essere nella prima colonna"
)
path = filedialog.askopenfilename(
    title="Seleziona File Presenze",
    filetypes=[
        ("File supportati", "*.xlsx *.xls, *.csv"),
        ("Excel files", "*.xlsx *.xls"),
        ("CSV files", "*.csv"),
    ],
)

if path:
    extension = os.path.splitext(path)[1].lower()

    try:
        if extension == ".csv":
            df = pd.read_csv(path, header=None, sep=None, engine="python")
        else:
            df = pd.read_excel(path, header=None)

        names_column = df.iloc[
            :, 0
        ].dropna()  # Prende la prima colonna e rimuove eventuali valori NaN
        names = names_column.tolist()

    except Exception as e:
        print(f"Errore durante la lettura del file {extension}: {e}")
        sys.exit()

# Initialize Openspace and organize the names
ufficio = Openspace()
ufficio.organize(names)
ufficio.display()
ufficio.export_excel()
ufficio.visualization()
