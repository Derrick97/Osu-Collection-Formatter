import os
import zipfile
from Utils import Utils
if __name__ == '__main__':
    u = Utils(os.getcwd())
    oszs = u.find_osz_files()
    print("------------------Made in Love From Wensi v.1.0.1------------------")
    print("请保证想要成包的所有歌曲osz都在本程序同一文件夹下。")
    print("Please make sure all oszs that you want to pack together is in the same directory as this program.")
    collection_name = input("输入新的包名(The Pack Name)：")
    creator = input("请输入作者名(The Creator Name)：")
    collection_artist = "Various Artists"
    all_files = []
    print("少狼祈祷中...Loading...")
    success = True
    for osz in oszs:
        zip = zipfile.ZipFile(osz)
        all_file_names = zip.namelist()
        zip.extractall()
        all_diffs = u.get_all_osu_diffs(all_file_names)
        u.all_osu = all_diffs
        u.get_all_bg(all_file_names)
        for diff in all_diffs:
            try:
                u.rename_osz_metadata(diff, collection_name, collection_name, collection_artist, collection_artist, creator)
            except ValueError:
                print("Rolling Back..")
                print("回滚操作中...")
                for file in all_files:
                    os.remove(file)
                success = False
                break
        if not success:
            break
        u.change_audio_file_name()
        all_files += u.get_all_files_after_renaming()
        u.reset()
    if success:
        zip = zipfile.ZipFile(collection_name+".osz", mode='w')
        for file in all_files:
            zip.write(file)
            os.remove(file)
        print("Success! Saved as " + collection_name + ".osz in the current directory.")
        print("整合成功！已保存为 " + collection_name + ".osz并存放在当前文件夹下。")
    else:
        print("Fail, please fix according to the error info, or directly contacts Derrickwolf@outlook.com.")
        print("出包失败，请按错误信息修复，或者联系Derrickwolf@outlook.com.")
    x = input("Press Any Key To Continue...按任意键并回车退出程序。")


