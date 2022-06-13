from tkinter import *
tk = Tk()
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1200, height=600, highlightthickness=0, background='#31363b')
canvas.pack()

default = {'width': 100, 'height': 100}
canvas0 = Canvas(tk, width=1200, height=50)
canvas0.place(x=600, y=25, anchor=CENTER)
canvas0.create_rectangle(0, 0, 1200, 50, fill="white")
canvas0.create_text(600, 25, font="Times 18 bold", text='МАССИВ', anchor=CENTER)

canvas01 = Canvas(tk, width=1200, height=50)
canvas01.place(x=600, y=310, anchor=CENTER)
canvas01.create_rectangle(0, 0, 1200, 50, fill="white")
canvas01.create_text(600, 25, font="Times 18 bold", text='СТЕК', anchor=CENTER)

canvas1 = Canvas(tk, **default)
canvas1.place(x=200, y=100, anchor=CENTER)
canvas1.create_rectangle(0, 0, 100, 100, fill="#fff0cf")
canvas1.create_text(50, 50, font="Times 20 bold", text='5')

canvas2 = Canvas(tk, **default)
canvas2.place(x=300, y=100, anchor=CENTER)
canvas2.create_rectangle(0, 0, 100, 100, fill="#b3c3ff")
canvas2.create_text(50, 50, font="Times 20 bold", text='4')

canvas3 = Canvas(tk, **default)
canvas3.place(x=400, y=100, anchor=CENTER)
canvas3.create_rectangle(0, 0, 100, 100, fill="#ffb3b3")
canvas3.create_text(50, 50, font="Times 20 bold", text='7')


canvas4 = Canvas(tk, **default)
canvas4.place(x=500, y=100, anchor=CENTER)
canvas4.create_rectangle(0, 0, 100, 100, fill="#cfffb3")
canvas4.create_text(50, 50, font="Times 20 bold", text='9')

canvas5 = Canvas(tk, **default)
canvas5.place(x=600, y=100, anchor=CENTER)
canvas5.create_rectangle(0, 0, 100, 100, fill="#f2ffb3")
canvas5.create_text(50, 50, font="Times 20 bold", text='2')

canvas6 = Canvas(tk, **default)
canvas6.place(x=700, y=100, anchor=CENTER)
canvas6.create_rectangle(0, 0, 100, 100, fill="#ffd3b3")
canvas6.create_text(50, 50, font="Times 20 bold", text='4')

canvas7 = Canvas(tk, **default)
canvas7.place(x=800, y=100, anchor=CENTER)
canvas7.create_rectangle(0, 0, 100, 100, fill="#b3ffd7")
canvas7.create_text(50, 50, font="Times 20 bold", text='4')

canvas8 = Canvas(tk, **default)
canvas8.place(x=900, y=100, anchor=CENTER)
canvas8.create_rectangle(0, 0, 100, 100, fill="#cfb3ff")
canvas8.create_text(50, 50, font="Times 20 bold", text='5')

canvas9 = Canvas(tk, **default)
canvas9.place(x=1000, y=100, anchor=CENTER)
canvas9.create_rectangle(0, 0, 100, 100, fill="#ffb3df")
canvas9.create_text(50, 50, font="Times 20 bold", text='6')

coords = dict()


def drag(event):
    global coords
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    mouse_x = round(mouse_x / 100) * 100
    mouse_y = round(mouse_y / 100) * 100
    if (mouse_x, mouse_y) not in coords.values():
        event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)
        coords[event.widget] = (mouse_x, mouse_y)
    elif canvas not in coords:
        coords[canvas] = (mouse_x, mouse_y)


canvas1.bind("<B1-Motion>", drag)
canvas2.bind("<B1-Motion>", drag)
canvas3.bind("<B1-Motion>", drag)
canvas4.bind("<B1-Motion>", drag)
canvas5.bind("<B1-Motion>", drag)
canvas6.bind("<B1-Motion>", drag)
canvas7.bind("<B1-Motion>", drag)
canvas8.bind("<B1-Motion>", drag)
canvas9.bind("<B1-Motion>", drag)

tk.mainloop()


