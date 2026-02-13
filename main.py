from utils.openspace import Openspace
import pandas as pd


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


file_presenze = "presenze.xlsx"
# Read names from the Excel file
df = pd.read_excel(file_presenze, sheet_name="Sheet1")
names_column = df["Nome"].dropna()
names = names_column.tolist()

# Initialize Openspace and organize the names
ufficio = Openspace()
ufficio.organize(names)
ufficio.display()
ufficio.export_excel()
