#!/usr/bin/env python3
import time
import tkinter as tk
import random
from utils import new_grid, set_block, print_matrix

random.seed(0)


class MainApp():
    __playstate = False
    __grid_size = 20

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Conwey game of of life")
        self.app.geometry("1000x800")
        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.grid = tk.Frame(self.app, width="1000px", padx="10px", pady="10px", bg="red", cursor="dot", height="600px")
        self.grid.grid(row=0, column=0)
        self.grid.grid_propagate(1)

        self.button_con = tk.Frame(self.app, pady="10px", padx="10px", bd="5px", highlightbackground="yellow",
                                   highlightcolor="green")
        self.button_con.grid(row=1, column=0)
        self.play = tk.Button(master=self.button_con, text="Play", bg="green", command=self.run)
        self.nexts = tk.Button(master=self.button_con, text="Next", bg="green", command=self.next_grid)
        self.pause = tk.Button(master=self.button_con, text="Pause", bg="yellow", command=self.stop_run, )
        self.reset = tk.Button(master=self.button_con, text="Reset", bg="red", command=self.reset_grid)
        self.clear = tk.Button(master=self.button_con, text="clear", bg="red", command=self.clear_grid)

        self.play.pack(side=tk.LEFT)
        self.nexts.pack(side=tk.LEFT)
        self.pause.pack(side=tk.LEFT)
        self.reset.pack(side=tk.LEFT)
        self.clear.pack(side=tk.LEFT)

        self.m_grid = [[random.randint(0, 1) for _ in range(self.__grid_size * 2)]
                       for _ in range(self.__grid_size)]
        self.base_grid = self.m_grid.copy()
        self.g_buttons = [[0 for _ in range(self.__grid_size * 2)] for _ in range(self.__grid_size)]

        for idxi, li in enumerate(self.m_grid):
            for idxj, val in enumerate(li):
                self.g_buttons[idxi][idxj] = tk.Button(self.grid, height=1, width=1, pady="0px", padx="1px",
                                                       highlightbackground="blue",
                                                       relief=tk.FLAT,
                                                       bg="{}".format("white" if val == 1 else "black"),
                                                       command=lambda i=idxi, j=idxj: self.set_grid(i, j))

        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                self.g_buttons[i][j].grid(row=i, column=j)

    def update_grid(self):
        self.m_grid = new_grid(self.m_grid, self.__grid_size)
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("white" if val == 1 else "black"))
        time.sleep(.1)

        self.app.update()

    @classmethod
    def grid_size(cls, n):
        if n > 30:
            print("grid too  large")
        else:
            cls.__grid_size = n

    def reset_grid(self):
        self.__playstate = False

        self.m_grid = self.base_grid.copy()
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("white" if val == 1 else "black"))
        self.app.update()

    def set_grid(self, i, j):
        self.m_grid[i][j] = 0 if self.m_grid[i][j] == 1 else 1
        val = self.m_grid[i][j]
        self.g_buttons[i][j].config(bg="{}".format("white" if val == 1 else "black"))

        self.app.update()

    def clear_grid(self):
        self.__playstate = False

        self.m_grid = [[0 for _ in range(self.__grid_size * 2)] for _ in range(self.__grid_size)]
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("white" if val == 1 else "black"))
        time.sleep(.1)

        self.app.update()

    def next_grid(self):
        self.update_grid()
        self.__init__()

    def run(self):
        self.__playstate = True
        while self.__playstate:
            self.update_grid()

    def stop_run(self):
        self.__playstate = False
        print("working")

    def mainloop(self):
        self.app.mainloop()


if __name__ == '__main__':
    MainApp.grid_size(30)

    app = MainApp()
    app.mainloop()
