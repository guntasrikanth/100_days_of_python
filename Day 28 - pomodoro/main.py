import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    windows.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 10
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label1.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(15)
    elif reps % 2 == 0:
        label1.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(5)
    else:
        label1.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        count_down(10)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_count = math.floor(count / 60)
    second_count = count % 60
    if second_count < 10:
        second_count = f"0{second_count}"
    canvas.itemconfig(timer_text, text=f'{min_count}:{second_count}')
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count-1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        label2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

windows = tkinter.Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

label1 = tkinter.Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label1.grid(row=0, column=1)

start_button = tkinter.Button(text='Start', command=start, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

label2 = tkinter.Label(text="",fg=GREEN, bg=YELLOW,)
label2.grid(row=3, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

windows.mainloop()

