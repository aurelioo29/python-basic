import random
import sys
sys.path.insert(0, 'D:/Coding/website/python_basic/package')
import library
sys.path.insert(0, 'D:/Coding/website/python_basic/games')
import cuy


def main():
    library.message_come()
    cuy.start()
    library.exit_program()
    
if __name__ == "__main__":
    main()