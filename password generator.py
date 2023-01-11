import random as r 
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Password Generator")


lbl1 = Label(window, text = "To get a random strong password click below" , font=("Arial", 20))
lbl1.grid(column=0, row=0)
lbl2 = Label(window , text="" , font=("Arial", 20))
lbl2.grid(column=0, row=2)
window.geometry('550x200')
txt = scrolledtext.ScrolledText(window,width=15,height=5)
txt.grid(column=0 , row=2)
# txt = Text(window , height=5 , width=10)
# txt.grid(column=0 , row=2)

def btnClicked():
    # letters = "qwertyuiopasdfghjklzxcbnm"
    # numbers = "1234567890"
    # speChars = "!@#$%^&*()_+{\}|:<>?\",./;'[]"
    # LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    chars = ["qwertyuiopasdfghjklzxcbnm","1234567890","!@#$%^&*()_+{\}|:<>?\",./;'[]","QWERTYUIOPASDFGHJKLZXCVBNM"]

    num = 8 
    count = 0 
    pswrd = ""

    while num > count :
        count = count +1
        chr = str(iter(chars))
        pswrd = chr[r.randrange(0,len(chr))] + pswrd 

    txt.insert(INSERT,pswrd + " \n")

def btnClear():
    txt.delete(1.0,END)

btn = Button(window , text = "Generate Passowrd" , bg= "white" , fg= "black" , command=btnClicked)
btn.grid(column=0, row=1)

btn2 = Button(window , text = "Clear" , bg= "white" , fg= "black" , command=btnClear).grid(column=0,row=3)
window.mainloop()
