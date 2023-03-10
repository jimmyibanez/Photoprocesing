import numpy as np
import cv2
import math
import imutils
from os import listdir
from os.path import join

def procesarImagen(path, name):

  faces = []
  if (len(faces) == 0):
    face_cascade = cv2.CascadeClassifier(r'haarcascades/haarcascade_frontalface_alt.xml')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  if (len(faces) == 0):
    face_cascade = cv2.CascadeClassifier(r'haarcascades/haarcascade_frontalface_alt2.xml')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  if (len(faces) == 0):
    face_cascade = cv2.CascadeClassifier(r'haarcascades/haarcascade_frontalface_alt_tree.xml')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  if (len(faces) == 0):
    face_cascade = cv2.CascadeClassifier(r'haarcascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  if (len(faces) == 0):
    img = cv2.imread(path)
    # height = 379
    width = 319
    # res = cv2.resize(img,(width, height), interpolation = cv2.INTER_CUBIC)
    res = imutils.resize(img, width)
    # res = imutils.resize(gray, width)
    resName = 'notFound/{}.jpg'.format(name)
    cv2.imwrite(resName, res)
  
  if (len(faces)>1):
    index = 0
    i = 0
    max = 0
    for (x,y,w,h) in faces:
      if (w > max):
        max = w
        index = i
      i += 1
    faces = [faces[index]]

  for (x,y,w,h) in faces:
      h = w *4.5/3.5
      x1 = math.floor(x-w*0.25)
      x2 = math.floor(x+w*1.25)
      y1 = math.floor(y-h*0.25 - h*0.15)
      y2 = math.floor(y+h*1.25 - h*0.15)
      if (y2 >= height):
        y2 = height - 1
        y1 = height - y2 + y1 if height - y2 + y1 > 0 else 0
      if (x2 >= width):
        x2 = width -1
        x1 = x1 if x1 > 0 else 0
      if (x1 < 0):
        x1 = 0
        x2 = x2 - x1 if x2 - x1 < width else width - 1
      if (y1 < 0):
        y1 = 0  
        y2 = y2 - y1 if y2 - y1 < height else height - 1
      if ( y2 - y1 > 4.5*(x2 - x1)/3.5):
        value = y2 - y1 - (x2 - x1)*4.5/3.5
        up = math.floor(value / 2)
        down = math.ceil(value / 2)
        y2 -= up
        y1 += down

with open("data.txt", "r") as fin:
  rows = (line.strip('\n').split(None, 1) for line in fin)
  d = {row[0]: row[1] for row in rows}

for i in d:
  try:
    imgOrigin = 'origin/{}'.format(i)
    print(imgOrigin)
    print(d.get(i))
    procesarImagen(imgOrigin, d.get(i))
  except Exception as inst:
    print(inst)