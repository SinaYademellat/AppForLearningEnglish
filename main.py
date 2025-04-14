import sys

def main():
    arguments = sys.argv
    is_first_time = arguments[1]
    if(is_first_time == 'y'):
        print('yes')
        return 0 
    
    else:
        print('No')
        return 1


if (__name__ == '__main__'):
    main()