import tkinter as tk
from tkinter import messagebox

def possible_blood_types(abo_father, abo_mother, rh_father, rh_mother):
    # ABO blood type combinations
    blood_combinations = {
        'AA': 'A',
        'AO': 'A',
        'OA': 'A',
        'BB': 'B',
        'BO': 'B',
        'OB': 'B',
        'AB': 'AB',
        'BA': 'AB',
        'OO': 'O'
    }

    blood_alleles = {
        'A': ['A', 'O'],
        'B': ['B', 'O'],
        'AB': ['A', 'B'],
        'O': ['O']
    }

    father_alleles = blood_alleles[abo_father]
    mother_alleles = blood_alleles[abo_mother]
    possible_allele_combinations = [f + m for f in father_alleles for m in mother_alleles]

    abo_count = {}
    for combo in possible_allele_combinations:
        blood_type = blood_combinations[combo]
        abo_count[blood_type] = abo_count.get(blood_type, 0) + 1

    total_abo_combinations = len(possible_allele_combinations)
    abo_percentages = {key: (value / total_abo_combinations) * 100 for key, value in abo_count.items()}

    # Rh factor combinations
    if rh_father == '-' and rh_mother == '-':
        rh_percentages = {'-': 100}
    elif rh_father == '+' and rh_mother == '+':
        rh_percentages = {'+': 75, '-': 25}
    else:
        rh_percentages = {'+': 50, '-': 50}

    return abo_percentages, rh_percentages

# Function to calculate probabilities and update the result_text widget
def calculate_probabilities():
    abo_father = abo_father_entry.get().upper()
    rh_father = rh_father_var.get()

    abo_mother = abo_mother_entry.get().upper()
    rh_mother = rh_mother_var.get()

    if (abo_father not in ['A', 'B', 'AB', 'O'] or abo_mother not in ['A', 'B', 'AB', 'O'] or
            rh_father not in ['+', '-'] or rh_mother not in ['+', '-']):
        messagebox.showerror("Error", "Invalid input. Please enter correct blood types and Rh factors.")
    else:
        abo_percentages, rh_percentages = possible_blood_types(abo_father, abo_mother, rh_father, rh_mother)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Based on the parents' blood types, the probabilities for the child's blood type are:\n")
        for abo, abo_pct in abo_percentages.items():
            for rh, rh_pct in rh_percentages.items():
                combined_pct = (abo_pct / 100) * rh_pct
                result_text.insert(tk.END, f"{abo}{rh}: {combined_pct:.2f}%\n")

# GUI setup
root = tk.Tk()
root.title("Blood Type Probability Calculator")



# Labels and Entry Widgets

tk.Label(root, text="Father's ABO Blood Type:",foreground="purple",background="lavender").grid(row=0, column=0, padx=10, pady=5, sticky="e")
abo_father_entry = tk.Entry(root)
abo_father_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Father's Rh Factor:",foreground="purple",background="lavender").grid(row=1, column=0, padx=10, pady=5, sticky="e")
rh_father_var = tk.StringVar(value='+')
tk.Radiobutton(root, text='+', variable=rh_father_var, value='+').grid(row=1, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text='-', variable=rh_father_var, value='-').grid(row=1, column=1, padx=5, pady=5, sticky="e")

tk.Label(root, text="Mother's ABO Blood Type:",foreground="purple",background="lavender").grid(row=2, column=0, padx=10, pady=5, sticky="e")
abo_mother_entry = tk.Entry(root)
abo_mother_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Mother's Rh Factor:",foreground="purple",background="lavender").grid(row=3, column=0, padx=10, pady=5, sticky="e")
rh_mother_var = tk.StringVar(value='+')
tk.Radiobutton(root, text='+', variable=rh_mother_var, value='+').grid(row=3, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text='-', variable=rh_mother_var, value='-').grid(row=3, column=1, padx=5, pady=5, sticky="e")

# Button to calculate probabilities
calculate_button = tk.Button(root, text="Calculate Probabilities", command=calculate_probabilities,background="dark violet",fg="white")
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Text widget to display results
result_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)
result_text.grid(row=5, column=0, columnspan=2, padx=10)

root.mainloop()
