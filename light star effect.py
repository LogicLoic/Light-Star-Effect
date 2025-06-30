#The higher is the Performance, The lower is the quality.

from tkinter import *
from random import *
from math import *

class Star:
    def __init__(self, x, y, size, color, angle):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.angle = angle
        self.graph = []

    def draw_star_line(self, size, color):
        angles = [self.angle, self.angle + pi/2, self.angle + pi, self.angle + 3*pi/2]
        points = [(self.x + size * cos(a), self.y + size * sin(a)) for a in angles]
        return [
            canvas.create_line(points[0][0], points[0][1], self.x, self.y, points[1][0], points[1][1], smooth=1, fill=color, width=1+Performance/2),
            canvas.create_line(points[1][0], points[1][1], self.x, self.y, points[2][0], points[2][1], smooth=1, fill=color, width=1+Performance/2),
            canvas.create_line(points[2][0], points[2][1], self.x, self.y, points[3][0], points[3][1], smooth=1, fill=color, width=1+Performance/2),
            canvas.create_line(points[3][0], points[3][1], self.x, self.y, points[0][0], points[0][1], smooth=1, fill=color, width=1+Performance/2)
        ]

    def draw_star(self):
        self.graph = []
        for step in range(0, self.size, Performance):
            self.graph.extend(self.draw_star_line(self.size - step, light_color(self.color, int(step/self.size*255))))
        for step in range(0, self.size, Performance):
            self.graph.extend(self.draw_star_line(2 * self.size - step, dark_color(self.color, int(step/self.size*255))))

def light_color(color, status):
    return f"#{hexa(status + (1 - status/255) * int(color[:2], 16))}{hexa(status + (1 - status/255) * int(color[2:4], 16))}{hexa(status + (1 - status/255) * int(color[4:], 16))}"

def dark_color(color, status):
    return f"#{hexa(status * int(color[:2], 16) / 255)}{hexa(status * int(color[2:4], 16) / 255)}{hexa(status * int(color[4:], 16) / 255)}"

def hexa(nb):
    h = hex(int(nb))[2:]
    if nb < 16:
        h = "0" + h
    if len(h) == 1:
        h = h + "0"
    return h

def realtime():
    global Performance
    try:
        Performance = int(entry.get())
        if Performance < 1:
            raise("Wrong performance value")
    except:
        entry.delete(0, END)
        entry.insert(0, int(sum([star.size for star in stars]) / 70) + 1)
        Performance = int(entry.get())
    
    try:
        Speed = float(entry2.get())
    except:
        entry2.delete(0, END)
        entry2.insert(0, 0.05)
        Speed = 0.05

    for star in stars:
        canvas.delete(*(star.graph))
        star.angle += Speed
        star.draw_star()
    window.after(1, realtime)

window = Tk()
window.title("Light star effect")

canvas = Canvas(window, width=1900, height=1000, bg="#000")
canvas.pack()

stars = [Star(450, 500, 1000, f"ff0000", 0), Star(1350, 500, 100, f"00ff00", 0), Star(1750, 500, 100, f"0000ff", 0)]

entry = Entry(window)
entry.insert(0, int(sum([star.size for star in stars]) / 70) + 1)
entry.place(x=1,y=1)

entry2 = Entry(window)
entry2.insert(0, 0.05)
entry2.place(x=1,y=20)

realtime()

window.mainloop()