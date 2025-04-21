import os
import pickle
import tkinter as tk
from Lernkartei_data_structure import Lernkartei_word





class AddNewWord_app():
    def __init__(self) -> None:
        # self.counter_nuber_is = 0
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
        # self.root_of_AddNewWord_app.bind('<Return>', self.GG)

    def show_len_newWordList_notsave(self):
        self.label_counter["text"] = f'{len(self.newWordList)}'

    def set_counter(self,possitain_XY:tuple =(0,89)):
        self.label_counter = tk.Label(self.root_of_AddNewWord_app,
                                text="0",
                                width=5,
                                anchor="center",
                                bg="#1DCD9F",
                                font=("Helvetica", 10),
                                )
        self.label_counter.place(x = possitain_XY[0],y=possitain_XY[1])


    def clean_Entry(self):
        self.e1_text.delete(0, 'end')
        self.e2_collocations.delete(0, 'end')

    def Gui_to_local_list_MyDatastructure(self)->None:
        tmp_Word = Lernkartei_word(
            Txt=self.e1_text.get() ,
            Collocations= self.e2_collocations.get(),
            Status=1 )
        self.newWordList.append(tmp_Word)
        self.show_len_newWordList_notsave()
        self.clean_Entry()

    def save_newWordToPkl(self):
        if(len(self.newWordList)==0): # مثل این که اول کامیت میکنیم بعد پوش میکنیم تو گیت :)
            print('first push buttom "ok"')
            return
        ds_path = '../Data Base'
        mypath = os.path.join(ds_path, 'Box_1.pkl')
        with open(mypath, 'rb') as inp:
            tmp_list_is = pickle.load(inp)

        for i in self.newWordList:
            tmp_list_is.append(i)

        print('Len Box1: ',len(tmp_list_is))
        with open(mypath, 'wb') as outp:
                pickle.dump(tmp_list_is, outp, pickle.HIGHEST_PROTOCOL)
        self.newWordList = []
        self.show_len_newWordList_notsave()
        print('save it')
  
  
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

        self.e1_text = tk.Entry(self.root_of_AddNewWord_app,font=("Helvetica", 15))
        self.e2_collocations = tk.Entry(self.root_of_AddNewWord_app,font=("Helvetica", 15))
        self.e1_text.place(x=120, y = 5 + 14)
        self.e2_collocations.place(x=120, y = 40 + 14)

        # ! ============================================ 
        self.set_counter()

        b1 = tk.Button(self.root_of_AddNewWord_app, width=5, text='ok',font=("Helvetica", 8) , command=self.Gui_to_local_list_MyDatastructure)
        b1.place(x=50,y=88)

        b2_saveToPklFile = tk.Button(self.root_of_AddNewWord_app,width=5,text='Save!',font=("Helvetica", 8) ,  command=self.save_newWordToPkl)
        b2_saveToPklFile.place(x=180 , y=88)
        


if (__name__=='__main__'):
    AddNewWord_app()
    