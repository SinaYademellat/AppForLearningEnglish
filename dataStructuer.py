from gtts import gTTS
from playsound import playsound
import os

class my_word():
    def __init__(self, word:str , Collocation:str=None):

        self.word = word
        self.collocation = Collocation


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def pronunciation(self,path:str = 'voice'):
        """use playsound to play mp3

        Args:
            path (str, optional): این مسیر را باید بعدا از دیتاست گرفت. Defaults to 'voice'.
        """


        # برسی اینکه آیا قبلا این کلمه ساخته شده یا نه
        if(os.system(f'dir {path} | FINDSTR {self.word}.mp3') == 0):
                    file = f"{path}/{self.word}.mp3"
                    file = file.replace(" ", "%20")
                    playsound(file, True)

        else:
                # اگر ساخته نشده بود بساز و بازگشتی فراخوانی کن
                self.make_mp3(input_txt = 'this is new word',path = path , slow_parm = False)
                self.pronunciation(path)


    # ! حود کلمه خودش و فراخوانی نکنه بهتر هست
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    def make_mp3(self, input_txt:str, path:str = 'voice' ,slow_parm:bool = False):
        """تبدیل متن به صدا و ذخیره آن به کمک گوگل

        Args:
            input_txt (str): جمله دلخواه
            slow_parm (bool, optional): سرعت خواندن جمله. Defaults to False.
        """

        language = 'en'
        myobj = gTTS(text =input_txt, lang=language, slow=slow_parm)
        myobj.save(f"{path}/{self.word}.mp3")


if __name__ == '__main__':
        
        A = my_word('sina1')
        A.make_mp3(input_txt = 'hi sina.unaccustomed atmosphere',slow_parm = True)
        A.pronunciation()

        print((' '*10)+'*'*23)

        A = my_word('sina2')
        A.make_mp3(input_txt = 'hi sina.unaccustomed atmosphere',slow_parm = False)
        A.pronunciation()

        A = my_word('sina3')
        A.pronunciation()
