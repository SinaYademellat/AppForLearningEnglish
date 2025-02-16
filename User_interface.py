import tkinter as tk

class AppForLearningEnglish():
        def __init__(self , title_for_root:str="sina yademellat"):
            '''
                title_for_root : اسم آن گروه از لغات باشد بهتر است 
            '''
            self.root = tk.Tk()
            self.main_word = tk.Label(self.root,text="",fg="black",bg="white",width="20",height="5",font=("Courier", 32))
            self.main_word.pack(pady=50)

            spacer= " " * 10
            self.root.title(spacer + title_for_root)

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
        
        def Run(self):
            self.set_geometry_center()
            self.update_word('Ali')
            self.root.mainloop()


