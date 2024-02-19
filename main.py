import os
from pydub import AudioSegment


# 指定文件夹路径
input_file ="B:/music"
out_file = "C:/Users/Alargi/Desktop/music"

#获取需要处理的文件目录
list=[]
out_list= os.listdir(out_file)
input_list=os.listdir(input_file)
for item in input_list:
    if item[:-4]+'.mp3' not in out_list:
        list.append(item[:-4])

#转码部分
def convert_ogg_to_mp3(ogg_name, mp3_name):
    # 使用 AudioSegment 加载 Ogg 文件
    audio = AudioSegment.from_ogg(input_file+'/'+ogg_name+'.ogg')
    # 将音频文件导出为 MP3 格式
    audio.export(out_file +'/'+mp3_name+'.mp3', format="mp3")
l=len(list)
n=1
for item in list:
    print(f"({n} / {l}) Now processing{item}  \n")
    convert_ogg_to_mp3(item,item)
    n+=1
print('Done')
