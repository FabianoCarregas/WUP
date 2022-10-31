import tkinter as tk
from functools import partial

import alura

window = tk.Tk()
window.title('WUG')
window.geometry("390x165")

def call_env():
    env = option.get()
    if env == "Alura":
        log_in.__call__()

    if env == "Alura-Start":
        print("Alura-Startttttttt")

    if env == "Alura-Lingua":
        print("Alura-Linguaaaaaa")

    if env == "MusicDot":
        print("MusicDottttttt")

    if env == "Alura-Latam":
        print("Alura-Latammmmm")

    if env == "BootCamp":
        print("BootCamppppp")

    if env == "TechPos":
        print("TechPosssssss")

    if env == "Alura-Online":
        print("Alura-Onlineeeeee")

env_options = ["Alura",
               "Alura-Start",
               "Alura-Lingua",
               "MusicDot",
               "Alura-Latam",
               "BootCamp",
               "TechPos",
               "Alura-Online"]

option = tk.StringVar(window)
option.set("Alura")

var_email = tk.StringVar()
var_password = tk.StringVar()
var_url = tk.StringVar()

tk.Label(window, text='Warm up Gnarus').grid(column=1, row=0)

tk.Label(window, text='-url-').grid(column=0, row=1)
url = tk.Entry(window, textvariable=var_url, width=35).grid(column=1, row=1)

tk.Label(window, text='Email').grid(column=0, row=2)
email = tk.Entry(window, textvariable=var_email, width=35).grid(column=1, row=2)

tk.Label(window, text='Key').grid(column=0, row=3)
password = tk.Entry(window, textvariable=var_password, show='*', width=35).grid(column=1, row=3)
tk.Checkbutton(window, text='save').grid(column=2, row=3)

drop = tk.OptionMenu(window, option, *env_options)
drop.pack
drop.grid(column=1, row=4)

log_in = partial(alura.log_in, var_email, var_password, var_url)

tk.Button(window, text='$-START-$', command=call_env).grid(column=1, row=5)

window.mainloop()