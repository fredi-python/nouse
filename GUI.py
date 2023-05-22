import json
import os.path
import tkinter as tk
from tkinter import filedialog

def save_to_json_file(instruction, output_data, filename="HomoScriptor.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    entry = {
        "instruction": instruction,
        "output": output_data
    }

    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

def save_data():
    instruction = instruction_text.get("1.0", tk.END).strip()
    output_data = output_text.get("1.0", tk.END).strip()
    save_to_json_file(instruction, output_data)
    instruction_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HomoScriptor GUI")

    instruction_label = tk.Label(root, text="Instruction:")
    instruction_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="nw")
    instruction_text = tk.Text(root, width=50, height=6, wrap=tk.WORD)
    instruction_text.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))

    output_label = tk.Label(root, text="Output Data:")
    output_label.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky="nw")
    output_text = tk.Text(root, width=50, height=6, wrap=tk.WORD)
    output_text.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

    save_button = tk.Button(root, text="Save", command=save_data)
    save_button.grid(row=2, columnspan=2, pady=(0, 10))

    root.mainloop()
