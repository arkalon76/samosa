import os

SUPPORTED_CONTAINERS = ['.mkv', '.avi', '.mp4', '.m4v']


def find_all_media_files(dir_to_search, extentions=SUPPORTED_CONTAINERS):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_to_search):
        for filename in filenames:
            if os.path.splitext(filename)[1] in extentions:
                file_list.append(filename)
    return file_list
