import os
import sys 
import subprocess as sub

# test = 'ffmpeg -y -rtbufsize 100M -f gdigrab -framerate 30 -probesize 10M -draw_mouse 1 -i desktop -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p "output.mp4"'
# test = 'ffmpeg -f dshow -i audio="Microphone (Realtek High Definition Audio)" D:\Audio\output.mp3'
# test = 'ffmpeg -list_devices true -f dshow -i -re "http://127.0.0.1:6000"'

# test = 'ffmpeg -y -f dshow -i audio -acodec libmp3lame out.mp3'

# test = 'ffmpeg -f dshow -i audio="virtual-audio-capturer":video="screen-capture-recorder" yo.mp4'
# ndivia = 'ffmpeg -y -t 10 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -draw_mouse 1 -i desktop -preset llhq -tune zerolatency -c:v h264_nvenc -r 60 out.mp4'
# intel = 'ffmpeg -y -t 10 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -probesize 10M -draw_mouse 1 -i desktop -c:v h264_qsv -r 60 -preset veryfast -tune zerolatency -crf 25 output.mp4'
# test = 'ffmpeg -f dshow -i audio out.mp4'

# test = 'ffmpeg -y -i out.mp3 -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -draw_mouse 1 -i desktop -c:v h264_nvenc -r 60 out.mp4'
# ffmpeg -y -i D:/public/output.avi -i D:/python_project/WStream/out.mp4 -filter_complex "overlay=W-w-100:H-h-100" D:/public/test.avi

# ffmpeg -y -i D:/python_project/WStream/out.mp4 -i D:/public/output.avi -filter_complex "[1]scale=400:300[ovrl];[0][ovrl]overlay=W-w-5:H-h-5:shortest=1[v]" -c:v h264_nvenc -max_muxing_queue_size 1024 -map "[v]" -map 1:a -c:a copy D:/public/test.avi

# ffmpeg -y -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 2560x1440 -framerate 60 -draw_mouse 1 -r 60 -i desktop -f dshow -i audio="Stereo mix(Realtek(R) Audio)" D://public/output.avi
# ffmpeg -f gdigrab -framerate ntsc -video_size 1920x1080 -i desktop  -f dshow -i audio="Stereo mix(Realtek(R) Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast D:\public\output.avi
def intel_recording(output_path):
    intel = 'ffmpeg -y -t 30 -rtbufsize 100M -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -probesize 10M -draw_mouse 1 -i desktop -map 0 -c:v h264_qsv -r 60 -preset veryfast -tune zerolatency -crf 25 ' + output_path
    args = intel.split(' ')
    ret = sub.call(args)
    

def ndivia_recording(output_path):
    # ndivia = 'ffmpeg -y -hwaccel cuvid -c:v h264_cuvid -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -r 60 -draw_mouse 1 -i desktop -qp 30 -f dshow -i audio -r 60 -c:v h264_nvenc -map 0:v -map 1:a: ' + output_path
    ndivia = 'ffmpeg -y -hwaccel cuvid -f gdigrab -offset_x 0 -offset_y 0 -video_size 1920x1080 -framerate 60 -draw_mouse 1 -i desktop -f dshow -i audio -c:v h264_nvenc ' + output_path
    args = ndivia.split(' ')
    for i in range(len(args)):
        if not args[i].find('audio'):
            args[i] = 'audio=Stereo mix(Realtek(R) Audio)'
    print(str(args))
    ret = sub.call(args)

def device_list():
    device = 'ffmpeg -report -list_devices true -f dshow -i dummy'
    args = device.split(' ')
    try:
        ret = sub.check_output(args,stdin=None, stderr=None, shell=False, )
    except sub.CalledProcessError as e:
        print('error')
    # print('ret :',ret)

def audio_recording(output_path):
    pass
# test = 'ffmpeg -re -i out.mp4 -f rtsp -rtsp_transport tcp rtsp://localhost:8888/live.sdp'
# test = 'ffmpeg -re -i out.mp4 -f hls http://localhost:8181/test.mp4'
# test = 'ffmpeg -re -i out.mp4 -f rtsp -rtsp_transport tcp rtsp://localhost:8181/live.sdp'
# test = 'ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -c:v libx264 -crf 0 -preset ultrafast output.mkv'
# test = 'ffmpeg -list_devices true -f dshow -i dummy'

if __name__ == '__main__':
    # args = test.split(' ')
    # print(args)
    # for i in range(len(args)):
    #     if not args[i].find('audio'):
    #         args[i] = 'audio=Stereo mix(Realtek(R) Audio)'
        # print(args[i])
    # print('args :', args)
    device_list()

    # ndivia_recording('http://121.158.56.113:8181/out.m3u8')
    # ndivia_recording('test.mp4')
    # ret = sub.call(args)
    # print(ret)