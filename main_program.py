"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import display
import sys

MAIN_MENU = ['Add album', 'Remove Album', 'Get albums by genre', 'Get longest album','Get total albums length', 'Exit']


def get_inputs(list_labels):
    inputs = []
    for label in list_labels:
        get_input = input(label)
        inputs.append(get_input)
    return inputs


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """


if __name__ == '__main__':
    main()
