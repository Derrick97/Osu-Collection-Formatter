import os
import zipfile
import sys
import tempfile
from Utils import Utils

if __name__ == '__main__':

    print("------------------Made in Love From Wensi v.1.0.2------------------")
    print("Please make sure all oszs that you want to pack together are in the same directory as this program.")
    print("请保证想要成包的所有歌曲osz都在本程序同一文件夹下。")

    print("读取本地osz中....Scanning for oszs...")
    u = Utils(os.getcwd())
    oszs = u.find_osz_files()
    if len(oszs) == 0:
        print("No oszs found in the current directory, please retry")
        print("未找到任何osz,请将想要成包的osz放在同文件夹下后再试。")
        input("Press Enter To Continue...按回车退出程序。")
        sys.exit()
    print(str(len(oszs)) + " osz(s) found.")
    print("找到" + str(len(oszs)) + "个osz。")
    collection_name = input("输入新的包名(The Pack Name)：")
    creator = input("请输入作者名(The Creator Name)：")
    collection_artist = input("请输入作曲者名,不输入则默认为Various Artists(The Artist Name, press enter to use default: Various Artists)：")
    if not collection_artist:
        collection_artist = "Various Artists"
    all_files = []
    print("少狼祈祷中...Loading...")





    success = True

    f = tempfile.TemporaryDirectory(dir=os.getcwd())
    print(f.name)

    u.path = f.name + "\\"

    try:
        for osz in oszs:
            zip = zipfile.ZipFile(osz)
            all_file_names = zip.namelist()
            zip.extractall(u.path)
            all_diffs = u.get_all_osu_diffs(all_file_names)
            u.all_osu = all_diffs
            u.get_all_bg(all_file_names)
            for diff in all_diffs:
                u.rename_osz_metadata(diff, collection_name, collection_name, collection_artist, collection_artist, creator)
            u.change_audio_file_name()
            all_files += u.get_all_files_after_renaming()
            u.reset()
    except:
        print("Fail, please fix according to the error info, or directly contacts Derrickwolf@outlook.com.")
        print("出包失败，请按错误信息修复，或者联系Derrickwolf@outlook.com.")

    zip = zipfile.ZipFile(collection_name+".osz", mode='w')
    for file in all_files:
        zip.write(u.path + file, file)

    print("Removing tmp folder...")
    print("清理中...")
    try:
        f.cleanup()
        print("tmp folder removed.")
        print("临时文件夹删除成功。")
    except:
        print("Failed to remove tmp folder.")
        print("临时文件夹删除失败。")
    print("Success! Saved as " + collection_name + ".osz in the current directory.")
    print("整合成功！已保存为 " + collection_name + ".osz并存放在当前文件夹下。")

    x = input("Press Enter To Continue...按回车退出程序。")

