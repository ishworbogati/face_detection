# Face_Detection
Detecting faces in images using Open CV and Haar Cascades.

This requires Open CV, Python, Haar Cascades training data and suitable OS platform (Mac, Linux or Windows). For specific version please check vendor websites for the latest.

I used Python 2.7.14 on a test machine running Windows 7 Professional (i3 2.1 GHz Arrandale).
To determine which version of Python you have installed, type the following on your terminal or command prompt:

python --version

OpenCV 3.4.3 was used with this project, suitable for Python 2.7.14. To determine if you have properly installed OpenCV, type the following from the python command line:

import cv2


Steps:
1. Load a image 
2. convert it to RBG
3. Load haarcascade file for face recognition
4. Apply it using sliding window menthod
5. apply a square box for detected area
6. display on original image
