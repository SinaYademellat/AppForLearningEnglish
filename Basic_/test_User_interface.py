from User_interface import AppForLearningEnglish
from Lernkartei_data_structure import Lernkartei_word


if __name__ == '__main__':
    tmp_txt_list = []
    for i in range(5):
            tmp_txt_list.append(chr(ord('A')  + i ))
    print(tmp_txt_list)
    my_word_list = []
    for i in tmp_txt_list :
        tmp_word = Lernkartei_word(Txt = i ,Collocations= i+i ,Status=1)
        my_word_list.append(tmp_word)

    tmp_ = AppForLearningEnglish('test',my_word_list)
    tmp_.Run()