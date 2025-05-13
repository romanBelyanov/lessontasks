from tkinter import *

def plustime():
    global minutes, seconds, canvas, lbl, win
    if not win:
        minutes, seconds = int(minutes), int(seconds)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        lbl["text"] = f"{minutes}:{seconds}"
        canvas.after(1000, plustime)

def game():
    global root, canvas, matrix, win, now_turn, minutes, seconds, lbl
    minutes = 0
    seconds = 0
    root = Tk()
    root.geometry("1200x750")
    root.title("Крестики-нолики")
    canvas = Canvas(bg="white", width=750, height=750)
    canvas.grid(row=0, column=0)
    canvas.create_rectangle(245, 0, 255, 750, fill="black")
    canvas.create_rectangle(495, 0, 505, 750, fill="black")
    canvas.create_rectangle(0, 245, 750, 255, fill="black")
    canvas.create_rectangle(0, 495, 750, 505, fill="black")
    lbl = Label(root, text="00:00")
    lbl.config(font=("Arial", 30))
    lbl.grid(row=0, column=1)
    canvas.after(1000, plustime)

    matrix = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    win = False
    now_turn = 0
    root.bind("<ButtonPress>", pressed)
    root.mainloop()

def yes():
    root.destroy()
    game()

def no():
    root.destroy()

def show_window(text):
    global win
    win = True
    second_win = Toplevel(root)
    second_win.title("Второе окно")
    Label(second_win, text=text).grid(row=0, column=0, columnspan=2)
    Label(second_win, text="Сыграть ещё раз?").grid(row=1, column=0, columnspan=2)
    Button(second_win, text="Да", command=yes).grid(row=2, column=0)
    Button(second_win, text="Нет", command=no).grid(row=2, column=1)
def who_win(matrix):
    if matrix[0][0] == 0 and matrix[0][1] == 0 and matrix[0][2] == 0:
        canvas.create_line(0, 125, 750, 125, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[1][0] == 0 and matrix[1][1] == 0 and matrix[1][2] == 0:
        canvas.create_line(0, 375, 750, 375, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[2][0] == 0 and matrix[2][1] == 0 and matrix[2][2] == 0:
        canvas.create_line(0, 625, 750, 625, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][0] == 0 and matrix[1][0] == 0 and matrix[2][0] == 0:
        canvas.create_line(125, 0, 125, 750, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][1] == 0 and matrix[1][1] == 0 and matrix[2][1] == 0:
        canvas.create_line(375, 0, 375, 750, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][2] == 0 and matrix[1][2] == 0 and matrix[2][2] == 0:
        canvas.create_line(625, 0, 625, 750, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0:
        canvas.create_line(0, 0, 750, 750, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][2] == 0 and matrix[1][1] == 0 and matrix[2][0] == 0:
        canvas.create_line(750, 0, 0, 750, width=20, fill="red")
        show_window("Нолики выиграли")
    elif matrix[0][0] == 1 and matrix[0][1] == 1 and matrix[0][2] == 1:
        canvas.create_line(0, 125, 750, 125, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[1][0] == 1 and matrix[1][1] == 1 and matrix[1][2] == 1:
        canvas.create_line(0, 375, 750, 375, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[2][0] == 1 and matrix[2][1] == 1 and matrix[2][2] == 1:
        canvas.create_line(0, 625, 750, 625, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[0][0] == 1 and matrix[1][0] == 1 and matrix[2][0] == 1:
        canvas.create_line(125, 0, 125, 750, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[0][1] == 1 and matrix[1][1] == 1 and matrix[2][1] == 1:
        canvas.create_line(375, 0, 375, 750, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[0][2] == 1 and matrix[1][2] == 1 and matrix[2][2] == 1:
        canvas.create_line(625, 0, 625, 750, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[2][2] == 1:
        canvas.create_line(0, 0, 750, 750, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif matrix[0][2] == 1 and matrix[1][1] == 1 and matrix[2][0] == 1:
        canvas.create_line(750, 0, 0, 750, width=20, fill="darkblue")
        show_window("Крестики выиграли")
    elif "x" not in matrix[0] and "x" not in matrix[1] and "x" not in matrix[2]:
        show_window("Ничья")





class Circle:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
    def draw(self, place_x, place_y):
        if place_x == 1:
            x = 125
        elif place_x == 2:
            x = 375
        elif place_x == 3:
            x = 625
        if place_y == 1:
            y = 125
        elif place_y == 2:
            y = 375
        elif place_y == 3:
            y = 625
        self.canvas.create_oval(y-115, x-115, y+115, x+115, fill="red", outline="red")
        self.canvas.create_oval(y-95, x-95, y+95, x+95, fill="white", outline="white")
        matrix[place_x-1][place_y-1] = 0

class XCross:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
    def draw(self, place_x, place_y):
        if place_x == 1:
            x = 125
        elif place_x == 2:
            x = 375
        elif place_x == 3:
            x = 625
        if place_y == 1:
            y = 125
        elif place_y == 2:
            y = 375
        elif place_y == 3:
            y = 625
        self.canvas.create_line(y-100, x-100, y+100, x+100, width=20, fill="darkblue")
        self.canvas.create_line(y+100, x-100, y-100, x+100, width=20, fill="darkblue")
        matrix[place_x-1][place_y-1] = 1




def pressed(event):
    global now_turn, matrix, win
    x, y = event.x, event.y
    circle = Circle(root, canvas)
    xcross = XCross(root, canvas)
    if x <= 250:
        place_x = 1
    elif x <= 500:
        place_x = 2
    elif x <= 750:
        place_x = 3
    if y <= 250:
        place_y = 1
    elif y <= 500:
        place_y = 2
    elif y <= 750:
        place_y = 3
    try:
        if matrix[place_y-1][place_x-1] == "x" and not win:
            if now_turn == 0:
                circle.draw(place_y, place_x)
                now_turn = 1
                who_win(matrix)
            elif now_turn == 1:
                xcross.draw(place_y, place_x)
                now_turn = 0
                who_win(matrix)
    except:
        pass


game()