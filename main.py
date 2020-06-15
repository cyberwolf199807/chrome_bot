import pyautogui as pag;
from PIL import Image, ImageGrab
from numpy import asarray
import time
flag=0

def operation_up():
    pag.keyDown('Up')
def start():
    time.sleep(5)
def keep_track(image):
    data1=asarray(image)
    print(Image.fromarray(data1))
    print(data1)
def translate_image(data):
    for i in range(450,564):
        for j in range(225,270):
            data[i,j]=171
    return data
def collide(data):
    for i in range(457,574):
        for j in range(225,270):
            if(data[i,j]<100):
                print("***Up arrow key fired***")
                operation_up()
                return

def grayscale_picture():
    image=ImageGrab.grab().convert('L')
    data=image.load()
    data=translate_image(data)
    keep_track(image)
    
if __name__=="__main__":
    print("Dino auto Script will start in 5 sec")
    start()
    while "true":
        image=ImageGrab.grab().convert('L')
        keep_track(image)
        data=image.load()
        collide(data)


    
    
    
    

    
