import os
import sys 
import subprocess as sub

# test = 'ffmpeg -y -rtbufsize 100M -f gdigrab -framerate 30 -probesize 10M -draw_mouse 1 -i desktop -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p "output.mp4"'
# test = 'ffmpeg -y -t 10 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 2560x1440 -framerate 60 -draw_mouse 1 -i desktop -preset llhq -tune zerolatency -c:v h264_nvenc -r 60 out.mp4'
# test = 'ffmpeg -f dshow -i audio="Microphone (Realtek High Definition Audio)" D:\Audio\output.mp3'
# test = 'ffmpeg -list_devices true -f dshow -i dummy'
# test = 'ffmpeg -f dshow -i audio="%s" -acodec libmp3lame -t 10 out.mp3' %('temp)')
test = 'ffmpeg -i stereo.flac -ac 1 mono.flac'
# test = 'ffmpeg -f dshow -i audio="virtual-audio-capturer":video="screen-capture-recorder" yo.mp4'


if __name__ == '__main__':
    args = test.split(' ')
    # for i in range(len(args)):
    #     if not args[i].find('audio'):
    #         args[i] = 'audio="스테레오 믹스(Realtek(R) Audio)"'
    #     print(args[i])
    ret = sub.call(args)
    print(ret)