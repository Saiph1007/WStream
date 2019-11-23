from ffmpeg import *
import sys
if __name__ == '__main__':
    audio, video =None, None
    ff = None
    while True:
        print('1. device list, 2. streaming start, 3.streaming stop 4. terminate')
        command = int(input('command : '))
        
        if command == 1:
            audio, video = device_list()
            if not len(audio):
                print('not found audio devices...\n')
            else:
                print('Audio devices')    
                for i in range(len(audio)):
                    print('%d : %s\n' %(i, audio[i]))
            if not len(video):
                print('not found video devices...\n')
            else:
                print('Video devices')    
                for i in range(len(video)):
                    print('%d : %s\n' %(i, video[i]))

        if command == 2:
            print('streaming start\n')
            if audio == None or video == None:
                print('Plase check device list')
                continue
            ff = FFmpeg(accelerator='ndivia', audio=2, audio_devices=audio, video_devices=video)
            ff.start()
        if command == 3:
            print('streaming stop\n')
            ff.terminate()
        
        if command == 4:
            print('program terminate...\n')
            break