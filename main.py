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
root.geometry('350x450')
fecha = Label(font=('Courier', 20, 'normal'), text=f'Hoy\n{today.day}/{today.month}/{today.year}')
fecha.pack(fill=X)
Hora = Label(font=('Courier', 20, 'normal'), text=f'Hora\n{time.strftime("%H:%M:%S")}')
Hora.pack(fill=X, padx=30, pady=30)


def update_time():
    new_time = time.strftime("%H:%M:%S")
    if Hora['text'] != new_time:
        Hora['text'] = f'Hora\n{new_time}'
    root.after(1000, update_time)


update_time()
root.mainloop()
