# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:22:08 2017

@author: chandler
"""

from facepp import API, File, APIError;
import cv2
import os.path
import os
import numpy as np;

API_KEY = "JUyJI7RQ5C_3jZD-yRqZKJxt0uzrPlnp"
API_SECRET = "lj0RAeiwvRmn63O1Ap1EIB8RIuonDpFB"

def facepp_detect(api,img_path):
    result = api.detect(image_file = File(img_path),return_landmark=2,
                        return_attributes="gender,age,headpose,eyestatus,emotion,mouthstatus,eyegaze")
    return result['faces']
    
def batch_process(src_path,dst_path):
    api = API(API_KEY,API_SECRET);
    cnt = 0;
    for parent,dirnames,filenames in os.walk(src_path):
        filenames.sort();
        while (not len(filenames)==0):
            filename = filenames.pop();
            if (os.path.exists(os.path.join(dst_path,os.path.splitext(filename)[0]+'.npy'))):
                cnt = cnt+1;
                continue;
            try:
                result = api.detect(image_file = File(os.path.join(parent,filename)),return_landmark=2,
                                    return_attributes="gender,age,headpose,eyestatus,emotion,mouthstatus,eyegaze")
                np.save(os.path.join(dst_path,os.path.splitext(filename)[0]+'.npy'),result);
                cnt = cnt+1;
                print(cnt,filename)
#                dictionary = np.load(filename).item()
            except APIError, error:
                print(error.body);
                filenames.append(filename);
                
if __name__ == "__main__":
    source_path = '/home/tracking/work/src/caffe/Training_Evaluation_Dataset/train/256x256';
    dst_path = '/home/tracking/work/src/facepp_drowsy/train_info';
    batch_process(source_path,dst_path);