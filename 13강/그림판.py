from tkinter import *

win = Tk()
win.title('그림판')
win.geometry('600x600')

label = Label(win, text='그림판', font=('Serif', 30, 'bold'))
label.pack(pady = 30)

canvas = Canvas(win, width = 600, height = 600, bg='white', relief = 'ridge', bd = 5)
canvas.pack()

pen_color = 'black'
pen_size = 5
def paint(event):
    x0 = event.x - 1
    x1 = event.x + 1
    y0 = event.y - 1
    y1 = event.y + 1
    canvas.create_oval(x0, y0, x1, y1, fill = pen_color, outline = pen_color, width = pen_size)
canvas.bind('<B1-Motion>', paint)

def change(color):
    global pen_color
    pen_color = color

red_button = Button(win, text='빨강', width = 5, bg = 'red', command=lambda: change('red'))
red_button.place(x=0, y=0)
red_button = Button(win, text='파랑', width = 5, bg = 'blue', command=lambda: change('blue'))
red_button.place(x=50, y=0)
red_button = Button(win, text='노랑', width = 5, bg = 'yellow', command=lambda: change('yellow'))
red_button.place(x=100, y=0)
red_button = Button(win, text='초록', width = 5, bg = 'green', command=lambda: change('green'))
red_button.place(x=150, y=0)
red_button = Button(win, text='보랑', width = 5, bg = 'purple', command=lambda: change('purple'))
red_button.place(x=200, y=0)

def sizedown():
    global pen_size
    pen_size -= 1
    if pen_size <0:
        pen_size = 1
    size_label['text'] = '{}'.format(pen_size)
def sizeup():
    global pen_size
    pen_size += 1
    size_label['text'] = '{}'.format(pen_size)


thin_button = Button(win, text='얇게', width = 5, bg = 'gray', command=sizedown)
thin_button.place(x=480, y=0)
bold_button = Button(win, text='굵게', width = 5, bg = 'gray', command=sizeup)
bold_button.place(x=550, y=0)

size_label = Label(win, text = '{}'.format(pen_size), font = ('Serif', 10, 'bold'))
size_label.place(x = 530, y = 0)

clear_button = Button(win, text = '지우기', width = 5, bg = 'gray', fg = 'white',
                            command = lambda: canvas.delete('all'))
clear_button.place(x = 0, y = 50)

win.mainloop()
