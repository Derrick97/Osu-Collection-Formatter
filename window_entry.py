import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem

from window import Ui_MainWindow
from meta_reader import osu_file
import os

import hashlib

import io

import zipfile

from formatter import fetch_files, format


class MainWindowUIClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowUIClass, self).__init__(parent=parent)
        self.setupUi(self)
        self.current_song_list = {}
        self.current_song_path = {}
        self.last_browse_address = r"E:\osu!\Songs"

    def assign_key(self, f):
        sha256_hash = hashlib.sha256()
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        key = sha256_hash.hexdigest()
        return key

    def debugPrint(self, msg):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.debug.append(msg)

    def show_progress(self, msg):
        self.progressField.append(msg)

    def browse_beatmaps(self):
        self.debugPrint("browse")
        fname = QFileDialog.getOpenFileName(None, 'Open file', self.last_browse_address,
                                            filter="Osu! Beatmap file (*.osu *.osz);")
        if fname[0]:
            filename = fname[0]
            if filename[-4:] == '.osu':
                self.browse_from_osu_file(filename)
            elif filename[-4:] == '.osz':
                self.browse_from_osz_file(filename)
            else:
                raise ValueError("Unsupported Filetype.")
        else:
            self.debugPrint("No file selected.")

    def browse_from_osu_file(self, filename):
        self.debugPrint("Browsed: " + filename)
        try:
            with open(filename, "rb") as f:
                key = self.assign_key(f)
                self.current_song_path[key] = filename
                self._add_chart_info(filename, key)
        except AssertionError:
            print("Assertion Failed: not osu")
        self.debugPrint(str(fetch_files(self.current_song_path, self.current_song_list)))

    def _add_chart_info(self, filename, key, f=None, archive_source=None):
        assert key != -1
        self.debugPrint("Adding: " + filename)
        if key in self.current_song_list:
            self.debugPrint("Chart already added.")
            return
        file = osu_file(filename, f, archive_source)
        if not file.init_error:
            self.current_song_list[key] = file
        else:
            self.debugPrint("Error adding chart " + filename + ": " + file.init_error)
            del self.current_song_path[key]
            return
        song_item = QListWidgetItem(os.path.basename(filename))
        song_item.setData(0x0100, key)
        self.debugPrint(song_item.data(0x0100))
        self.song_list.addItem(song_item)

    def browse_osu_from_folder(self, folder):
        for r, d, f in os.walk(folder):
            for filename in f:
                if filename[:-4] == '.osu':
                    self.browse_from_osu_file(filename)

    def browse_from_osz_file(self, filename):
        self.debugPrint("Browsed: " + filename)
        try:
            with zipfile.ZipFile(filename, mode='r') as archive:
                for name in archive.namelist():
                    if name[-4:] == '.osu':
                        with archive.open(name, 'r') as file:
                            key = self.assign_key(file)
                            self.current_song_path[key] = filename
                            self.debugPrint("osz: key: " + str(key))
                        with archive.open(name, 'r') as raw:
                            f = io.TextIOWrapper(raw, encoding='utf-8')
                            self._add_chart_info(name, key, f, archive_source=archive)
        except zipfile.BadZipfile:
            print("Bad osz file")
        print(self.current_song_path)
        print(self.current_song_list)
        # self.debugPrint(str(fetch_files(self.current_song_path, self.current_song_list)))

    def set_enable_all_field(self, flag):
        self.artistLineEdit.setEnabled(flag)
        self.artistRomanisedLineEdit.setEnabled(flag)
        self.songNameLineEdit.setEnabled(flag)
        self.songNameRomanisedLineEdit.setEnabled(flag)
        self.difficultynameLineEdit.setEnabled(flag)
        self.levelLineEdit.setEnabled(flag)

    def clear_fields(self):
        self.artistLineEdit.clear()
        self.artistRomanisedLineEdit.clear()
        self.songNameLineEdit.clear()
        self.songNameRomanisedLineEdit.clear()
        self.difficultynameLineEdit.clear()
        self.levelLineEdit.clear()
        self.mapperLineEdit.clear()

    def toggle_generate(self):
        if len(self.packNameLineEdit.text()) > 0 and \
                len(self.packAuthorLineEdit.text()) > 0:
            self.generateButton.setEnabled(True)
        else:
            self.generateButton.setEnabled(False)

    def format_pack(self):
        try:
            assert len(self.packNameLineEdit.text()) > 0 and \
                   len(self.packAuthorLineEdit.text()) > 0
            if len(self.packArtistLabel.text()) == 0:
                artist = "Various Artists"
            else:
                artist = self.packArtistLabel.text()
            format(self.current_song_path, self.current_song_list, self.packNameLineEdit.text(), artist,
                   self.packAuthorLineEdit.text(), self.show_progress)
        except AssertionError:
            print("Input missing.")

    def display_info(self, item: QListWidgetItem):
        if len(self.song_list.selectedItems()) > 1:
            self.set_enable_all_field(False)
            self.clear_fields()
        else:
            file: osu_file = self.current_song_list[item.data(0x0100)]
            self.artistLineEdit.setText(file.artist)
            self.artistRomanisedLineEdit.setText(file.artist_unicode)
            self.songNameLineEdit.setText(file.title)
            self.songNameRomanisedLineEdit.setText(file.roman_title)
            self.difficultynameLineEdit.setText(file.version)
            self.mapperLineEdit.setText(file.creator)
            self.set_enable_all_field(True)

    def remove_chart(self):
        items = self.song_list.selectedItems()
        self.set_enable_all_field(False)
        for item in items:
            key = item.data(0x0100)
            del self.current_song_path[key]
            self.song_list.takeItem(self.song_list.row(item))
            del self.current_song_list[key]
        self.clear_fields()
        self.set_enable_all_field(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainWindowUIClass()
    ui.show()
    sys.exit(app.exec_())
