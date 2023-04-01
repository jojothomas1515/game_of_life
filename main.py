#!/usr/bin/env python3
import time
import tkinter as tk
import random
from utils import new_grid, set_block

random.seed(1)
grid = [[random.randint(0, 1) for _ in range(20)] for _ in range(20)]

app = tk.Tk()
app.title("Conwey game of of life")
app.geometry("800x600")
for i, val in enumerate(grid):
    for j, vj in enumerate(val):
        tk.Button(app, height=1, width=2, pady="1px", padx="2px", bg="{}".format("white" if vj == 0 else "black"),
                  relief=tk.SUNKEN, bd="1px", highlightcolor="blue").grid(row=i, column=j)


def updater(grid):

    for child in app.winfo_children():
        child.destroy()
    grid= new_grid(grid, 20)

    for i, val in enumerate(grid):
        for j, vj in enumerate(val):
            tk.Button(app, height=1, width=2, pady="1px", padx="2px", bg="{}".format("white" if vj == 0 else "black"),
                      relief=tk.SUNKEN, bd="1px", highlightbackground="black").grid(row=i, column=j)
    app.update()

    app.after(100, lambda :updater(grid))


app.after(5, lambda :updater(grid))
app.mainloop()
