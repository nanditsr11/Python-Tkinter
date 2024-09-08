import tkinter as tk
import tkinter.ttk as ttk

def on_click(a):
    print(combobox1.get())

main_window = tk.Tk()
main_window.geometry("600x300")
main_window.title("Combobox")

combobox1 = ttk.Combobox(main_window, values=[1,2,3,4,5])    #Values should be in the form of List
# combobox1['values'] = [1,2,3,4]
combobox1.bind("<<ComboboxSelected>>", on_click)
# combobox1.current(0)   #Takes the index from the list

combobox1.pack()

main_window.mainloop() 