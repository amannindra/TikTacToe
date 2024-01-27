import random 
from tkinter import *
import re

'''
root = Tk()

root.title("My First Window")
root.geometry('300x200')
canvas = Canvas()

canvas.create_rectangle(10,10,110,110,outline ="black",fill ="white",width = 2)
canvas.create_rectangle(10,10,110,110,outline ="black",fill ="white",width = 2)
canvas.create_rectangle(10,10,110,110,outline ="black",fill ="white",width = 2)
canvas.create_rectangle(10,10,110,110,outline ="black",fill ="white",width = 2)

canvas.pack()
root.mainloop()
'''


class TikTakToe():
        
    def __init__(self):
        self.grid = []
        self.user_input = []
        self.x_cord = 1
        self.y_cord = 1
    def start(self):
        for i in range(3):
            row = [" ", " ", " "]
            for i in range(3):
                self.grid.append(row)
    def get_input(self):
        while True:
            self.get_x_cords()
            if not self.x_cord.isdigit() or not (1 <= int(self.x_cord) <= 3):
                continue

            self.get_y_cords()
            if not self.y_cord.isdigit() or not (1 <= int(self.y_cord) <= 3):
                continue

            self.x_cord = int(self.x_cord)
            self.y_cord = int(self.y_cord)
            break

        print(self.x_cord, self.y_cord)

    
    def get_x_cords(self):
        self.x_cord = (input("Give me your X coordinate: "))

    def get_y_cords(self):
        self.y_cord = (input("Give me your Y coordinate: "))

    def print(self):   
        for i in range(3):
            print(self.grid[i])

tiktak = TikTakToe()
tiktak.start()
tiktak.print()
tiktak.get_input()