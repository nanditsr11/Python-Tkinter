import tkinter as tk

def click_now():
    print("Radio Button Clicked : ", var.get())

main_window = tk.Tk()
main_window.title("Radio Button Demo")
main_window.geometry("500x300")

var = tk.IntVar()

radio1 = tk.Radiobutton(main_window, text= 'Red', command=click_now, variable=var, value=1, height=2, width=2)
radio1.pack()

radio2 = tk.Radiobutton(main_window, text='Green', command=click_now, variable=var, value=2, height=2, width=2)
radio2.pack()

radio3 = tk.Radiobutton(main_window, text="Blue", command=click_now, variable=var, value=3, height=2, width=2)
radio3.pack()

main_window.mainloop()  