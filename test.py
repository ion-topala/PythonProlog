import tkinter as tk
from tkinter import END

from pyswip import Prolog

# create a Prolog engine
prolog = Prolog()

# define Prolog rules
prolog.consult('TopalaIonTezaProlog.pl')


class MedicineApp:
    def __init__(self, master):
        self.master = master
        master.title("Medicine App")

        # Medication name input
        self.med_label = tk.Label(master, text="Enter medication name:", font=('Arial 12'))
        self.med_label.grid(row=0, column=0, padx=(75, 20), pady=20)

        self.med_entry = tk.Entry(master, font=('Arial 12'))
        self.med_entry.grid(row=0, column=1, padx=(75, 20), pady=10)

        # Predefined questions
        prologQueries = {
            1: "Show drug's medication class ",
            2: "Query drug's side effects",
            3: "What medicine interacts negative?",
            4: "Is the drug a beta-blocker?",
            5: "Is it the drug safe for pregnancy?",
            6: "Medications for symptoms",
        }

        # Radio buttons for selecting questions
        self.selected_question = tk.IntVar()
        self.radio_buttons = []
        for i, question in enumerate(prologQueries):
            radio_button = tk.Radiobutton(master, text=(prologQueries[question]), variable=self.selected_question,
                                          font=('Arial 10'),
                                          value=question)
            radio_button.grid(row=i + 1, column=0, padx=(75, 20), pady=10, sticky=tk.W)
            self.radio_buttons.append(radio_button)

        # Button to show answer for selected question
        self.answer_button = tk.Button(master, text="Show answer", font=('Arial 10'), command=self.show_answer)
        self.answer_button.grid(row=7, column=0, padx=(75, 20), pady=10, sticky=tk.W)

        # Button to clear answer label
        self.clear_button = tk.Button(master, text="Clear answer", font=('Arial 10'), command=self.clear_answer)
        self.clear_button.grid(row=7, column=1, padx=(75, 20), pady=10, sticky=tk.W)

        # Button to close the program
        # self.quit_button = tk.Button(master, text="Quit", font=('Arial 14'), command=master.quit)
        # self.quit_button.grid(row=8, column=0, padx=(75, 20), pady=10, sticky=tk.W)
        self.results = tk.Text(root)
        self.results.grid(row=8, column=0, columnspan=3, padx=(75, 20), sticky=tk.W)

        # Initialize answer dictionary
        self.answers = {}

    def show_answer(self):
        # Get current medication name
        medication = str(self.med_entry.get()).lower()
        if not medication:
            return
        # Get selected question
        key = self.selected_question.get()

        if key == 1:
            self.query_medication_class(medication)
        elif key == 2:
            self.query_side_effect(medication)
        elif key == 3:
            self.interacts_negative(medication)
        elif key == 4:
            self.is_beta_blocker(medication)
        elif key == 5:
            self.is_safe_for_pregnancy(medication)
        elif key == 6:
            self.medication_for_symptoms(medication)
        # Display question
        # self.question_label.config(text=question)

        # If answer for current question already exists, display it
        # if question in self.answers:
        #     self.answer_label.config(text=self.answers[question])
        # else:
        #     self.answer_label.config(text="No answer found.")

    def query(self, value):
        input_text = value.lower()
        self.query_medication_class(input_text)

    def query_medication_class(self, input_text):
        for result in prolog.query(f'medication_class({input_text}, MedicationClass)'):
            self.results.insert(END,
                                f'{input_text.title()} is from class {str(result["MedicationClass"]).title()}' + '\n')

    def query_side_effect(self, input_text):
        for result in prolog.query(f'side_effect({input_text}, SideEffect)'):
            self.results.insert(END,
                                f'{input_text.title()}\'s side effect is {str(result["SideEffect"]).title()}' + '\n')

    def interacts_negative(self, input_text):
        for result in prolog.query(f'interacts_with({input_text}, Medicine)'):
            self.results.insert(END,
                                f'{input_text.title()} interacts negative with {str(result["Medicine"]).title()}' + '\n')

    def medication_for_symptoms(self, input_text):
        for result in prolog.query(f'medication_for_symptom({input_text}, Symptom)'):
            drugList = []
            for drug in result['Symptom']:
                drugList.append(str(drug).title())
            drugMessage = ', '.join(drugList)
            self.results.insert(END,
                                f'For {input_text.lower()} you can use {drugMessage}' + '\n')

    def is_beta_blocker(self, input_text):
        for result in prolog.query(f'is_beta_blocker({input_text})'):
            if len(result) == 0:
                self.results.insert(END, 'Medication is a beta blocker' + '\n')
                return
        self.results.insert(END, 'Medication is not a beta blocker' + '\n')

    def is_safe_for_pregnancy(self, input_text):
        for result in prolog.query(f'safe_for_pregnancy({input_text})'):
            if len(result) == 0:
                self.results.insert(END, 'Medication is safe for pregnancy' + '\n')
                return
        self.results.insert(END, 'Medication is not safe for pregnancy' + '\n')

    def clear_answer(self):
        # Clear answer label
        self.results.delete('1.0', END)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x500")
    app = MedicineApp(root)
    app.run()
