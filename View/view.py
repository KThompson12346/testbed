from tkinter import *

class View:
    window = Tk()
    window.title('Algorithm Testbed')
    title_frame = Frame(window) # a frame used to display the title of the program
    button_frame = Frame(window)
    canvas_frame = Frame(window)

    canvas = Canvas(canvas_frame, width=600, height=700, background='white')

    title_label = Label(title_frame, text='Searching & Sorting Algorithm Testbed', font='Helvetica 20 bold')

    init_button = Button(button_frame, text='     Initialise     ', width=15, pady=10)
    start_button = Button(button_frame, text='     Start     ', width=15, pady=10)
    pause_button = Button(button_frame, text='     Pause     ', width=15, pady=10)
    step_button = Button(button_frame, text='     Step     ', width=15, pady=10)
    clear_button = Button(button_frame, text='     Clear     ', width=15, pady=10)

    # putting the label onto the title_frame
    title_label.grid(rowspan=2, column=0)
    # putting buttons onto the button_frame
    init_button.grid(rowspan=1, column=0, pady=10, padx=5)
    start_button.grid(rowspan=1, column=0, pady=10, padx=5)
    pause_button.grid(row=2, column=0, pady=10, padx=5)
    step_button.grid(row=3, column=0, pady=10, padx=5)
    clear_button.grid(row=4, column=0, pady=10, padx=5)
    # putting canvas onto canvas_frame
    canvas.grid(row=0, column=0)

    # putting frames on the window
    title_frame.grid(row=0, columnspan=2)
    button_frame.grid(row=1, column=0)
    canvas_frame.grid(row=1, column=1)

    # window.mainloop()
