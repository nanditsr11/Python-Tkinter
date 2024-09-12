import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")

label = tk.Label(main_window, text= "Python", bg='green', fg='White')
label.place(x=200, y=30)

main_window.mainloop()

