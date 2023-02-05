import tkinter as tk
from tkinter import messagebox

def solve(a, b):
    n = len(b)
    for i in range(n):
        pivot = max(range(i, n), key=lambda j: abs(a[j][i]))
        if i != pivot:
            a[i], a[pivot] = a[pivot], a[i]
            b[i], b[pivot] = b[pivot], b[i]
        for j in range(i+1, n):
            m = a[j][i] / a[i][i]
            b[j] -= m * b[i]
            for k in range(i, n):
                a[j][k] -= m * a[i][k]
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i+1, n))) / a[i][i]
    return x

def submit():
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(entries[i][j].get()))
        a.append(row)
    b = [float(entries[i][n].get()) for i in range(n)]
    x = solve(a, b)
    message = "La solución es:\n" + "\n".join(f"x{i+1} = {xi}" for i, xi in enumerate(x))
    messagebox.showinfo("Resultado", message)

root = tk.Tk()
root.title("Resolución de sistemas de ecuaciones lineales 3x3")

n = 3
entries = []
for i in range(n):
    row = []
    for j in range(n+1):
        entry = tk.Entry(root)
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

button = tk.Button(root, text="RESULTADO", command=submit)
button.grid(row=n, column=0, columnspan=n+1, sticky="E")

root.mainloop()