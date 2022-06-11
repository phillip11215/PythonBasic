from tkinter import *
from tkinter import messagebox
import mazes

def draw_map():
    for y in range(7):
        for x in range(11):
            if maze[y][x] == 0:
                canvas.create_rectangle(x*width, y*height, x*width + width, y*height + height , fill='gray', outline='white')
            elif maze[y][x] == 2:
                canvas.create_rectangle(x*width, y*height, x*width + width, y*height + height , fill='orange', outline='white')

def draw_player():
    global player
    player = canvas.create_image(player_x * width + width/2, player_y*height+height/2, image = img, tag = 'CAT')


win = Tk()
win.title('미로')

canvas = Canvas(width = 880, height = 560, bg = 'white')
canvas.pack()





width = 80
height = 80
img = PhotoImage(file='작은고양이.png')

level = 1

maze = mazes.mazes[level-1]
player_x = 1
player_y = 1
player = None

draw_map()
draw_player()

def draw_map():
    for y in range(7):
        for x in range(11):
            if maze[y][x] == 0:
                canvas.create_rectangle(x*width, y*height, x*width + width, y*height + height , fill='gray', outline='white')
            elif maze[y][x] == 2:
                canvas.create_rectangle(x*width, y*height, x*width + width, y*height + height , fill='orange', outline='white')

def key_down(e):
    global player_x, player_y, level, maze
    key = e.keysym
    if key == 'Up' and maze[player_y-1][player_x] != 0:
        canvas.move(player, 0, -height)
        player_y -= 1
    elif key == 'Down' and maze[player_y+1][player_x] != 0:
        canvas.move(player, 0, height)
        player_y += 1
    elif key == 'Right' and maze[player_y][player_x+1] != 0:
        canvas.move(player, width, 0)
        player_x += 1
    elif key == 'Left' and maze[player_y][player_x-1] != 0:
        canvas.move(player, -width, 0)
        player_x -= 1

    if maze[player_y][player_x] == 2:
        messagebox.showinfo('결과', '출구 도착!')
        level += 1
        maze = mazes.mazes[level-1]
        canvas.delete('all')
        player_y = 1
        player_x = 1
        draw_map()
        draw_player()

win.bind('<KeyPress>', key_down)
win.mainloop()
