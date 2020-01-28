"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import display
import sys

MAIN_MENU = ['Add album', 'Remove Album', 'Get albums by genre', 'Get longest album', 'Get total albums length', 'Get genres stats', 'Get oldest album', 'Exit']
ALBUM_NAME = 0


def get_inputs(list_labels):
    inputs = []
    for label in list_labels:
        get_input = input(label)
        inputs.append(get_input)
    return inputs


def add_album(albums):
    album_properties = get_inputs(['artist name: ', 'album name: ', 'release year: ', 'genre: ', 'length: '])
    albums.append(album_properties)
    file_handling.export_data(albums, mode='w')


def remove_album(albums):
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
    is_program_working = True
    while is_program_working:
        display.print_program_menu(MAIN_MENU)
        albums = file_handling.import_data()
        choose_option = get_inputs(['Enter option number: '])
        option = choose_option[0]
        if option == '0':
            add_album(albums)
        elif option == '1':
            remove_album(albums)
        elif option == '2':
            get_genre = get_inputs(['genre: '])
            display.print_albums_list(music_reports.get_albums_by_genre(albums, get_genre[0]))
        elif option == '3':
            display.print_album_info(music_reports.get_longest_album(albums))
        elif option == '4':
            total_albums_length = music_reports.get_total_albums_length(albums)
            display.print_command_result(f'Total albums length in mins: {total_albums_length}')
        elif option == '5':
            genre_stats = music_reports.get_genre_stats(albums)
            for genre_name, amount_of_albums in genre_stats.items():
                display.print_command_result(f'{genre_name}|{amount_of_albums}')
        elif option == '6':
            oldest_album = music_reports.get_oldest_album(albums)
            display.print_album_info(oldest_album)
        elif option == '7':
            sys.exit()


if __name__ == '__main__':
    main()
