from txt_to_mp3 import text2mp3

class my_word():
    def __init__(self, word:str , Collocation:str=None ,  path:str = 'voice'):

        self.word = word
        self.collocation = Collocation
        self.path   = path


if __name__ == '__main__':
      
        w =  my_word(
                    word='test_0',
                    Collocation='An introduction to ML.',
                    path = 'voice'
                    )
    

        A = text2mp3(w.path)
        print('mode 1: ')
        A.pronunciation(w.word , new_txt_for_mp3 = w.collocation)
        
        print('mode 2: ')
        A.pronunciation(w.word , new_txt_for_mp3 = w.collocation)
        