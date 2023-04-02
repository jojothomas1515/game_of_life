#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import *
from kivy.clock import Clock
from utils import new_grid
import random

n = 20
layout = GridLayout(cols=1,
                    rows=n, )
m_window = GridLayout(rows=2, cols=1)
button_con = GridLayout(rows=1, cols=4, size_hint_y=None, height=50)
play = Button(text="Play", background_color="green")
pause = Button(text="Pause", background_color="yellow")
next_b = Button(text="Next", background_color="blue")
reset = Button(text="Reset", background_color="red")

button_con.add_widget(play)
button_con.add_widget(pause)
button_con.add_widget(next_b)
button_con.add_widget(reset)

m_window.add_widget(layout)
m_window.add_widget(button_con)

random.seed(1)


class MainApp(App):
    c_evn: object

    def __init__(self):
        self.grid = grid = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        self.first_grid = self.grid.copy()
        self.setup()
        play.bind(on_press=lambda e: self.play())
        pause.bind(on_press=lambda e: self.pause())
        next_b.bind(on_press=lambda e: self.next())
        reset.bind(on_press=lambda e: self.reset())
        super().__init__()


    def setup(self):
        for i in range(n):
            sublayout = GridLayout(rows=1, cols=n)
            for j in range(n):
                sublayout.add_widget(
                        Button(background_color="{}".format("white" if self.grid[i][j] == 0 else "green"), ))
            layout.add_widget(sublayout)

    def play(self):
        Clock.max_iteration = 1000
        if (len(Clock.get_events()) < 2):
            self.c_evn = Clock.schedule_interval(lambda x: self.updater(n), .2)

    def next(self):
        Clock.max_iteration = 1000
        if (len(Clock.get_events()) < 2):
            self.c_evn = Clock.schedule_once(lambda x: self.updater(n), .2)

    def pause(self, *largs):
        Clock.unschedule(self.c_evn)

    def reset(self):
        self.grid = self.first_grid
        for idxi, but_li in enumerate(layout.children):
            for idxj, but in enumerate(but_li.children):
                if self.grid[idxi][idxj] == 1:
                    but.background_color = "green"
                else:
                    but.background_color = "white"

    def updater(self, n):
        temp = new_grid(self.grid, n)

        for i in range(n):
            for j in range(n):
                self.grid[i][j] = temp[i][j]

        for idxi, but_li in enumerate(layout.children):
            for idxj, but in enumerate(but_li.children):
                if self.grid[idxi][idxj] == 1:
                    but.background_color = "green"
                else:
                    but.background_color = "white"

    def build(self):
        return m_window


MainApp().run()
