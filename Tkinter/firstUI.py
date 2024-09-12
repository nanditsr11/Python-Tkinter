import tkinter as tk

main_window = tk.Tk()  #This line creates a main window which acts as a base to create more components and a full fledged app.
main_window.title("My Python Window")
main_window.geometry("800x600")  #helps in setting the default size of the window.
main_window.minsize(200, 100)  #defines the minimum size of the window
main_window.maxsize(1000, 600)  #defines the maximum size of the window

main_window.mainloop()   #this function does the job of adding all the components to the main window and also keeps a track of all the events that occur
                          # on the GUI, if you dont use this function then the output wont display

