from Utils import Utils
from meta_reader import osu_file
import os
import tempfile
import zipfile
import sys
import shutil
from collections import defaultdict


# Get bg/bga/audio for single .osu file.
def _get_related_file_for_osu(file: osu_file):
    return [file.audio_file, file.bg_name]


def fetch_files(song_paths: dict, song_list: dict):
    oszs = set()
    all_osu_files = defaultdict(set)
    for key, path in song_paths.items():
        if path[-4:] == '.osz':
            oszs.add(path)
        elif path[-4:] == '.osu':
            files = _get_related_file_for_osu(song_list[key])
            files.append(path)
            files = set([os.path.join(os.path.dirname(path), f) for f in files])
            all_osu_files[os.path.dirname(path)] = all_osu_files[os.path.dirname(path)].union(files)
    return oszs, all_osu_files

def format(song_paths: dict, song_list: dict, collection_name, collection_artist, creator, verbose_func):
    u = Utils(os.getcwd())
    f = tempfile.TemporaryDirectory(dir=os.getcwd())

    u.path = f.name + "\\"

    oszs, all_osu_files = fetch_files(song_paths, song_list)

    verbose_func("Totally: " + str(len(oszs)) + " oszs and " + str(len(all_osu_files)) + " osu files.")

    all_files = []

    for i, osz in enumerate(oszs):
        verbose_func("Processing osz " + str(i) + ": " + os.path.basename(osz))
        zip = zipfile.ZipFile(osz)
        all_file_names = zip.namelist()
        zip.extractall(u.path)
        u.name_list = all_file_names
        all_diffs = u.get_all_osu_diffs()
        u.all_osu = all_diffs
        for diff in all_diffs:
            u.rename_osz_metadata(diff, collection_name, collection_name, collection_artist, collection_artist, creator)
        u.change_audio_file_name()
        all_files += u.get_all_files_after_renaming()
        u.reset()
    for i, (folder, related_files) in enumerate(all_osu_files.items()):
        verbose_func("Processing osu file under " + folder + ".")
        for file in related_files:
            old_path = os.path.join(folder, file)
            shutil.copy(old_path, u.path)
        u.name_list = related_files
        all_diffs = u.get_all_osu_diffs()
        u.all_osu = all_diffs
        for diff in all_diffs:
            u.rename_osz_metadata(diff, collection_name, collection_name, collection_artist, collection_artist, creator)
        u.change_audio_file_name()
        all_files += u.get_all_files_after_renaming()
        u.reset()

    new_name = collection_artist + " - " + collection_name + ".osz"
    zip = zipfile.ZipFile(new_name, mode='w')
    for file in all_files:
        zip.write(u.path + file, file)

if __name__ == '__main__':
    pass