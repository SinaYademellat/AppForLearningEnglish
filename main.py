import sys
import Basic_.first_loading as load_for_first_time

def main():
    arguments = sys.argv
    is_first_time = arguments[1]
    if(is_first_time == 'y'):
        print('yes')
        """راه درستش 
        راه درستش این هست که به شکل پکچ کنیم و ران بگیریم 
        """
        load_for_first_time.Run_first_loading()
        
        return 0 
    
    else:
        print('No')
        return 1


if (__name__ == '__main__'):
    main()