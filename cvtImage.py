# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:45:00 2017

@author: chandler
"""
import os;
import os.path;
from cv2 import VideoCapture,imwrite;

video_folder = os.getcwd();
image_folder = os.path.join(os.getcwd(),'image');

#video_folder = '/home/tracking/work/src/facepp_drowsy/video/';
#image_folder = '/home/tracking/work/src/facepp_drowsy/image/';

print_interval = 5;

if __name__ == "__main__":
    if not os.path.exists(image_folder):
        os.makedirs(image_folder);
    for parent,dirnames,filenames in os.walk(video_folder):
        for video_name in filenames:
            print("processing video: "+video_name);
            video = VideoCapture(os.path.join(parent,video_name));
            if not os.path.exists(os.path.join(image_folder,os.path.splitext(video_name)[0])):
                os.makedirs(os.path.join(image_folder,os.path.splitext(video_name)[0]));
            frame_cnt = 0;
            while (True):
                flag,frame = video.read();
                if (not flag):
                    break;
#                print(os.path.join(image_folder,os.path.splitext(video_name)[0]+'_{:0>5d}'.format(frame_cnt)+'.jpg'))
                if (frame_cnt%print_interval==0):
                    imwrite(os.path.join(image_folder,os.path.splitext(video_name)[0],os.path.splitext(video_name)[0]+'_{:0>5d}'.format(frame_cnt)+'.jpg'),frame);
                frame_cnt = frame_cnt + 1;
