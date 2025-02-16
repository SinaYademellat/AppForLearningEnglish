from User_interface import AppForLearningEnglish
from tmp_code import usefile

if __name__ == '__main__':
    M = []
    M = usefile()
    print(M)
    main_windo = AppForLearningEnglish()
    main_windo.Run()