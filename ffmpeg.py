import os
import sys
import subprocess as sub
from multiprocessing import Process
import multiprocessing
import logging 
 
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(logging.NullHandler())

# ch = logging.StreamHandler(logging.NullHandler)
# logger.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
# logger.addHandler(ch)
class FFmpeg():
    def __init__(self, resolution='1920x1080', audio=0, video=0,
                 time=-1, accelerator='', video_devices=[], audio_devices=[], output='http://121.158.56.113:8181/out.m3u8'):
        self.command = 'ffmpeg -y '

        self.isNdivia = False
        self.isIntel = False
        if time != -1:
            self.command += '-t %s ' %(time)

        if accelerator == 'ndivia':
            self.command += '-hwaccel cuvid '
            self.isNdivia = True

        self.command += '-f gdigrab -offset_x 0 -offset_y 0 -video_size %s -r 60 -draw_mouse 1 -i desktop ' %(resolution)

        self.command += '-f dshow -i audio '

        if self.isNdivia:
            self.command += '-c:v h264_nvenc '
        self.command += '-hls_time 10 -hls_list_size 0 '
                    
        self.command += output
        print(self.command)
        self.args = self.command.split(' ')
        for i in range(len(self.args)):
            if not self.args[i].find('audio'):
                self.args[i] = 'audio=%s' %(audio_devices[audio])
        print(self.args)


    def start(self):
        self.proc = sub.Popen(self.args)
        
    def terminate(self):
        self.proc.terminate()
    def overlay(self):
        pass


def systemCall(command):
    os.system(command)
    sys.stdout = open('test.txt', 'w')
    print('os pid : ',os.getpid)

def device_list():

    audio = False
    video = False
    temp_audio_devices = []
    audio_devices = []
    temp_video_devices = []
    video_devices = []

    result, file_name = find_log()
    if result:
        os.remove(file_name)
    command = 'ffmpeg -report -list_devices true -f dshow -i dummy'
    try:
        sub.call(command, stdout=sub.PIPE, stderr=sub.STDOUT)
    except Exception as e:
        print(e)
    result, file_name = find_log()
    if not result:
        return [], []
    f = open(file_name, encoding='utf-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        if line.find('dummy: Immediate exit requested') >= 0:
            break
        if not video:
            if line.find('DirectShow video devices') >= 0:
                video = True
                continue
        else:
            if not audio:
                if line.find('DirectShow audio devices') >= 0:
                    audio = True
                    continue
                else:
                    temp_video_devices.append(line)
            else:
                temp_audio_devices.append(line)
    for device in temp_audio_devices:
        if device.find('"') >= 0 and device.find('Alternative name') <= 0:
            start_index = device.find('"')
            audio_devices.append(device[start_index + 1:-2])
    for device in temp_video_devices:
        if device.find('"') >= 0 or device.find('Alternative name') >= 0:
            start_index = device.find('"')
            video_devices.append(device[start_index + 1:-2])
    return audio_devices, video_devices


def find_log():
    file_list = os.listdir(os.getcwd())
    log = None
    for file_name in file_list:
        if file_name.find('.log') >= 0:
            log = file_name
    if log == None:
        return False, ''
    return True, log
