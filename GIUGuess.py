#guess Game with GUI
import math
import random
import tkinter as tk

from click import command
root = tk.Tk()
#root.geometry("400x200")
lower = tk.IntVar()
higher = tk.IntVar()
def submit():
    inp1 = lower.get()
    inp2 = higher.get ()
    x = random.randint(inp1,inp2)
    print(x)
    y = round(math.log(inp2 - inp1+1,2))
    print(y)
    if y == 0:
        line_label = tk.Label(root,text= "Koi input de Lodu").grid(row = 3, column =0)
    else:
        line_label1 = tk.Label( root , text = f"The number of chances you have is: {y}").grid(row = 3, column =0)
    count  = 0
    guessnumber = tk.IntVar()
    def check():
        inp3 = guessnumber.get()
        if inp3 == x:
            congr_label = tk.Label(root , text="You guessed the number").grid(row=6)
        else:
            congra_label = tk.Label(root, text = "You guessed the wrong").grid(row = 6)
            
        guessnumber.set("")
    while count < y:
        count+=1
        text_guess_label = tk.Label(root , text="Enter the number to guess").grid(row=4,column=0)
        text_guess_Entry = tk.Entry(root , textvariable= guessnumber).grid(row=4,column=1)
        text_guess_button = tk.Button(root, text = "Check", command= check).grid(row= 5 ,column=0)
        exit_button = tk.Button(root ,  text = "Exit",command= exit).grid(row =7)
    if count > y:
        text_text = tk.Label(root, text = "You don't have chance").grid(row = 6)
    lower.set("")
    higher.set("")
text_lower_label = tk.Label(root, text= "Enter the the lower number:").grid(row = 0 , column = 0)
text_lower_entry = tk.Entry(root, textvariable= lower).grid(row = 0 , column=2)
text_higher_label = tk.Label(root, text= "Enter the the higher number:").grid(row = 1 , column =0)
text_higher_entry = tk.Entry(root, textvariable= higher).grid(row = 1 , column=2)
text_button = tk.Button(root, text = "Submit",command= submit).grid(row = 2,column= 0)
root.mainloop()
