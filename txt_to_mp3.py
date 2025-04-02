from gtts import gTTS
from playsound import playsound
from pathlib import Path

class text2mp3():
    def __init__(self, save_path:str =None):
        self.save_path = save_path
        self.list_of_mp3 = []


    def set_list_of_mp3(self):
            directory = Path(self.save_path)

            mp3_files = list(directory.glob("*.mp3"))
            mp3_files = [file.name for file in mp3_files]
            # print(mp3_files)

            self.list_of_mp3 = mp3_files


    def make_mp3(self,name_of_mp3:str , path_for_save:str ,input_txt , slow_parm:bool = False ):
        language = 'en'
        myobj = gTTS(text = input_txt, lang=language, slow=slow_parm)
        myobj.save(f"{path_for_save}/{name_of_mp3}.mp3")




    def pronunciation(self, input_word:str='sina1', new_txt_for_mp3:str=None):
            """use playsound to play mp3
            """
            
            if(len(self.list_of_mp3) == 0 ):
                    self.set_list_of_mp3()

        
            current_item = (input_word+'.mp3')

            if( current_item in self.list_of_mp3):
                        file = f"{self.save_path}/{input_word}.mp3"
                        file = file.replace(" ", "%20")
                        playsound(file, True)
            else:
                    self.make_mp3( name_of_mp3 =  input_word ,path_for_save = self.save_path ,input_txt = new_txt_for_mp3, slow_parm = False)
                    self.list_of_mp3.append(current_item)
                    self.pronunciation(input_word)
