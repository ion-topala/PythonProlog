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
        self.med_label = tk.Label(master, text="Enter medication name:", font=('Arial 14'))
        self.med_label.grid(row=0, column=0, padx=(75, 20), pady=20)

        self.med_entry = tk.Entry(master, font=('Arial 14'))
        self.med_entry.grid(row=0, column=1, padx=(75, 20), pady=10)

        # Predefined questions
        questionsV2 = {
            1: "Show drug's medication class ",
            2: "Another question"
        }
        # self.questions = [
        #     "What is the dosage for this medication?",
        #     "What are the potential side effects of this medication?",
        #     "How long should I take this medication for?",
        #     "What should I do if I miss a dose of this medication?"
        # ]

        # Radio buttons for selecting questions
        self.selected_question = tk.IntVar()
        self.radio_buttons = []
        for i, question in enumerate(questionsV2):
            radio_button = tk.Radiobutton(master, text=(questionsV2[question]), variable=self.selected_question,
                                          font=('Arial 14'),
                                          value=question)
            radio_button.grid(row=i + 1, column=0, padx=(75, 20), pady=10, sticky=tk.W)
            self.radio_buttons.append(radio_button)

        # Button to show answer for selected question
        self.answer_button = tk.Button(master, text="Show answer", font=('Arial 14'), command=self.show_answer)
        self.answer_button.grid(row=7, column=0, padx=(75, 20), pady=10, sticky=tk.W)

        # Button to clear answer label
        self.clear_button = tk.Button(master, text="Clear answer", font=('Arial 14'), command=self.clear_answer)
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
        medication = self.med_entry.get()

        # Get selected question
        question = self.selected_question.get()
        self.query(medication)

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
