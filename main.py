from pyswip import Prolog
from tkinter import *

# create a Prolog engine
prolog = Prolog()

# define Prolog rules
prolog.consult('TopalaIonTezaProlog.pl')

# create GUI
root = Tk()
root.geometry("1000x500")
root.title("PySWIP Prolog Interaction")

# define function to query Prolog and display results
def query():
    input_text = str(medication_input.get()).lower()
    query_medication_class(input_text)

def query_medication_class(input_text):
    for result in prolog.query(f'medication_class({input_text}, MedicationClass)'):
        results.insert(END, f'{input_text.title()} is from class {str(result["MedicationClass"]).title()}' + '\n')

# create user interface elements
medication_label = Label(root, text="Medication name:", font=('Arial 14'))
medication_label.grid(row=0, column=0, padx=(75, 20), pady=20)

medication_input = Entry(root, width=20, font=('Arial 14'))
medication_input.grid(row=0, column=1)

medication_button = Button(root, text="Search", command=query, font=('Arial 14') )
medication_button.grid(row=0, column=2, padx=50)
#
# results_label = Label(root, text="Results:")
# results_label.grid(row=1, column=0)
#
# medication_class = Label(root, text="Medication Class:", font=('Arial 14'))
# medication_class.grid(row=1, column=0, padx=(75, 20))

results = Text(root)
results.grid(row=2, column=0, columnspan=3, padx=(75, 20))

# start GUI event loop
root.mainloop()