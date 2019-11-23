import os
import subprocess as sub
from multiprocessing import Process

class FFmpeg():
    def __init__(self, resolution='1920x1080', audio=-1, camera=False,
                 time=-1, accelerator='', output='C:/public/out.avi'):
        self.command = 'ffmpeg -y '
        self.isNdivia = False
        self.isIntel = False
        self.video_devices, self.audio_devices = device_list()
        if time != -1:
            self.command += '-t %s ' %(time)

        if accelerator == 'ndivia':
            self.command += '-hwaccel cuvid '
            self.isNdivia = True

        self.command += '-f gdigrab -offset_x 0 -offset_y 0 -video_size %s -framerate 60 -draw_mouse 1 -i desktop ' %(resolution)

        self.command += '-f dshow -i audio="%s" ' % (self.audio_devices[audio])

        if self.isNdivia:
            self.command += '-c:v h264_nvenc '
                    
        self.command += output

    def start(self):
        self.proc = Process(target=systemCall, args=(self.command,))
        self.proc.start()
    def terminate(self):
        self.proc.terminate()
    def overlay(self):
        pass


def systemCall(command):
    try:
        os.system(command)
    except Exception as e:
        print('error :', str(e))

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
        sub.call(command.split(' '))
    except Exception as e:
        print(e)
    result, file_name = find_log()
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
