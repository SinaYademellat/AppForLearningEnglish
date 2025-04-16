import tkinter as tk

class AppForLearningEnglish():
        def __init__(self , title_for_root:str="sina yademellat" , list_of_Words:list = ['test_1', 'test_2', 'test_3']):
            '''
                title_for_root : اسم آن گروه از لغات باشد بهتر است 
            '''
            
            self.root = tk.Tk()

            # --------------- title ---------------
            spacer= " " * 10
            self.root.title(spacer + title_for_root)
            #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            # --------------- Label ---------------
            self.main_word = tk.Label(self.root,text="",fg="black",bg="white",width="20",height="5",font=("Courier", 32))
            self.main_word.pack(pady=50)
            #! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            self.current_word_index = -1 
            self.list_of_Words = list_of_Words
            
            # --------------- Buttom ---------------
            Buttom_1 = tk.Button(self.root,
                   text="Buttom_1", 
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
            Buttom_1.place(x=5, y=54)

            # ------- ----- B2
            Buttom_2 = tk.Button(self.root,
                   text="Buttom_2", 
                #    command=self.Next_word_for_Button1,
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
            Buttom_2.place(x=5, y=(54*2))
            
            # ------- ----- B3
            Buttom_3 = tk.Button(self.root,
                   text="Buttom_3", 
                #    command=self.Next_word_for_Button1,
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
            Buttom_3.place(x=5, y=(54*3))

                        
            # ------- ----- B4
            Buttom_4 = tk.Button(self.root,
                   text="Buttom_4", 
                #    command=self.Next_word_for_Button1,
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
            Buttom_4.place(x=5, y=(54*4))
            
            
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

        def update_word(self,new_word:str=""):
             self.main_word.config(text=new_word)

        def Next_word_for_Button1(self):
                self.current_word_index += 1
                self.current_word_index %= len(self.list_of_Words)
                self.update_word(self.list_of_Words[self.current_word_index])

        def Run(self):
            self.set_geometry_center()
            self.root.mainloop()
