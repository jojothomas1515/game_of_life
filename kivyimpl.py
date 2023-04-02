#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import *
from kivy.clock import Clock
from utils import new_grid
import random

n = 20
layout = GridLayout(cols=1,
                    rows=n, )
random.seed(1)
grid = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

for i in range(n):
    sublayout = GridLayout(rows=1, cols=n)
    for j in range(n):
        sublayout.add_widget(
            Button(background_color="{}".format("white" if grid[i][j] == 0 else "green"), ))
    layout.add_widget(sublayout)




class MainApp(App):
    def updater(self, grid, n):
        temp = new_grid(grid, n)

        for i in range(n):
            for j in range(n):
                grid[i][j] = temp[i][j]

        for idxi, but_li in enumerate(layout.children):
            for idxj , but in enumerate(but_li.children):
                if grid[idxi][idxj] == 1:
                    but.background_color = "green"
                else:
                    but.background_color = "white"

    def running(self):
        print("running")
    def build(self):
        Clock.max_iteration = 100
        Clock.schedule_interval(lambda x : self.updater(grid, n), .2)
        return layout


MainApp().run()
