from tkinter import *
import janken as jk
root = Tk()
root.title("janken")

label = Label(text="choose player1 hand")
label.pack()

r_button = Button(
    text="rock",
    width=10,
    command=lambda:jk.janken(0)
)
p_button = Button(
    text="paper",
    width=10,
    command=lambda:jk.janken(1)
)
s_button = Button(
    text="scissors",
    width=10,
    command=lambda:jk.janken(2)
)
r_button.pack()
p_button.pack()
s_button.pack()

label = Label(text="choose player2 hand")
label.pack()

rII_button = Button(
    text="rock",
    width=10,
    command=lambda:jk.jankenII(0)
)
pII_button = Button(
    text="paper",
    width=10,
    command=lambda:jk.jankenII(1)
)
sII_button = Button(
    text="scissors",
    width=10,
    command=lambda:jk.jankenII(2)
)
rII_button.pack()
pII_button.pack()
sII_button.pack()

root.mainloop()
