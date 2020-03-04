# Osu-Collection-Formatter V.1.0.1

A small Python script to make Osu beatmap Collections in a quick and beautiful way.

一个快捷的Osu!整合软件，快速出合集。

## Preview: 
(Now fixed to this naming style. Custom style will be supported in the future.)
https://osu.ppy.sh/beatmapsets/1010028#mania/2114329

## Running

There are two ways of running this program: by compiling or by running the .exe directly. 

### By Compiling

Git clone or download as zip, extract all files and store it inside an empty folder, to make things easy, please don't included any irrelevant
files in this folder. Assume this folder is on your desktop, and its name is called packer. After this, move all the oszs that you want to pack into this folder, and then open cmd, type the following code
(Not the things in the brackets):

````
cd Desktop

cd packer

python3 main.py (If you are using MAC or Linux)

python main.py (If you are using Windows)

````
The program should jumps out and prompt you to type pack name and creator name. Just follows the instructions.

### By Running the .exe file

If running through exe, there is no need to download the .py files, just put all your oszs under the same directory with the .exe file. Still, to make things easy, please don't included any irrelevant
files in this folder. Then double click on the .exe and follow the instructions.

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
