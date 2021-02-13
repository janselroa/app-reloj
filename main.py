import platform
import os
import datetime
import time
from tkinter import *

today = datetime.datetime.now()

root = Tk()
if platform.system() == "Windows":
    root.iconbitmap('img/reloj.ico')
else:
    root.iconphoto(True, PhotoImage(
        os.path.join(sys.path[0], "img/icono.png")))

root.title('Reloj')
root.geometry('400x400')
root.config(background='#1f2f3f')
miframe=Frame()
miframe.config(width='400', height='400', background='#ffffff')
miframe.pack(padx=60, pady=60)


fecha = Label(miframe, font=('Courier', 20, 'normal'), text=f'Hoy\n{today.day}/{today.month}/{today.year}\n', fg='#ffffff', bg='#72a922')
fecha.pack(fill=X)
Hora = Label(miframe,font=('Courier', 20, 'normal'), text=f'{time.strftime("%H:%M:%S")}\nHora local',fg='#ffffff', bg='#72a922')
Hora.pack(fill=X)


def update_time():
    new_time = time.strftime("%H:%M:%S")
    if Hora['text'] != new_time:
        Hora['text'] = f'{new_time}\nHora local'
    root.after(1000, update_time)


update_time()
root.mainloop()