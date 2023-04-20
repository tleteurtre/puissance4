import cv2 as cv
import numpy as np

boule_img = cv.imread('attaqe.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('boule.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(boule_img, needle_img, cv.TM_CCOEFF_NORMED)

cv.imshow('Result',result)
cv.waitKey()