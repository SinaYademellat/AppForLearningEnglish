import tkinter as tk
from Lernkartei_data_structure import Lernkartei_word

class AddNewWord_app():
    def __init__(self) -> None:
        self.counter_nuber_is = 0
        self.newWordList = []
        self.root_of_AddNewWord_app = tk.Tk()
        # . . . . . . . . . . . . . . . . . . . . . .
        self.set_Gui()
        self.root_of_AddNewWord_app.mainloop()

    def WindoSizeAndFixeIt(self,window_width:int=500,window_height:int=300):
        screen_width  = self.root_of_AddNewWord_app.winfo_screenwidth()
        screen_height = self.root_of_AddNewWord_app.winfo_screenheight()    
        # پیداکردن پدینگ مورد دلخواه
        x_offset = (screen_width - window_width)   // 2
        y_offset = (screen_height - window_height) // 2
        # -------------------
        self.root_of_AddNewWord_app.geometry(f"{window_width}x{window_height}+{ x_offset }+{y_offset}")
        self.root_of_AddNewWord_app.resizable(False,False)
        # ----------


    def GG(self,event):
        self.counter_nuber_is+=1
        self.label_counter["text"] = f'{self.counter_nuber_is}'


    def set_counter(self,possitain_XY:tuple =(0,89)):
        self.label_counter = tk.Label(self.root_of_AddNewWord_app,
                                text="0",
                                width=5,
                                anchor="center",
                                bg="#1DCD9F",
                                font=("Helvetica", 10),
                                )
        self.label_counter.place(x = possitain_XY[0],y=possitain_XY[1])

        self.root_of_AddNewWord_app.bind('<Return>', self.GG)


    def FF(self):
        print('s')
   
    def set_Gui(self):
        # -----------------
        backgroundColor_root = '#FF9A9A'
        # -----------------
        self.root_of_AddNewWord_app.title('New Word')
        self.WindoSizeAndFixeIt(window_width = 370 ,window_height = 120)
        self.root_of_AddNewWord_app.config(bg = backgroundColor_root)
        # print( self.x_offset )
        # ! ============================================ 
        
        l1 = tk.Label(self.root_of_AddNewWord_app, width=10,text="text",font=("Helvetica", 15))
        l2 = tk.Label(self.root_of_AddNewWord_app, text="collocations",width=10,font=("Helvetica", 15))
        l1.place(x =0 ,y = 5 + 14)
        l2.place(x =0 ,y = 40 + 14)

        e1 = tk.Entry(self.root_of_AddNewWord_app,font=("Helvetica", 15))
        e2 = tk.Entry(self.root_of_AddNewWord_app,font=("Helvetica", 15))
        e1.place(x=120, y = 5 + 14)
        e2.place(x=120, y = 40 + 14)

        # ! ============================================ 
        self.set_counter()


        b1 = tk.Button(self.root_of_AddNewWord_app, width=5, text='ok',font=("Helvetica", 8) , command=self.FF)
        b1.place(x=50,y=88)




if (__name__=='__main__'):
    AddNewWord_app()
    print()