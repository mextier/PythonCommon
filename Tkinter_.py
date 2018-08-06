# https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
#https://www.youtube.com/playlist?list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar


from tkinter import *

def button_clicked():
    print("thanks for clicking!")


root1 = Tk()
button1 = Button(root1, bg="red", text="Кликни меня!", command=button_clicked)
button1.pack()
root1.mainloop()
