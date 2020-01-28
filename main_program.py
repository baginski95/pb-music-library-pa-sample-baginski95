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


def add_album():
    albums = file_handling.import_data()
    album_properties = get_inputs(['artist name: ', 'album name: ', 'release year: ', 'genre: ', 'length: '])
    albums.append(album_properties)
    file_handling.export_data(albums, mode='w')


def remove_album():
    ALBUM_NAME = 0
    albums = file_handling.import_data()
    get_album_name = get_inputs(['album name: '])
    for album in albums[:]:
        if album[ALBUM_NAME] == get_album_name[0]:
            albums.remove(album)
    file_handling.export_data(albums, mode='w')


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
