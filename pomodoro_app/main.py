from tkinter import *
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
REPS = 0
TIMER = None
MARK = ''
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    check.config(text='')
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60
    if REPS == 8:
        count_down(long_break_Sec)
        timer_text.config(text="Break", fg=RED)
    if REPS % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    global TIMER
    global MARK
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
       TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        sessions = math.floor(REPS/2)
        for _ in range(sessions):
            MARK += "✓"
        check.config(text=MARK)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_text.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="pomodoro_app/tomato.png")
canvas.create_image(100, 112, image=bg_image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()