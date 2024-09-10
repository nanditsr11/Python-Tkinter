import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")

Label1 = tk.Label(main_window, text="Hello Python 1", bg='green', fg='Black')
Label1.pack(side=tk.BOTTOM)

Label2 = tk.Label(main_window, text="Hello Python 2", bg='green', fg='Black')
Label2.pack(fill= tk.X)

Label3 = tk.Label(main_window, text="Hello Python 3", bg='green', fg='Black')
Label3.pack(side=tk.LEFT, fill= tk.Y)

Label4 = tk.Label(main_window, text="Hello Python 4", bg='Blue', fg='White')
Label4.pack(pady=10)

Label5 = tk.Label(main_window, text="Hello Python 5", bg='Blue', fg='White')
Label5.pack(pady=10)

Label6 = tk.Label(main_window, text="Hello Python 6", bg='Blue', fg='White')
Label6.pack(padx=10, side=tk.LEFT)

Label7 = tk.Label(main_window, text="Hello Python 7", bg='Blue', fg='White')
Label7.pack(padx=10, side=tk.LEFT)

Label8 = tk.Label(main_window, text="Hello Python 8", bg='Maroon', fg='White')
Label8.pack(pady=10, ipadx=10)

Label9 = tk.Label(main_window, text="Hello Python 9", bg='Blue', fg='White')
Label9.pack(ipady=10)

main_window.mainloop() 