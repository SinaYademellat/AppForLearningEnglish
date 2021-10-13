#one label(L1) && two button (b_?) 
#lest go :)

import tkinter
import os

#global value :)

index_i=0 
new_word=["Next","ALI","fares","javad","reza","1231312"]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Button_Next(s):
    global index_i  
    global new_word
    L1.config(text=s)
   
    # loop takrar :)
    if index_i <len(new_word)-1:
        index_i+=1
    else:
        index_i=0
    

def Button_Else():
    L1.config(bg="yellow",text="fun")

 
root=tkinter.Tk()

L1=tkinter.Label(root,text="sina",fg="black",bg="cyan",width="20",height="5",font=("Courier", 22))
L1.pack()

b_next=tkinter.Button(root,text="Next",bg="Lime",width="24",command=lambda:Button_Next(new_word[index_i])).pack(side=tkinter.LEFT)
b_else=tkinter.Button(root,text="Else",bg="red",width="23",command=lambda:Button_Else()).pack(side=tkinter.RIGHT)

root.mainloop()
