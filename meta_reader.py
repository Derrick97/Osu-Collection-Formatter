import os

class osu_file:
    def __init__(self, file, f=None, archive_source=None):
        if not f and not archive_source:
            self.directory = os.path.dirname(file)
        else:
            self.directory = None
        self.title = ""
        self.roman_title = ""
        self.artist = ""
        self.artist_unicode = ""
        self.creator = ""
        self.version = ""
        self.audio_file = ""
        self.beatmap_id = ""
        self.beatmap_set_id = ""
        self.bg_events = []
        self.bg_name = ""
        self.beat_objs = []
        self.init_error = self.init_from_file(file, f, archive_source)
        self.level = None

    # Check if mp3 / bgs are presented.
    def check_source(self, archive_source):
        if not archive_source:
            audio_file = os.path.join(self.directory, self.audio_file)
            if not os.path.exists(audio_file):
                return "Audio Missing."
            if len(self.bg_name) > 0:
                bg_file = os.path.join(self.directory, self.bg_name)
                if not os.path.exists(r'%s' % bg_file):
                    return "BG Missing."
        else:
            file_list = archive_source.namelist()
            if self.audio_file not in file_list:
                return "Audio Missing."
            if len(self.bg_name) > 0 and self.bg_name not in file_list:
                return "BG Missing"
        return ""




    def init_from_file(self, osu_file_name, f=None, archive_source=None):
        bg_last_line_index = -2
        obj_start = False
        if f is None:
            f = open(osu_file_name, "r+", encoding='utf-8')
        for i, line in enumerate(f):
            if "AudioFilename:" in line:
                self.audio_file = line[15:].strip("\n")
            elif "Title:" in line:
                self.title = line[6:].strip("\n")
            elif "TitleUnicode:" in line:
                self.roman_title = line[13:].strip("\n")
            elif "Artist:" in line:
                self.artist = line[7:].strip("\n")
            elif "ArtistUnicode:" in line:
                self.artist_unicode = line[14:].strip("\n")
            elif "Creator:" in line:
                self.creator = line[8:].strip("\n")
            elif "Version:" in line:
                self.version = line[8:].strip("\n")
            elif "BeatmapID:" in line:
                self.beatmap_id = "BeatmapID:0" + "\n"
            elif "BeatmapSetID:" in line:
                self.beatmap_set_id = "BeatmapSetID:-1" + "\n"
            elif "//Background and Video events" in line:
                self.bg_events.append(line)
                bg_last_line_index = i
            elif i == bg_last_line_index + 1:
                if line[0] == "/":
                    continue
                    # line_list.append(line)
                else:
                    self.bg_name = line.split(",")[2][1:-1]
            elif "[HitObjects]" in line:
                obj_start = True
            else:
                if obj_start:
                    self.beat_objs.append(line)
        return self.check_source(archive_source)

# Test Use only.
if __name__ == '__main__':
    file = r"E:\osu!\Songs\beatmap-637911133123973570-Crazy cinema story\chroma - Crazy cinema story (Imperial Wolf) [String Quartet].osu"
    f = osu_file(file)
    print(f.beat_objs[:10])