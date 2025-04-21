import os
import pickle

import tkinter as tk
from Lernkartei_data_structure import Lernkartei_word


class AppForLearningEnglish():
        def __init__(self , title_for_root:str="sina yademellat" , All_list_fo_word:list[list[Lernkartei_word]] = None):
            '''
                title_for_root : اسم آن گروه از لغات باشد بهتر است 
            '''
            
            self.root = tk.Tk()

            # --------------- title ---------------
            spacer= " " * 10
            self.root.title(spacer + title_for_root)
            #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # --------------- Label (word) ---------------
            self.main_word = tk.Label(self.root,text="",fg="black",bg="#169976",width="20",height="5",font=("Courier", 32))
            self.main_word.pack(pady=50)
            #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            self.current_word_index = -1 
            self.current_List_index_ = 0

            self.All_word_input_list=All_list_fo_word.copy()

            self.list_of_Words = self.All_word_input_list[self.current_List_index_]
            # ----------------- add current word object.
            self.currentWordObject = None
            # !================= laod new List of word
            tmp_Word_L = [Lernkartei_word('T','C',0)]
            self.new_All_list_fo_word = []
            for i in range(6):
                self.new_All_list_fo_word.append(tmp_Word_L)
            # =============================================
            
            # --------------- Buttom(1): Next word ---------------
            Buttom_1 = tk.Button(self.root,
                   text="Next word", 
                   command=self.Next_word_for_Button1,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100
                    )
            Buttom_1.place(x=5, y=54 - 4)

            # ------- ----- B2 : Collocations
            Buttom_2 = tk.Button(self.root,
                   text="Collocations", 
                   command=self.show_Collocations_of_curent_word,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100
                    )
            Buttom_2.place(x=5, y=((54*2) + 16))
            
            # ------- ----- B3 : Wrong
            Buttom_3 = tk.Button(self.root,
                   text="wrong", 
                   command=self.push_WrongButtom,
                   activebackground="red", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100
                    )
            Buttom_3.place(x=670, y=(54*1))

                        
            # ------- ----- B4 : pronounce
            Buttom_4 = tk.Button(self.root,
                   text="pronounce", 
                #    command=self.def_4,
                   activebackground="#BBD8A3", 
                   activeforeground="white",
                   anchor="center",
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                #    -----------------------
                   overrelief="sunken",
                #    -----------------------
                   wraplength=100
                    )
            Buttom_4.place(x=(800//2) - 50 , y=(54*4))
            
            
            #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def set_geometry_center(self,window_width:int=800,window_height:int=300):
            """می خواهیم صحفه دقیقا وسط مانیتور باشه

            Args:
                window_width  (int, optional): عرض برنامه ما    . Defaults to 400.
                window_height (int, optional): ارتفاع برنامه ما . Defaults to 250.
            """
            #  پیدا کردن ارتفاع و عرض نمایشگر کاربر
            screen_width  = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
             
            # پیداکردن پدینگ مورد دلخواه
            x_offset = (screen_width - window_width)   // 2
            y_offset = (screen_height - window_height) // 2


            self.root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
            self.root.resizable(False,False)

            # ----------
            self.root.config(bg ='#1DCD9F')

        def update_word(self,new_word:str=""):
             self.main_word.config(text=new_word)

        def Next_word_for_Button1(self):
                # ==================================
                if (self.currentWordObject != None):
                      self.currentWordObject.status += 1

                # =====================================


                self.current_word_index += 1
                # self.current_word_index %= len(self.list_of_Words)

                if(self.current_word_index >= len(self.list_of_Words)):
                      self.SetAllWordList(self.list_of_Words)
                      self.open_new_Box_of_words()
                      return
                # ----------------------------------------------<< add current word object :) >> ------------------------------------------
                self.currentWordObject = self.list_of_Words[self.current_word_index]
                self.update_word(self.currentWordObject.txt)

                # -------------------------------------------------------------------------------------------------

        def show_Collocations_of_curent_word(self):
                    if(self.currentWordObject != None):
                        self.update_word(self.currentWordObject.collocations) 

        def push_WrongButtom(self):
                if(self.currentWordObject != None): # زمانی که اصلا کلمه نداریم که معنی نمیده وضعیت را صفر کنیم
                    """why status = 0 ? :)
                        # اگر کلمه ای اشتباه گفته شد باید بره به باکس شماره یک
                        # برای همین امر اول وضعیت را به صفر تغییر داده و تابع کلمه بعد را فرا می خوانیم 
                        # با توجه به این که برای نمایش کلمه بعدی همیشه وضیعت کلمه قبل را یکی اضافه می کنیم یعنی
                        # به جعبه بعدی اناتقال میدهیم تا برای دفعه بعدی راحت باشیم
                        # به همین علت این جا وضعیت را صفر قرار دادیم تا دفعه بعدی در جعبه شماره یک که جعبه اول هست انتقال یابد 
                    """
                    self.currentWordObject.status = 0
                    self.Next_word_for_Button1()    # got to next word

        # +++++++++++++++++++++++

        def SetAllWordList(self,list_of_word_is:list[Lernkartei_word]):
            for w in list_of_word_is:
                print(w.txt , 's: ', w.status)
                # break
                if(w.status <=1 ):
                    self.new_All_list_fo_word[0].append(w)

                if(w.status >= len(self.new_All_list_fo_word)):
                    self.new_All_list_fo_word[-1].append(w)
  
                else:
                    self.new_All_list_fo_word[w.status].append(w)

            print('-'*6 , ' End curent box ','-'*6)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        def open_new_Box_of_words(self):
            
            self.current_word_index  = -1 
            self.current_List_index_ += 1
            if(self.current_List_index_ >= len(self.All_word_input_list)):
                  print('EndL')
                  self.root.destroy()
                #   Save New word in pkl file 
            else:
                    self.list_of_Words = self.All_word_input_list[self.current_List_index_]
                    self.Next_word_for_Button1()


        #! =================================================
        #  ~~~~~~~~~~~~~~~~~~ <<  RUN >> ~~~~~~~~~~~~~~~~~~
        #! =================================================
        def Run(self):
            self.set_geometry_center()
            self.root.mainloop()

#  ------------------------------------------------------------
#  ------------------------------------------------------------

class RunAppForEnglish():
    # """_summary_
    # برای آینده این که لیست و شافل کنی و  با کیبورد کار کنه و ..
    # """
    def __init__(self,DataBase_path_is = '../Data Base') -> None:
            self.DataBase_path_is = DataBase_path_is
    
    def loadPKLfiles(self,Debug = False):
            # pass
            list_of_Word_for_pass = []
            for box_number in range(6):
                # ----  << set path >>             
                mypath = os.path.join(self.DataBase_path_is, f'Box_{box_number+1}.pkl')
                # -------------------------------
                if(Debug):
                    print(mypath)
                # -------------------------------
                with open(mypath, 'rb') as inp:
                    tmp_list_is = pickle.load(inp)
                # -------------------------------
                if(Debug):
                    # print(tmp_list_is[0])
                    print('len: ',len(tmp_list_is))
                    first_item_is  = tmp_list_is[0]
                    print(first_item_is)
                    print('~'*20)
                # -------------------------------

                list_of_Word_for_pass.append(tmp_list_is)

            return list_of_Word_for_pass




if (__name__ == '__main__'):
    # ! -----------------<< test 1 >>---------------------------
    """_summary_
    برای خودم دو تا باکس دل خواه با مقادیر گفته شده ساختیم و تست کردیم
    """
    # tmp_1 = [Lernkartei_word('A','a',1) ,Lernkartei_word('AA','aa',1)  ]
    # tmp_2 = [Lernkartei_word('B','b',2) ,Lernkartei_word('BB','bb',2)  ]
    # M = [tmp_1, tmp_2]
    # AppForLearningEnglish('',M).Run()
    # ! --------------------------------------------

    # ---------------
    """_summary_
        روی کل دیتاست ما-همان باکس های که گفتیم اجراه بشه
    """
    L = RunAppForEnglish().loadPKLfiles()
    AppForLearningEnglish('',L).Run()


    