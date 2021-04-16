#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from seperation import clean_results, break_characters

import easyocr
import cv2
import numpy as np


def clean(path, show=False):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.medianBlur(gray, 5)

    kernel = np.ones((5,5), np.uint8)
    alpha, beta = 1, 25

    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    if show:
        cv2.imshow("result", image)
        cv2.waitKey(0)
        cv2.destroyallwindows()
    # Save Result
    cv2.imwrite('temp.jpg', image)

def locate(image):
    reader = easyocr.Reader(['en'], gpu=False)
    return reader.readtext(image)

def draw_boxes(result, image):
    for detection in result:
        #  top_left = tuple([int(val) for val in detection[1][0]])
        #  bottom_right = tuple([int(val) for val in detection[1][2]])
        top_left = (detection[1][0][0], detection[1][0][1])
        bottom_right = (detection[1][2][0], detection[1][2][1])
        midpoint = detection[2]
        text = detection[0]
        if text.lower() == 'u' or text.lower() == 'k':
            continue

        font = cv2.FONT_HERSHEY_SIMPLEX
        image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        image = cv2.putText(image, text, midpoint, font, 3, (255, 0, 0), 3, cv2.LINE_AA)
        #  image = cv2.putText(image, str((top_left, bottom_right)), top_left, font, 2, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

IMAGE_PATH = 'images/methanol2.jpg'

#  clean(IMAGE_PATH)
#  result = locate('temp.jpg')
#  print(result)
#  result = [([[1444, 134], [1703, 134], [1703, 433], [1444, 433]], 'H', 0.8577108091616061), ([[1503, 722], [1643, 722], [1643, 959], [1503, 959]], 'U', 0.1177254299524435), ([[81, 1193], [430, 1193], [430, 1597], [81, 1597]], 'H', 0.35081935800930353), ([[1383, 1232], [1665, 1232], [1665, 1584], [1383, 1584]], 'C', 0.6188473903267209), ([[2435, 1246], [2735, 1246], [2735, 1601], [2435, 1601]], 'H', 0.9541214036289603), ([[1447, 1916], [1607, 1916], [1607, 2129], [1447, 2129]], 'U', 0.03177076760090913), ([[1337, 2436], [1609, 2436], [1609, 2740], [1337, 2740]], 'H', 0.9752844739384869)]
result = [([[327, 277], [419, 277], [419, 515], [327, 515]], 'H', 0.5169475173293883), ([[32, 604], [130, 604], [130, 714], [32, 714]], 'H', 0.8897842079336193), ([[193, 577], [671, 577], [671, 713], [193, 713]], '~(-h', 0.45371490716934204), ([[300, 892], [458, 892], [458, 1006], [300, 1006]], 'Oh', 0.3088542355854099)]

clean = clean_results(result)
data = break_characters(clean)
for i in data:
    print(i)

image = cv2.imread('temp.jpg')
draw_boxes(data, image)

