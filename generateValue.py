import imageio
from selenium import webdriver
from time import sleep
import hashlib
import numpy as np

def change_to_be_hex(s):
   return int(s,base=16)


def function1():
    driver = webdriver.Chrome(executable_path=r'C:\Users\mateu\OneDrive\Pulpit\PS\chromedriver.exe')
    driver.get('https://www.twitch.tv')
    sleep(5)
    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()
    image = imageio.imread('screenshot.png')
    binaryImage = ''
    for i in image.ravel():
        binaryImage = binaryImage + f'{i:08b}'

    imageStep200 = ''
    counter = 0
    for i in binaryImage:
        counter = counter + 1
        if counter == 200:
            if i == '1':
                imageStep200 = imageStep200 + '0'
            elif i == '0':
                imageStep200 = imageStep200 + '1'
            counter = 0
        else:
            imageStep200 = imageStep200 + i

    MD5 = hashlib.md5(imageStep200.encode()).hexdigest()
    imageStep300 = ''
    counter = 0
    for i in binaryImage:
        counter = counter + 1
        if counter == 300:
            if i == '1':
                imageStep300 = imageStep300 + '0'
            elif i == '0':
                imageStep300 = imageStep300 + '1'
            counter = 0
        else:
            imageStep300 = imageStep300 + i

    allSHA = hashlib.sha256(imageStep300.encode()).hexdigest()
    SHA1 = allSHA[0:int(len(allSHA)/2)]
    SHA2 = allSHA[int(len(allSHA)/2):len(allSHA)]
    firstBlock = hex(int(SHA1, 16) ^ int(MD5, 16))
    secondBlock = hex(int(SHA2, 16) ^ int(MD5, 16))
    finalValue = firstBlock[2:] + secondBlock[2:]
    finalList = np.array([], dtype=np.uint8)
    for i in range(0, int(len(finalValue)/2)):
        #temp = finalValue[2*i:2*i+2]
        finalList = np.append(finalList, np.array([int(finalValue[2*i:2*i+2], 16)], dtype=np.uint8))
    with open('data.txt', 'ab') as f:
        np.save(f, finalList)