from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 55
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    finally:
        global reps
        reps = 0
        title_label.config(fg=GREEN, text="TIMER")
        check_label.config(text="")
        canvas.itemconfig(timer_text, text="00:00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    if reps % 8 == 0:
        title_label.config(fg=RED, text="Break")
        count_down((float(long_break_entry.get()) * 60))
    elif reps % 2 == 0:
        messagebox.showinfo("Break", "Take a break")
        title_label.config(fg=PINK, text="Break")
        count_down((float(break_entry.get()) * 60))
    else:
        title_label.config(fg=GREEN, text="Work")
        count_down((float(work_entry.get()) * 60))
    # window.lift()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if math.floor(count / 60) >= 60:
        calculate_time(count)
    else:
        count_min = math.floor(count / 60)
        count_sec = math.floor(count % 60)
        if count_min < 10:
            count_min = f"0{count_min}"
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif reps == 15:
        messagebox.showinfo("End of Day", "That's enough work for today!")
    elif reps == 8:
        messagebox.showinfo("Long Break", "Take a walk or grab a bite!")
        check_it()
    else:
        check_it()


def calculate_time(count):
    count_hour = math.floor((count / 60) / 60)
    count_min = math.floor((count / 60) % 60)
    count_sec = math.floor((count % 60) % 60)
    # count_sec = 0
    if count_hour < 10:
        count_hour = f"0{count_hour}"
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_hour}:{count_min}:{count_sec}")


def check_it():
    start_timer()
    work_sessions = math.floor(reps / 2)
    marks = "".join("✔" for _ in range(work_sessions))
    check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=YELLOW, width=600)

title_label = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, text="TIMER", bg=YELLOW)
title_label.grid(column=2, row=1, rowspan=2)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=tomato_img)
timer_text = canvas.create_text(150, 132, text="00:00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=3)

check_label = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=5)

work_label = Label(font=(FONT_NAME, 10, "bold"), fg="black", bg=YELLOW, text="Work")
work_label.grid(column=0, row=0, sticky="w")

break_label = Label(font=(FONT_NAME, 10, "bold"), fg="black", bg=YELLOW, text="Short Break")
break_label.grid(column=0, row=1, sticky="w")

long_break_label = Label(font=(FONT_NAME, 10, "bold"), fg="black", bg=YELLOW, text="Long Break")
long_break_label.grid(column=0, row=2, sticky="w")

# Entry
work_entry = Entry(width=5)
work_entry.insert(END, WORK_MIN)
work_entry.grid(column=1, row=0)

break_entry = Entry(width=5)
break_entry.insert(END, SHORT_BREAK_MIN)
break_entry.grid(column=1, row=1)

long_break_entry = Entry(width=5)
long_break_entry.insert(END, LONG_BREAK_MIN)
long_break_entry.grid(column=1, row=2)


# buttons
def start_clicked():
    reset_timer()
    start_timer()


start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), width=5, command=start_clicked)
start_button.grid(column=1, row=4)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), width=5, command=reset_timer)
reset_button.grid(column=3, row=4)

empty_label = Label(width=10, bg=YELLOW)
empty_label.grid(column=5, row=5)


window.mainloop()
