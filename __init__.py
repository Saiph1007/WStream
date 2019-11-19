import os
import sys 
import subprocess as sub

# test = 'ffmpeg -y -rtbufsize 100M -f gdigrab -framerate 30 -probesize 10M -draw_mouse 1 -i desktop -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p "output.mp4"'
# test = 'ffmpeg -f dshow -i audio="Microphone (Realtek High Definition Audio)" D:\Audio\output.mp3'
test = 'ffmpeg -list_devices true -f dshow -i -re "http://127.0.0.1:6000"'

# test = 'ffmpeg -f dshow -i audio="%s" -acodec libmp3lame -t 10 out.mp3' %('temp)')
# test = 'ffmpeg -f dshow -i audio="virtual-audio-capturer":video="screen-capture-recorder" yo.mp4'
# ndivia = 'ffmpeg -y -t 10 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -draw_mouse 1 -i desktop -preset llhq -tune zerolatency -c:v h264_nvenc -r 60 out.mp4'
# intel = 'ffmpeg -y -t 10 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -probesize 10M -draw_mouse 1 -i desktop -c:v h264_qsv -r 60 -preset veryfast -tune zerolatency -crf 25 output.mp4'


def intel_recording(output_path):
    intel = 'ffmpeg -y -t 30 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -probesize 10M -draw_mouse 1 -i desktop -map 0 -c:v h264_qsv -r 60 -preset veryfast -tune zerolatency -crf 25 ' + output_path
    args = intel.split(' ')
    ret = sub.call(args)
    

def ndivia_recording(output_path):
    ndivia = 'ffmpeg -y -t 20 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -draw_mouse 1 -i desktop -preset llhq -tune zerolatency -c:v h264_nvenc -r 60 ' + output_path
    args = ndivia.split(' ')
    ret = sub.call(args)

def device_list():
    device = 'ffmpeg -list_devices true -f dshow -i dummy'
    args = device.split(' ')
    try:
        ret = sub.check_output(args,stdin=None, stderr=None, shell=False, )
    except sub.CalledProcessError as e:
        print('error')
    # print('ret :',ret)

# test = 'ffmpeg -re -i out.mp4 -f rtsp -rtsp_transport tcp rtsp://localhost:8888/live.sdp'
# test = 'ffmpeg -re -i out.mp4 -f hls http://localhost:8181/test.mp4'
test = 'ffmpeg -re -i out.mp4 -f rtsp -rtsp_transport tcp rtsp://localhost:8181/live.sdp'
    
if __name__ == '__main__':
    args = test.split(' ')
    # for i in range(len(args)):
    #     if not args[i].find('audio'):
    #         args[i] = 'audio="스테레오 믹스(Realtek(R) Audio)"'
    #     print(args[i])
    # device_list()
    intel_recording('http://localhost:8181/test.m3u8')
    # ret = sub.call(args)
    # print(ret)