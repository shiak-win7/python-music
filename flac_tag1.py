#coding:utf-8
import sys, os
from mutagen.flac import FLAC
import glob

class Mutagen_Getfolder:

  def get_foldername(self, foldername):

    target_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = target_path + '\\' + foldername + '\\*.flac'

    music_files = glob.glob(target_folder)
    album_data = FLAC(music_files[0])
    print('+-------------------------+')
#    print(album_data.tags.keys())
#    print(album_data.info.length)
    print(album_data["album"]) 
    print(album_data["artist"])
    print(album_data["genre"]) 
    print(album_data["date"])
    print('+-------------------------+')

    for music_data in music_files:
    	music = FLAC(music_data)
    	print(os.path.basename(music_data))
    	print(music["tracknumber"], music["title"])
    	print("")
    	
if __name__ == '__main__':
  args = sys.argv
  if len(args) == 1:
    print('I need a folder name for argment.')
  else:
    mg = Mutagen_Getfolder
    mg.get_foldername(*sys.argv)
