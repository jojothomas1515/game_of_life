#!/usr/bin/env python
"""Implementaion of conway game of life with TKinter."""
import random
import time
import tkinter as tk
from utils import new_grid

random.seed(0)


class MainApp:
    """
    Contains all the needed code of conway gui implementation.

    For the gird to be more on the screen  gird size is use on the display grid as
    "Rows(__grid_size) x Columns(__grid_size * 2)".

    Args:
        __playstate (bool): solely for the purpose of pausing the iterations
        __grid_size (int): size of the grid to be display
    """
    __playstate = False
    __grid_size = 20

    def __init__(self):
        """
        Construct the window/frames/and button and append them to the
        appropriate containers.
        """

        self.app = tk.Tk()
        self.app.title("Conway game of of life")
        self.app.geometry("1000x800")
        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)

        # frame to hold all the grid items
        self.grid = tk.Frame(self.app, width="1000px", padx="2px", pady="2px", bg="black", cursor="dot", height="600px")
        self.grid.grid(row=0, column=0)
        self.grid.grid_propagate(True)  # if true the frame can grow to fit the content

        # frame holds all the control buttons
        self.button_con = tk.Frame(self.app, pady="10px", padx="10px", bd="5px")
        self.button_con.grid(row=1, column=0)

        # control buttons creation
        self.play = tk.Button(master=self.button_con, text="Play", command=self.run)
        self.nexts = tk.Button(master=self.button_con, text="Next", command=self.next_grid)
        self.pause = tk.Button(master=self.button_con, text="Pause", command=self.stop_run, )
        self.reset = tk.Button(master=self.button_con, text="Reset", command=self.reset_grid)
        self.clear = tk.Button(master=self.button_con, text="clear", command=self.clear_grid)
        self.clear = tk.Button(master=self.button_con, text="clear", command=self.clear_grid)

        # control buttons placement
        self.play.pack(side=tk.LEFT)
        self.nexts.pack(side=tk.LEFT)
        self.pause.pack(side=tk.LEFT)
        self.reset.pack(side=tk.LEFT)
        self.clear.pack(side=tk.LEFT)

        # conway n * n*2 matrix grid representing the cells
        self.m_grid = self.make_grid(1)
        self.base_grid = self.m_grid.copy()

        # grid to store the matrix items
        self.g_buttons = self.make_grid(0)

        # create, add and place buttons on the grid
        for idxi, li in enumerate(self.m_grid):
            for idxj, val in enumerate(li):
                self.g_buttons[idxi][idxj] = tk.Button(self.grid, height=1, width=1, pady="0px", padx="1px",
                                                       highlightbackground="#555555",
                                                       relief=tk.FLAT,
                                                       bg="{}".format("yellow" if val == 1 else "gray"),
                                                       command=lambda i=idxi, j=idxj: self.set_grid(i, j))
                self.g_buttons[idxi][idxj].grid(row=idxi, column=idxj)

    def make_grid(self, r: int) -> [[]]:
        """
        Create a grid with each cell having a random value between
        0 and r
        Args:
            r (int):

        Returns:
            grid
        """
        return [[random.randint(0, r) for _ in range(self.__grid_size * 2)]
                for _ in range(self.__grid_size)]

    def update_grid(self):
        """ Update the grid cells with the conway rules and update the display."""
        self.m_grid = new_grid(self.m_grid, self.__grid_size)
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("yellow" if val == 1 else "gray"))
        time.sleep(.1)

        self.app.update()

    @classmethod
    def grid_size(cls, size: int):
        """
        classmethod use to set the size of the grid/

        Args:
            size (int): size

        Returns:

        """
        if size > 30:
            print("grid too large using default")
        else:
            cls.__grid_size = size

    def reset_grid(self):
        """ Reset grid to the default state when the program was initially ran."""
        self.__playstate = False
        self.m_grid = self.base_grid.copy()
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("yellow" if val == 1 else "gray"))
        self.app.update()

    def set_grid(self, i, j):
        """
        callback command for the grid items buttons to set as cell
        to living or dead.
        Args:
            i (int): row for the cell
            j (int): column of the cell
        """
        self.m_grid[i][j] = 0 if self.m_grid[i][j] == 1 else 1
        val = self.m_grid[i][j]
        self.g_buttons[i][j].config(bg="{}".format("yellow" if val == 1 else "gray"))
        self.app.update()

    def clear_grid(self):
        """ Set all the cells in the grid to dead cell"""
        self.__playstate = False
        self.m_grid = self.make_grid(0)
        for i, li in enumerate(self.g_buttons):
            for j, val in enumerate(li):
                val = self.m_grid[i][j]
                self.g_buttons[i][j].config(bg="{}".format("yellow" if val == 1 else "gray"))
        time.sleep(.1)
        self.app.update()

    def next_grid(self):
        """ Update the program to the next state of the grid cells."""
        self.__playstate = False
        self.update_grid()

    def run(self):
        """ Infinitely iterate and display the states of the grid cells. """
        self.__playstate = True
        while self.__playstate:
            self.update_grid()

    def stop_run(self):
        """ Pause the infinite iteration started by run."""
        self.__playstate = False

    def mainloop(self):
        """runs the gui."""
        self.app.mainloop()

if __name__ == '__main__':
    MainApp.grid_size(30)
    MainApp().mainloop()
