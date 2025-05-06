import sys
import Basic_.first_loading as load_for_first_time
import Basic_.User_interface as Basic_UserInterFace
import Basic_.Add_New_Word as AddNEWItem


def main():
    arguments = sys.argv
    is_first_time = arguments[1]
    if(is_first_time == 'y'):
        print('<< Data Base >>' ,end=' ')
        load_for_first_time.Run_first_loading()
        print(': ok',end='\n')

    print('<< Run >>')
    Basic_UserInterFace.Run_user_interface_main()
    
    print('<< Add New >>')
    AddNEWItem.Run_Add_New_word()
    return 0

if (__name__ == '__main__'):
    main()