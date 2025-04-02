"""_summary_
 این این قسمت یک فیلم یوتیوب هست که یاد داد

"""

class Lernkartei_word:
    def __init__(self, Txt:str  , Status:int , Collocations:str = None ) -> None:
        """_summary_

        Args:
            Txt (str): _description_
            Status (int):
                day 1  : ==> 1
                day 2  : ==> 2
                day 3  : ==> 3
                week 1 : ==> 4
                week 2 : ==> 5
                Months : ==> 6

        """
        self.txt = Txt
        self.collocations = Collocations
        # self.farsi = Farsi
        self.status = Status 

    def Save_in_txt(self):
        main_path = 'tmp_db_txt/'
        txt_file =f'Status_{self.status}.txt'

        path_is = main_path + 'Txt_' + txt_file 
        f = open(path_is, "a")
        f.write(self.txt + '\n')
        f.close()

        path_is = main_path + 'collocations_' + txt_file 
        f = open(path_is, "a")
        f.write(self.collocations + '\n')
        f.close()

if __name__ == '__main__':
    A = Lernkartei_word(Txt='test_1', Status=2,Collocations='colloca_1')
    A.Save_in_txt()
    A.txt ='test_2'
    A.Save_in_txt()