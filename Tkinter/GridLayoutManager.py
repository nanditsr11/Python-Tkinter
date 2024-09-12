import tkinter as tk

main_window = tk.Tk()
main_window.geometry("500x300")

label1 = tk.Label(main_window, text="Hello Python 1", bg='green', fg='White')
label1.grid(row=0, column=0, padx= 10)

label2 = tk.Label(main_window, text="Hello Python 2", bg='green', fg='White')
label2.grid(row=0, column=1, padx= 10)

label3 = tk.Label(main_window, text="Hello Python 3", bg='green', fg='White')
label3.grid(row=0, column=2, padx= 10)

label4 = tk.Label(main_window, text="Hello Python 4", bg='green', fg='White')
label4.grid(row=1, column=0, padx= 10, pady= 10, columnspan=2)

label5 = tk.Label(main_window, text="Hello Python 5", bg='green', fg='White')
label5.grid(row=1, column=2, padx= 10, pady= 10, rowspan=2)

label6 = tk.Label(main_window, text="Hello Python 6", bg='green', fg='White')
label6.grid(row=2, column=0, padx= 10, pady= 10)

main_window.mainloop()