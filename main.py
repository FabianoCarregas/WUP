import tkinter as tk
from functools import partial
from tkinter import messagebox
import alura
import start
import lingua
import musicDot
import latam
import bootcamp
import techpos
import online

white = "white"
grey = "#3e3e42"
dark = "#252526"
blue = "#007acc"


def call_env():
    env = option.get()
    if env == "Alura":
        log_alura.__call__()

    if env == "Alura-Start":
        log_start.__call__()

    if env == "Alura-Lingua":
        log_lingua.__call__()

    if env == "MusicDot":
        log_musicDot.__call__()

    if env == "Alura-Latam":
        log_latam.__call__()

    if env == "BootCamp":
        log_bootcamp.__call__()

    if env == "TechPos":
        log_techpos.__call__()

    if env == "Alura-Online":
        log_online.__call__()


env_options = ["Alura",
               "Alura-Start",
               "Alura-Lingua",
               "MusicDot",
               "Alura-Latam",
               "BootCamp",
               "TechPos",
               "Alura-Online"]

window = tk.Tk()
window.title('WUG')
window.geometry("390x295")
window.resizable(width=False, height=False)

frame_up = tk.Frame(window, width=390, height=40, bg=dark)
frame_up.grid(row=0, column=0)

frame_down = tk.Frame(window, width=390, height=300, bg=dark)
frame_down.grid(row=1, column=0)

option = tk.StringVar(window)
option.set("Alura")

var_email = tk.StringVar()
var_password = tk.StringVar()
var_url = tk.StringVar()

heading = tk.Label(frame_up, text='Warm up Gnarus', bg=dark, fg=white, font=('Poppins 16'))
heading.place(x=100, y=5)

line = tk.Label(frame_up, text='', bg=blue, width=80, height=1)
line.place(x=0, y=33)

url_label = tk.Label(frame_down, text='url *', bg=dark, fg=white, font=('Poppins 10'))
url_label.place(x=20, y=10)
url = tk.Entry(frame_down, textvariable=var_url, width=43, bg=grey, fg=white)
url.place(x=20, y=30)

email_label = tk.Label(frame_down, text='email *', bg=dark, fg=white, font=('Poppins 10'))
email_label.place(x=20, y=65)
email = email = tk.Entry(frame_down, textvariable=var_email, width=43, bg=grey, fg=white)
email.place(x=20, y=85)

pass_label = tk.Label(frame_down, text='password *', bg=dark, fg=white, font=('Poppins 10'))
pass_label.place(x=20, y=119)
password = tk.Entry(frame_down, textvariable=var_password, show='*', width=35, bg=grey, fg=white)
password.place(x=20, y=139)

save = tk.Checkbutton(frame_down, text='save', bg=dark, fg=white, activebackground=grey, font=('Poppins 10'))
save.place(x=310, y=139)

drop = tk.OptionMenu(frame_down, option, *env_options)
drop.config(bg=grey, fg=white)
drop.place(x=195, y=195)

warm = tk.Button(frame_down, text='START', command=call_env)
warm.config(bg=blue, fg=white)
warm.place(x=90, y=196)

log_alura = partial(alura.run, var_email, var_password, var_url)
log_start = partial(start.run, var_email, var_password, var_url)
log_lingua = partial(lingua.run, var_email, var_password, var_url)
log_musicDot = partial(musicDot.run, var_email, var_password, var_url)
log_latam = partial(latam.run, var_email, var_password, var_url)
log_bootcamp = partial(bootcamp.run, var_email, var_password, var_url)
log_techpos = partial(techpos.run, var_email, var_password, var_url)
log_online = partial(online.run, var_email, var_password, var_url)

window.mainloop()
