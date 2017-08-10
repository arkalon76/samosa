import os
import guessit
from imdbpie import Imdb
from guessit import guessit

SUPPORTED_CONTAINERS = ['.mkv', '.avi', '.mp4', '.m4v']
imdb = Imdb(anonymize=True)  # to proxy requests


def find_all_media_files(dir_to_search, extentions=SUPPORTED_CONTAINERS):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_to_search):
        for filename in filenames:
            if os.path.splitext(filename)[1] in extentions:
                file_list.append(filename)
    return file_list


def resolve_imdb_from_filename(test_file):
    # First, let's extract the name of the movie and it's year
    nameDict = guessit(test_file)
    try:
        title = nameDict['title']
        year = str(nameDict['year'])
    except KeyError:
        print('This file "' + test_file + '" seems oddly named.\
              Please follow [title] [year] format')
        return None
    imdbResult = imdb.search_for_title(title)
    for movie in imdbResult:
        if year == movie['year']:
            print('Match found')
            return movie['imdb_id']
