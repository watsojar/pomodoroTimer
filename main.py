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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="Timer")
    checkLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global reps
    reps += 1
    workSecs = WORK_MIN * 60
    shortBreakSecs = SHORT_BREAK_MIN * 60
    longBreakSecs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countDown(longBreakSecs)
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(shortBreakSecs)
        timerLabel.config(text="Break", fg=PINK)
    else:
        countDown(workSecs)
        timerLabel.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countDown(count):
    countMin = math.floor(count / 60)
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks = ""
        workSessions = math.floor(reps / 2)
        for _ in range(0, workSessions):
            marks += "✓"
        checkLabel.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Study Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# buttons
startBtn = Button(text="Start", command=startTimer)
startBtn.grid(column=0, row=2)

resetBtn = Button(text="Reset", command=resetTimer)
resetBtn.grid(column=2, row=2)

# labels
timerLabel = Label(text="Timer", fg=GREEN, bg=YELLOW)
timerLabel.config(font=(FONT_NAME, 100, "bold"))
timerLabel.grid(column=1, row=0)

checkLabel = Label(text="", fg=GREEN, bg=YELLOW)
checkLabel.grid(column=1, row=3)

window.mainloop()
