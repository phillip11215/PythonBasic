from operator import index
from tkinter import *

win = Tk()
win.title('분식집 키오스크')


def show_meal():
    meal_button.configure(bg = 'yellow')
    beverage_button.configure(bg = 'white')
    toping_button.configure(bg = 'white')
    frame4.pack_forget()
    frame2.pack()
    frame4.pack()
    frame3.pack_forget()
    frame5.pack_forget()
def show_beverage():
    beverage_button.configure(bg='yellow')
    meal_button.configure(bg = 'white')
    toping_button.configure(bg = 'white')
    frame4.pack_forget()
    frame3.pack()
    frame4.pack()
    frame2.pack_forget()
    frame5.pack_forget()
def show_toping():
    toping_button.configure(bg='yellow')
    meal_button.configure(bg = 'white')
    beverage_button.configure(bg = 'white')
    frame4.pack_forget()
    frame5.pack()
    frame4.pack()
    frame2.pack_forget()
    frame3.pack_forget()

    
def print_order():
    temp = ''
    for meal in meal_order:
        temp = temp + meal + ' X ' + str(meal_order[meal]) + '\n'
    for beverage in beverages_order:
        temp = temp + beverage + ' X ' + str(beverages_order[beverage]) + '\n'
    for toping in toping_order:
        temp = temp + toping + ' X ' + str(toping_order[toping]) + '\n'


    order_list.delete('1.0', END)
    order_list.insert(INSERT, temp)

frame1 = Frame(win)
frame1.pack()
meal_button = Button(frame1, text='식사', bg = 'yellow', padx = 10, pady = 10, command=show_meal)
meal_button.grid(row = 0, column = 0, padx=10, pady=10)
beverage_button = Button(frame1, text = '음료', padx=10, pady=10, command=show_beverage)
beverage_button.grid (row = 0, column = 1, padx=10, pady=10)
toping_button = Button(frame1, text='토핑', padx=10, pady=10, command=show_toping)
toping_button.grid (row = 0, column = 2, padx=10, pady=10)
order_button = Button(frame1, text='주문완료', padx=10, pady=10)
order_button.grid(row = 0, column = 3, padx=10, pady=10)
order_amount = Label(frame1, text = '0원', font = 'Serif 15', padx=10, pady=10)
order_amount.grid(row=0, column = 4, padx=10, pady=10)

topings = ['치즈', '삶은 달걀', '떡 추가', '만두', '라면사리']

toping_order = {}

def add_toping(menu):
    if menu in toping_order:
        toping_order[menu] = toping_order[menu] + 1
    else:
        toping_order[menu] = 1
    print(toping_order)
    print_order()

meals = ['김밥', '라면', '떡볶이', '튀김', '쫄면']

meal_order = {}

def add_meal(menu):
    if menu in meal_order:
        meal_order[menu] = meal_order[menu] + 1
    else:
        meal_order[menu] = 1
    print(meal_order)
    print_order()
    


frame2 = Frame(win)
frame2.pack()
index = 0
for meal in meals:
        b = Button(frame2, text = '{}'.format(meal), width = 10, 
        padx = 10, pady = 10, command=lambda menu=meal : add_meal(menu))
        b.grid(row = 0, column=index, padx= 10, pady=10)
        index += 1

beverages = ['콜라', '사이다', '오투', '파워에이드', '환타']

beverages_order = {}

def add_beverages(menu):
    if menu in beverages_order:
        beverages_order[menu] = beverages_order[menu] + 1
    else:
        beverages_order[menu] = 1
    print(beverages_order)
    print_order()

frame3 = Frame(win)
index = 0
for beverage in beverages:
    b = Button(frame3, text = '{}'.format(beverage), width = 10, 
    padx = 10, pady = 10, command=lambda menu=beverage : add_beverages(menu))
    b.grid(row = 0, column=index, padx= 10, pady=10)
    index += 1


frame5 = Frame(win)
index = 0
for toping in topings:
    b = Button(frame5, text = '{}'.format(toping), width = 10, 
    padx = 10, pady = 10, command=lambda menu=toping : add_toping(menu))
    b.grid(row = 0, column=index, padx= 10, pady=10)
    index += 1

frame4 = Frame(win)
frame4.pack()
order_list = Text(frame4, height = 10)
order_list.pack()


win.mainloop()
