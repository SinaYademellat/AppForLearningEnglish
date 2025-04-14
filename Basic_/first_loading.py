"""
    _summary_
    همون بوت استرپینگ هست ولی فقط موقع نصب نیاز هست اجرا بشه

"""
import os
import pickle

from Lernkartei_data_structure import Lernkartei_word


class FisrtTimeLoad:
    def __init__(self,path_of_pkl_file_as_Db:str) -> None:
        
        self.Path_for_pkl_file_as_Db = path_of_pkl_file_as_Db

        for box_number in range(6):
            # tmp_item
            test_word_is = Lernkartei_word(Txt = f'Txt_box{box_number+1}' ,Collocations=f'Collocations_box{box_number+1}' ,Status=box_number+1)
            temp_list   = [test_word_is]

            # ----  << set path >>
            mypath = os.path.join(path_of_pkl_file_as_Db, f'Box_{box_number+1}.pkl')
            # Saving 
            with open(mypath, 'wb') as outp:
                pickle.dump(temp_list, outp, pickle.HIGHEST_PROTOCOL)
            del temp_list 


def Run_first_loading():
    DataBase_path = '../Data Base'
    """ ایده برای آینده
            ! در آینده این قسمت را می توان این به این شکل پیاده سازی کرد:
             زمان اجرا از کامند لاین آدرس را بگیریم و در مرحله بعدی
             بنا بر سیتم عامل همان فولدر را می سازیم
            ?  mkdir db_pkl .
    """
   
    bootstrapping = FisrtTimeLoad(DataBase_path)

    print('Data Base is Ok')


if (__name__ == '__main__') :
    Run_first_loading()
