ARTIST_NAME = 0
ALBUM_NAME = 1
YEAR = 2
GENRE = 3
lENGTH = 4


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    same_genre_albums = []
    for album in albums:
        if album[GENRE] == genre:
            same_genre_albums.append(album)
    return same_genre_albums


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album = albums[0]
    for album in albums:
        album_time = float(album[lENGTH].replace(':', '.'))
        longest_album_time = float(longest_album[lENGTH].replace(':', '.'))
        if album_time > longest_album_time:
            longest_album = album
    return longest_album


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    total_albums_length = 0.00
    for album in albums:
        minutes, seconds = album[lENGTH].split(':')
        total_albums_length += float(minutes) + float(seconds)/60.0
    total_albums_length = round(total_albums_length, 2)
    return total_albums_length


def get_genre_stats(albums):
    """
    Get all genres and count how many albums they have
    :param list albums: albums' data
    :returns: all genres and their amount of albums
    :rtype: dict
    """
    genres_dict = {}
    for album in albums:
        genres_dict.setdefault(album[GENRE], 0)
        genres_dict[album[GENRE]] += 1
    return genres_dict


def get_last_oldest(albums):
    """
    Get oldest album from all albums
    :param list albums: albums' data
    :returns: oldest album specifications
    :rtype: list
    >>> [["The Beatles", "Revolver", "1966", "rock", "34:43"],["David Bowie", "Low", "1977", "rock", "38:26"]]
    [["The Beatles", "Revolver", "1966", "rock", "34:43"]]
    """
    oldest_album = albums[0]
    for album in albums:
        if int(album[YEAR]) <= int(oldest_album[YEAR]):
            oldest_album = album
    return oldest_album


def get_last_oldest_of_genre(albums, genre):
    """
    Get oldest album of given genre
    :param list albums: albums' data
    :param str genre: genre to filter by
    :returns: oldest album specifications in given genre
    :rtype: list
    """
    oldest_genre_album = albums[0]
    for album in albums:
        if album[GENRE] == genre and (int(album[YEAR]) < int(oldest_genre_album[YEAR])):
            oldest_genre_album = album
    return oldest_genre_album
