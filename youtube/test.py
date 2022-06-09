import cv2
import pytessaract
pytesseract.pytesseract.tesseract_cmd = '/home/romain/anaconda3/lib/python3.9/site-packages/pytesseract/tesseract'

img = cv2.imread('yourimage.jpeg')   

text = pytessaract.image_to_string(img)