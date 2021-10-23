import tkinter

index_i=0 
new_word=[]

def usefile(nameOfFile):
   nextWord=[]
   f=open(nameOfFile,'r')
   tmp_str=f.read()
   nextWord=tmp_str.split()
   f.close()
   return nextWord


root=tkinter.Tk()

L1=tkinter.Label(root,text="sina",fg="black",bg="white",width="20",height="5",font=("Courier", 22))
L1.pack()


def Button_Next(s):
    global index_i  
    global new_word
    L1.config(text=s)
   
    # loop takrar :)
    if index_i <len(new_word)-1:
        index_i+=1
    else:
        index_i=0
    
    L1.config(bg="cyan")

    
def Button_Else():
    L1.config(bg="yellow",text="fun")
 

b_next=tkinter.Button(root,text="L",bg="Lime",width="24",command=lambda:Button_Next(new_word[index_i])).pack(side=tkinter.LEFT)
b_else=tkinter.Button(root,text="R",bg="red",width="23" ,command=lambda:Button_Else()).pack(side=tkinter.RIGHT)

if __name__=="__main__":
    new_word = usefile("db.txt")
    root.resizable(width=False, height=False) # fix -->  window size  :)
    root.mainloop()
