# Osu-Collection-Formatter V.1.0.3

A small Python script to make Osu beatmap Collections in a quick and beautiful way.

一个快捷的Osu!整合软件，快速出合集。

## Preview: 
(Now fixed to this naming style, only support custom pack name and custom creator name. Custom style will be supported in the future.)
https://osu.ppy.sh/beatmapsets/1010028#mania/2114329  
**V1.0.3 New: When bg used in .osu file is not found in the osz, the program will now warn the user and continue instead of terminate the program.** 

## Running

There are two ways of running this program: by compiling or by running the .exe directly. 

### By Compiling (Slightly Complex, used for debug)

Git clone or download as zip, extract all files and store it inside an empty folder, to make things easy, please don't included any irrelevant
files in this folder. Assume this folder is on your desktop, and its name is called packer. After this, move all the oszs that you want to pack into this folder, and then open cmd (or terminal in the context of Linux), type the following code
(Not the things in the brackets):

````
cd Desktop

cd packer

python3 main.py (If you are using MAC or Linux)

python main.py (If you are using Windows)

````
The program should jumps out and prompt you to type pack name and creator name. Just follows the instructions.

### By Running the .exe file (Easy and Straightforward)

If running through exe, there is no need to download the .py files, just put all your oszs under the same directory with the .exe file. Still, to make things easy, please don't included any irrelevant files in this folder. Then double click on the .exe and follow the instructions. 

Any unknown or not understandable errors, please directly contact derrickwolf@outlook.com.

## Supports:

  1. Reserve all corresponding BGs.
  
  2. Supports packing the the difficulties under the same mapset with different audio files. Example: https://osu.ppy.sh/beatmapsets/292994#mania/659237
 
  3. Supports packing normal songs.

## Not Support

  1. Will not reserve hitsounds when packing. Please refrain from using this on ranked maps, unless you can endure with playing with no hitsound.

## Caveat

  1. This program has only been tested on **Mania** files, there is no gurantte that it will also work on other modes.
  
  2. Please always has unicode and romanised name or there may be unexpected errors.
  
  3. Please make sure all bgs mentions in the .osu files are presented in the original osz, or the program will warn you that the bg cannot be found and will rollback all the operations.
  
  4. If packing songs fails or packing songs with hitsound, there will be some left over files for now (Which will be fixed in the future). For now please delete the left over files by hand.
  
## Future

  1. Add full support for different modes.
  
  2. Unpack all files in a separate folder when operating which is more neat.
  
  3. Rollback in a neat way. (Aims to fix caveat 4.)
  
  4. Custom version name style.
  
  5. Import difficulty list so that the difficulties can be displayed in the version name. (i.e the manually written difficulty, such as Lv.10, etc, not the star rating.)
  
  --------------------------------------------------------------------------------------------------------------------------------
  
## 预览：
https://osu.ppy.sh/beatmapsets/1010028#mania/2114329
注意：现在默认格式如此osz所示，只支持自定义作图者以及合集名称。更多自定义样式功能将在下一版本添加。   
**V1.0.3新功能：如果.osu中引用的背景图未被包含在osz中，则程序会提醒用户并完成做包，而不会显示中止操作。**

## 运行
此程序运行有两种方式：通过.py文件运行（需要python3或以上）或者通过.exe可执行文件运行（需要Windows）。

### 通过.py文件(略复杂，建议开发者使用，可以用于debug)
git clone 或者打包下载此目录， 解压后存放至任意空文件夹。假设此文件夹存放在桌面，并且叫做packer。此时请将所有想要整合的osz全部放在此文件夹内，并打开命令提示符，然后输入以下代码。不需要输入括号内内容。

````
cd Desktop 

cd packer （如何cd到当前文件夹请百度或者谷歌，此处只是用windows举例。）

python3 main.py (If you are using MAC or Linux)

python main.py (If you are using Windows)

````

### 通过.exe运行 (简单直接，但是需要Windows)

如果决定使用exe运行，则不需下载.py文件，也不需要安装python。直接将所有需要的osz和这个exe后缀名文件放进一个空文件夹，然后双击exe运行，按照指示即可。此状态下如果发现了看不懂的报错请直接联系Derrickwolf@outlook.com。

## 已支持功能
除开打包正常歌曲以外，还支持打包同谱面下带有差分音源的谱面，例如Fullerene-的马里奥： https://osu.ppy.sh/beatmapsets/292994#mania/659237 。
同样支持不同难度使用不同封面，所有封面都会照旧保留。

## 不支持功能
如果尝试打包代有key音或者hitsound的谱面，hitsound和key音都不会被保留。所以如果想要打包rank谱面，必须忍受没有hitsound。

## 特别注意

1. 本软件只在mania模式下测试过，暂时不保证其他模式可用，未来会逐渐完整支持。

2. 请保证每个osz里面都包含所有需要使用的背景图，否则会提示谱面背景图片找不到，并会导致出包失败。

3. 如果强行想打包带有key音/hitsound的图，或者打包因为某些原因失败，目前会残留一些osz中处理失败的文件，请暂时手动删除后再尝试修复错误再使用这个软件。 以后会添加自动删除所有错误文件的功能。

## 未来可能添加的功能

1. 全模式支持。

2. 使用分离文件夹解压osz，防止残留文件难以删除。

3. 更完整的回滚操作。

4. 自定义难度命名方式。

5. 导入难度列表并显示在难度名内。
