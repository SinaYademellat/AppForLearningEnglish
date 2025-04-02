from User_interface import AppForLearningEnglish
from tmp_code import usefile

if __name__ == '__main__':
    My_words = usefile()
    print(My_words)
    main_windo = AppForLearningEnglish(title_for_root='day 1',list_of_Words=My_words)
    main_windo.Run()