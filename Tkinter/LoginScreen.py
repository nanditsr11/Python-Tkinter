import tkinter as tk
import tkinter.ttk as ttk
 

def on_click(a):
    print("Username : ", username_entry.get())
    print("Password : ", password_entry.get())
    print("Agr above 18 years?", var.get())

def combobox_ret(a):
        print(combobox1.get())

main_window = tk.Tk()
main_window.geometry("600x300")
main_window.title("Login Page")

page_label = tk.Label(main_window, text="Login Page", padx=67, bg='green')
page_label.grid(row=0, column=0, columnspan=2)

username_label = tk.Label(main_window, text="Username : ")
password_label = tk.Label(main_window, text="Password : ")
username_label.grid(row=3, column=0)
password_label.grid(row=4, column=0)

username_entry = tk.Entry(main_window)
password_entry = tk.Entry(main_window)
username_entry.grid(row=3, column=1)
password_entry.grid(row=4, column=1)

age_label = tk.Label(main_window, text="Are you above 18 years old ?")
age_label.grid(row=5, column=0)

var = tk.IntVar()

age_button1 = tk.Radiobutton(main_window, text="Yes", variable= var, value=1)
age_button1.grid(row=5, column=1)
age_button2 = tk.Radiobutton(main_window, text="No", variable= var, value=2)
age_button2.grid(row=5, column=2)

combobox_label = tk.Label(main_window, text="Gender")
combobox_label.grid(row=6, column=0)
combobox1 = ttk.Combobox(main_window, values=["Male", "Female", "Rather Not Say"])
combobox1.bind("<<ComboboxSelected>>", combobox_ret)
combobox1.grid(row=6, column=1)

submit_button = tk.Button(main_window, text= "Submit", bg= 'green', fg='White', font="comicsansms 10 bold", command=on_click)
submit_button.grid(row=7, column=0)

main_window.mainloop()

