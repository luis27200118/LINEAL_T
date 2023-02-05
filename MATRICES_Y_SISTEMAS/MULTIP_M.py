import tkinter as tk
from tkinter import messagebox

def multiply_matrices():
    try:
        matrix1 = [[int(j.get()) for j in i] for i in matrix1_entries]
        matrix2 = [[int(j.get()) for j in i] for i in matrix2_entries]
        
        result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        
        messagebox.showinfo("Result", str(result))
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos en las entradas de las matrices")

def create_matrix_inputs(matrix_entries, matrix_input_frame, rows, columns):
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = tk.Entry(matrix_input_frame, width=3)
            entry.grid(row=i, column=j)
            row.append(entry)
        matrix_entries.append(row)

root = tk.Tk()
root.title("Multiplicación de Matrices")

matrix1_entries = []
matrix2_entries = []

matrix1_label = tk.Label(root, text="Matriz 1")
matrix1_label.grid(row=0, column=0, columnspan=3)

matrix1_input_frame = tk.Frame(root)
matrix1_input_frame.grid(row=1, column=0, columnspan=3)

create_matrix_inputs(matrix1_entries, matrix1_input_frame, 3, 3)

matrix2_label = tk.Label(root, text="Matriz 2")
matrix2_label.grid(row=0, column=3, columnspan=3)

matrix2_input_frame = tk.Frame(root)
matrix2_input_frame.grid(row=1, column=3, columnspan=3)

create_matrix_inputs(matrix2_entries, matrix2_input_frame, 3, 3)

multiply_button = tk.Button(root, text="Multiplicar", command=multiply_matrices)
multiply_button.grid(row=2, column=0, columnspan=6)

root.mainloop()
