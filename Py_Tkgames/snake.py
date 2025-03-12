import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

#canvas

canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

#snake

snake = [(100, 100), (80, 100), (60, 100)] 
snake_dir = (20, 0)
snake_color = "green"

# food

food = (200, 200)
food_color = "red"

# score

score = 0

def draw_snake():
    for x, y in snake:
        canvas.create_rectangle(x, y, x+20, y+20, fill=snake_color)

def draw_food():
    x, y = food
    canvas.create_rectangle(x, y, x+20, y+20, fill=food_color)

def move_snake():
    global snake_dir
    x, y = snake[0]
    x += snake_dir[0]
    y += snake_dir[1]
    snake.insert(0, (x, y))
    snake.pop()

def check_collision():
    x, y = snake[0]
    if x < 0 or x >= 600 or y < 0 or y >= 600:
        return True
    if snake[0] in snake[1:]:
        return True
    return False

def check_food():
    global food, score
    if snake[0] == food:
        snake.append(snake[-1])
        score += 1
        x = random.randint(0, 29) * 20
        y = random.randint(0, 29) * 20
        food = (x, y)

def game_over():
    canvas.delete("all")
    canvas.create_text(300, 300, text="Game Over", fill="white", font=("Arial", 24))

def game_loop():
    if check_collision():
        game_over()
        return
    check_food()
    canvas.delete("all")
    draw_snake()
    draw_food()
    move_snake()
    canvas.create_text(50, 50, text=f"Score: {score}", fill="white", font=("Arial", 24))
    root.after(100, game_loop)

def change_direction(new_dir):
    global snake_dir
    # Prevent reversing direction
    if (new_dir[0] != -snake_dir[0]) and (new_dir[1] != -snake_dir[1]):
        snake_dir = new_dir

root.bind("<KeyPress-Left>", lambda e: change_direction((-20, 0)))
root.bind("<KeyPress-Right>", lambda e: change_direction((20, 0)))
root.bind("<KeyPress-Up>", lambda e: change_direction((0, -20)))
root.bind("<KeyPress-Down>", lambda e: change_direction((0, 20)))

game_loop()

root.mainloop()
