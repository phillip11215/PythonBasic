from operator import index
from tkinter import *

win = Tk()
win.title('분식집 키오스크')


def show_meal():
    meal_button.configure(bg = 'yellow')
    beverage_button.configure(bg = 'white')
    frame4.pack_forget()
    frame2.pack()
    frame4.pack()
    frame3.pack_forget()
def show_beverage():
    beverage_button.configure(bg='yellow')
    meal_button.configure(bg = 'white')
    frame4.pack_forget()
    frame3.pack()
    frame4.pack()
    frame2.pack_forget()

    
def print_order():
    temp = ''
    for meal in meal_order:
        temp = temp + meal + ' X ' + str(meal_order[meal]) + '\n'
    for beverage in beverages_order:
        temp = temp + beverage + ' X ' + str(beverages_order[beverage]) + '\n'

    order_list.delete('1.0', END)
    order_list.insert(INSERT, temp)

frame1 = Frame(win)
frame1.pack()
meal_button = Button(frame1, text='식사', bg = 'yellow', padx = 10, pady = 10, command=show_meal)
meal_button.grid(row = 0, column = 0, padx=10, pady=10)
beverage_button = Button(frame1, text = '음료', padx=10, pady=10, command=show_beverage)
beverage_button.grid (row = 0, column = 1, padx=10, pady=10)
order_button = Button(frame1, text='주문완료', padx=10, pady=10)
order_button.grid(row = 0, column = 2, padx=10, pady=10)
order_amount = Label(frame1, text = '0원', font = 'Serif 15', padx=10, pady=10)
order_amount.grid(row=0, column = 3, padx=10, pady=10)

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
# meal1 = Button(frame2, text = '{}'.format(meals[0]), width = 10, padx = 10, pady = 10, command = lambda: add_meal(meals[0]))
# meal1.grid(row=0, column= 0, pady=10, padx=10)
# meal2 = Button(frame2, text = '{}'.format(meals[1]), width = 10, padx = 10, pady = 10, command = lambda: add_meal(meals[1]))
# meal2.grid(row=0, column= 1, pady=10, padx=10)
# meal3 = Button(frame2, text = '{}'.format(meals[2]), width = 10, padx = 10, pady = 10, command = lambda: add_meal(meals[2]))
# meal3.grid(row=0, column= 2, pady=10, padx=10)
# meal4 = Button(frame2, text = '{}'.format(meals[3]), width = 10, padx = 10, pady = 10, command = lambda: add_meal(meals[3]))
# meal4.grid(row=0, column= 3, pady=10, padx=10)
# meal5 = Button(frame2, text = '{}'.format(meals[4]), width = 10, padx = 10, pady = 10, command = lambda: add_meal(meals[4]))
# meal5.grid(row=0, column= 4, pady=10, padx=10)

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

frame4 = Frame(win)
frame4.pack()
order_list = Text(frame4, height = 10)
order_list.pack()


win.mainloop()
