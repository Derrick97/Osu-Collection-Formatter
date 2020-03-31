import os


def remove_unallowed_character(s):
    unallowed = ["/", "\\", "*", ":", "?", "<", ">", "|", "\""]
    for c in unallowed:
        if c in s:
            s = s.replace(c, " ")
    return s


class Utils:
    def __init__(self, path):
        self.path = path
        self.audio_name_dict = {}
        self.music_counter = 0
        self.bg_counter = 0
        self.name_list = []
        # self.all_bgs = []
        self.bg_dict = {}
        self.all_osu = []
        self.all_osu_after_renamed = []

    def find_osz_files(self):
        targets = []
        for r, d, f in os.walk(self.path):
            for file in f:
                if file[-4:] == ".osz":  # find all file using osz as extension.
                    targets.append(os.path.join(file))
        return targets

    def rename_osz_metadata(self, osu_file_name, new_title, new_title_unicode, new_artist, new_artist_unicode,
                            new_creator, new_version_name="", version_style="None"):
        line_list = []
        old_title = ""
        old_artist = ""
        old_creator = ""
        old_audio_name = ""
        old_version_name = ""
        has_visited_audio = False
        bg_last_line_index = -2
        f = open(osu_file_name, "r+", encoding='utf-8')
        for i, line in enumerate(f):
            if "AudioFilename:" in line:
                old_audio_name = line[15:].strip("\n")
                if old_audio_name in self.audio_name_dict.keys():
                    line_list.append("AudioFilename: " + self.audio_name_dict[old_audio_name] + "\n")
                    has_visited_audio = True
            elif "Title:" in line:
                old_title = line[6:].strip("\n")
                line_list.append("Title:" + new_title + "\n")
            elif "TitleUnicode:" in line:
                line_list.append("TitleUnicode:" + new_title_unicode + "\n")
            elif "Artist:" in line:
                old_artist = line[7:].strip("\n")
                line_list.append("Artist:" + new_artist + "\n")
            elif "ArtistUnicode" in line:
                line_list.append("ArtistUnicode:" + new_artist_unicode + "\n")
            elif "Creator:" in line:
                old_creator = line[8:].strip("\n")
                line_list.append("Creator:" + new_creator + "\n")
            elif "Version:" in line:
                old_version = line[8:].strip("\n")
                if new_version_name:
                    line_list.append("Version:" + new_version_name + "\n")
                else:
                    new_version_name = self.build_version_name(old_title, old_artist, old_creator, new_creator,
                                                               old_version)
                    line_list.append("Version:" + new_version_name + "\n")
            elif "BeatmapID:" in line:
                line_list.append("BeatmapID:0" + "\n")
            elif "BeatmapSetID:" in line:
                line_list.append("BeatmapSetID:-1" + "\n")
            elif "//Background and Video events" in line:
                line_list.append(line)
                bg_last_line_index = i
            elif i == bg_last_line_index + 1:
                if line[0] == "/":
                    line_list.append(line)
                else:
                    old_bg_name = line.split(",")[2][1:-1]
                    if not old_bg_name in self.name_list:
                        print("The BG of " + osu_file_name + " is not found in the directory.")
                        continue
                    # try:
                    #     self.name_list.index(old_bg_name)
                    # except:
                    #     print("The BG of " + osu_file_name + " is not found in the directory.")
                    #     print(osu_file_name + ": 该文件背景图(BG)未在osz中找到，中止操作。")
                    #     raise ValueError

                    if not old_bg_name in self.bg_dict.keys():
                        new_bg_name = self.rename_osz_bg(old_bg_name, new_title_unicode, self.bg_counter)
                        self.bg_counter += 1
                        self.bg_dict[old_bg_name] = new_bg_name
                    else:
                        new_bg_name = self.bg_dict[old_bg_name]
                    new_line = line.split(",")
                    new_line[2] = "\"" + new_bg_name + "\""
                    line_list.append(",".join(new_line))
            else:
                line_list.append(line)
        if not has_visited_audio:
            self.audio_name_dict[old_audio_name] = self.get_new_audio_name(old_audio_name, old_title,
                                                                           self.music_counter)
            line_list[3] = "AudioFilename: " + self.audio_name_dict[old_audio_name] + "\n"
            self.music_counter += 1
        f.truncate(0)
        with open(osu_file_name, "w", encoding="utf-8") as f:
            f.writelines(line_list)
        new_name = self.rename_osu_file(new_artist_unicode, new_title_unicode, new_creator, new_version_name)
        self.all_osu_after_renamed.append(new_name)
        os.listdir(self.path)
        os.rename(osu_file_name, self.path + new_name)

    def build_version_name(self, old_title, old_artist, old_creator, new_creator, old_version):
        if old_creator == new_creator:
            return remove_unallowed_character(old_artist + " - " + old_title + " [" + old_version + "]")
        else:
            return remove_unallowed_character(
                old_artist + " - " + old_title + " [" + old_creator + "\'s " + old_version + "]")

    def get_all_osu_diffs(self):
        return [self.path + file for file in self.name_list if file[-4:] == ".osu"]

    # def get_all_bg(self, name_list):
    #     supported_extension = [".jpg", ".jpeg", ".png"]
    #     self.all_bgs = [file for file in name_list if file[-4:] in supported_extension]

    def get_new_audio_name(self, old_audio_name, old_title, counter):
        try:
            extension_index = old_audio_name.index(".")
            return remove_unallowed_character(old_title + "_" + str(counter) + old_audio_name[extension_index:])
        except ValueError:
            print("Unsupported song format: no extensions.")

    def rename_osz_bg(self, old_bg_name, new_bg_name, counter):
        new_name = new_bg_name + "_" + str(counter) + old_bg_name[old_bg_name.index("."):]
        os.rename(self.path + old_bg_name, self.path + new_name)
        return new_name

    def reset(self):
        self.audio_name_dict = {}
        self.bg_dict = {}
        self.all_osu_after_renamed = []
        self.name_list = []

    def change_audio_file_name(self):
        for k, v in self.audio_name_dict.items():
            v = remove_unallowed_character(v)
            os.rename(self.path + k, self.path + v)

    def rename_osu_file(self, new_artist_unicode, new_title_unicode, new_creator, new_version_name):
        return remove_unallowed_character(
            new_artist_unicode + " - " + new_title_unicode + " (" + new_creator + ") " + " [" + new_version_name + "].osu")

    def get_all_files_after_renaming(self):
        print("处理中: " + str(self.all_osu_after_renamed))
        all_audio = list(self.audio_name_dict.values())
        all_bgs = list(self.bg_dict.values())
        return self.all_osu_after_renamed + all_audio + all_bgs
