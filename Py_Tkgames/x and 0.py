import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("X and 0")
root.geometry("300x300")

canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

# create the grids
def draw_grid():
    for i in range(2):
        canvas.create_line(100 * (i + 1), 0, 100 * (i + 1), 300, fill="white", width=3)
        canvas.create_line(0, 100 * (i + 1), 300, 100 * (i + 1), fill="white", width=3)

draw_grid()

# create the x and 0
def create_x(x, y):
    canvas.create_line(x, y, x + 100, y + 100, fill="red", width=3)
    canvas.create_line(x + 100, y, x, y + 100, fill="red", width=3)

def create_0(x, y):
    canvas.create_oval(x, y, x + 100, y + 100, outline="blue", width=3)

# create the game
def create_game():
    global player
    player = "x"
    global game
    game = [[None, None, None], [None, None, None], [None, None, None]]
    global game_over
    game_over = False
    canvas.delete("all")
    draw_grid()

create_game()

def check_game_over():
    global game_over
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] is not None:
            game_over = True
            return game[i][0]
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] is not None:
            game_over = True
            return game[0][i]
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] is not None:
        game_over = True
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] is not None:
        game_over = True
        return game[0][2]
    if all([all(row) for row in game]):
        game_over = True
        return "Tie"
    return None

def click(event):
    global player  # Declare player as global
    if game_over:
        return
    x, y = event.x // 100, event.y // 100
    if game[y][x] is None:
        if player == "x":
            create_x(x * 100, y * 100)
            game[y][x] = "x"
            player = "0"
        else:
            create_0(x * 100, y * 100)
            game[y][x] = "0"
            player = "x"
    winner = check_game_over()
    if winner:
        if winner == "Tie":
            messagebox.showinfo("Game Over", "It's a tie")
        else:
            messagebox.showinfo("Game Over", f"{winner} wins")
        create_game()

canvas.bind("<Button-1>", click)

root.mainloop()