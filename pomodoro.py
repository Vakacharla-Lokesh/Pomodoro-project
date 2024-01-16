from tkinter import *
import math
#CONSTANT
PINK = "#e2979c"
RED = "e#3705b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#TIMER RESET 
def reset_timer():
    global timer
    global reps
    reps = 0
    my_window.after_cancel(timer)
    timer_label.config(text="Timer")
    my_canvas.itemconfig(timer_text, text = "00:00")
    check_label.config(text="")

#TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        # time_sec = LONG_BREAK_MIN
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    elif reps %2 == 1:
        # time_sec = WORK_MIN
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps %2 == 0:
        # time_sec == SHORT_BREAK_MIN
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)

    
#COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    my_canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = my_window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        numb_work_sess = math.floor(reps/2)
        for i in range(numb_work_sess):
            mark += "✔️"
        check_label.config(text=mark)
        
#UI SETUP
my_window = Tk()
my_window.title("POMODORO")
my_window.config(padx=100, pady=50, bg=YELLOW)

my_canvas = Canvas(width=300, height=170, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro project\\tomato.png")
my_canvas.create_image(150, 85, image = tomato_img)
timer_text = my_canvas.create_text(150, 105, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
my_canvas.grid(row=1, column=1)

#LABELS
timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

#BUTTONS
start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


my_window.mainloop()