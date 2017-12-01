# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:45:00 2017

@author: chandler
"""
import os;
import os.path;
import cv2;

video_folder = '/home/tracking/work/src/facepp_drowsy/video/';
image_folder = '/home/tracking/work/src/facepp_drowsy/image/';

print_interval = 5;

if __name__ == "__main__":
    if not os.path.exists(image_folder):
        os.makedirs(image_folder);
    for parent,dirnames,filenames in os.walk(video_folder):
        for video_name in filenames:
            print("processing video: "+video_name);
            video = cv2.VideoCapture(os.path.join(parent,video_name));
            frame_cnt = 0;
            print_cnt = 0;
            while (True):
                flag,frame = video.read();
                if (not flag):
                    break;
#                print(os.path.join(image_folder,os.path.splitext(video_name)[0]+'_{:0>5d}'.format(frame_cnt)+'.jpg'))
                if (print_cnt%print_interval==0):
                    cv2.imwrite(os.path.join(image_folder,os.path.splitext(video_name)[0]+'_{:0>5d}'.format(frame_cnt)+'.jpg'),frame);
                frame_cnt = frame_cnt + 1;
                print_cnt = print_cnt + 1;