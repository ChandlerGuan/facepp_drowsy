# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:48:48 2017

@author: chandler
"""
from facepp import API, File
import cv2

API_KEY = "JUyJI7RQ5C_3jZD-yRqZKJxt0uzrPlnp"
API_SECRET = "lj0RAeiwvRmn63O1Ap1EIB8RIuonDpFB"

def facepp_detect(api,img_path):
    result = api.detect(image_file = File(img_path),return_landmark=2,return_attributes="gender,age")
    return result['faces']
    

if __name__ == "__main__":
    api = API(API_KEY,API_SECRET)
#    result = facepp_detect(api,'demo.jpeg')
    result = facepp_detect(api,'033_noglasses_nonsleepyCombination_000230.jpg')
    
    img = cv2.imread('033_noglasses_nonsleepyCombination_000230.jpg')
    for k,v in result[0]['landmark'].iteritems():
        cv2.circle(img,
                   (int(v['x']),
                    int(v['y'])),3,(0,255,0),-1);
    cv2.imshow("result",img);
    