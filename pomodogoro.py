from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg="#215E61")

title_label = Label(text= "Timer", fg="#662222", bg="#215E61", font=("Courier", 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness= 0 , bg="#662222")
image_in = PhotoImage(file="cauliflower.png")
canvas.create_image(100, 112, image= image_in)
canvas.create_text(100, 130, text="00:00", file= "white", font= ("courier", 30, "bold"))
canvas.pack()











window.mainloop()