import requests
import os
import numpy as np
import cv2

def download_image(url, name='image.png'):
    if os.path.exists(name):
        return
    response = requests.get(url)
    with open(name, 'wb') as f:
        f.write(response.content)

url = 'https://wallpapersmug.com/download/3840x2160/db3578/naruto-anime-boy-art.jpg'
download_image(url, 'naruto4k.jpg')
im = cv2.imread('naruto4k.jpg')
# im = cv2.resize(im, (2000, 1200)) # resoulution given manually
im = cv2.resize(im, (0, 0), fx=0.25, fy=0.25) # resoulution given by factor
# print(im.shape)
bwim = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Naruto', im)
# cv2.imshow('Naruto BW', bwim)
# concating images
both = np.concatenate((im, cv2.cvtColor(bwim, cv2.COLOR_GRAY2BGR)), axis=0)
print(both.shape)
cv2.putText(both, 'original', (40, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(both, 'gray', (40, 60+540), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.rectangle(both, (10, 10),(180, 90), (0, 255, 0), 2)
cv2.imshow('Naruto', both)
cv2.waitKey(0)