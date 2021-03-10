# @Author : 游永全
# @Date : 2021/3/10
# @Edition : Python3
# @System : Raspberry_Pi
from picamera import PiCamera
import time
import os

with PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    root = os.getcwd() + '/'
    camera.start_preview()
    time.sleep(5)
    date = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    path = root + date + '.jpg'
    camera.capture(path)
    print('已拍摄照片：' + date)
    camera.stop_preview()
