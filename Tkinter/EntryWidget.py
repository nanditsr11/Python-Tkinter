import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")
main_window.title("Entry Widget")

entry = tk.Entry(main_window, bg='White', fg='Black', justify='right',  font="comicsansms 10 italic", bd=2)
entry.pack()

main_window.mainloop()