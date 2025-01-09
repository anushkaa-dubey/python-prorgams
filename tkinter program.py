#Used .pack() here 
#Question : To print 3 boxes of different height and width
from tkinter import *
def create_window():
    # Create and pack the red rectangle
    red_frame = Frame(root, bg="red", width=100, height=100)
    red_frame.pack(side=TOP, pady=(20, 0))
    
    # Create and pack the yellow rectangle
    yellow_frame = Frame(root, bg="yellow", width=70, height=70)
    yellow_frame.pack(side=TOP, pady=(10, 0))

    # Create and pack the blue rectangle
    blue_frame = Frame(root, bg="blue", width=40, height=40)
    blue_frame.pack(side=TOP, pady=(10, 0))

root = Tk()
root.geometry("200x300")  # Set window size

create_window()

root.mainloop()
