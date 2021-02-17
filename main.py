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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    count_down(5 * 60)

def count_down(count):

    count_min = math.floor(count / 60 )
    count_sec = count % 60
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=tomato_img)
timer_count= canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row=1)

#label title
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column= 1, row=0)

#start button
start_button = Button(text="Start",  width= 8, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column= 0, row=2)

#rest button
reset_button = Button(text="Reset", width= 8,  highlightbackground=YELLOW)
reset_button.grid(column= 2, row=2)

#check mark
check_mark = Label(text= "✔", fg= GREEN, bg=YELLOW)
check_mark.grid(column= 1, row =3)


window.mainloop()

