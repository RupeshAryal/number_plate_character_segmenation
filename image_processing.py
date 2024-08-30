import cv2 as cv
from utils import list_of_character_classes


import numpy as np

def image_preprocessing(image_path = None, image = None):
  if image_path:
     image = cv.imread(image_path)

  height, width = image.shape[:2]

  crop_top = int(0.1 * height)
  crop_bottom = int(0.9 * height)
  crop_left = int(0.0 * width)
  crop_right = int(1 * width)

  # Crop the image
  cropped_image = image[crop_top:crop_bottom, crop_left:crop_right]

  
  # increasing the contrast of the image using histogram equilization
  lab = cv.cvtColor(cropped_image, cv.COLOR_BGR2LAB)
  l_channel, a, b = cv.split(lab)

  clahe = cv.createCLAHE(clipLimit = 7.0, tileGridSize = (1,1))
  cl = clahe.apply(l_channel)

  contrast_image = cv.merge((cl, a, b))

  enhanced_image = cv.cvtColor(contrast_image, cv.COLOR_LAB2BGR)
  grey_scaled = cv.cvtColor(enhanced_image, cv.COLOR_BGR2GRAY)  


  #smoothing using gaussian Blur to remove noise
  blurred_image = cv.GaussianBlur(grey_scaled, (5,5), 0)

  #converting to binary image
  _, binary_image = cv.threshold(grey_scaled, 128, 255, cv.THRESH_BINARY)

  #dilation followed by erosion
  dilated_image = cv.dilate(binary_image, np.ones((2,2), np.uint8), iterations=1)
  eroded_image = cv.erode(dilated_image, np.ones((1,1), np.uint8), iterations=1)

  return eroded_image, cropped_image, binary_image



def get_x_from_countours(contours):
   '''
   return x corrdinates of contours
   '''
   x, y, w, h = cv.boundingRect(contours)
   return x


def get_percentage_diff(x, y):
  '''
  returns percentage difference between width and heights
  eg: if width is 100 and height is 80, it returns (100-80)/100 = 20%. That is the difference in width and height is only 0.2
  '''
  if x < 15 and y < 15:
    #if both the width and height are less than 10, we discard it assuming it as noise
    return 1

  try:
    return abs(x - y) / max(x, y)
    
  except ZeroDivisionError:
    return abs(x - y) / 1
  


def get_final_contours(contours):

  #sorting the contors based on their x-axis position, return contours from left to right
  cont = sorted(contours, key=get_x_from_countours)

  #variable to store all the final contours
  final_contours = []

  #looping through all the contours
  for c in cont:
    _, _, width, height = cv.boundingRect(c)

    threshold = 0.6
    value = get_percentage_diff(width, height)

    #if the difference in percentage between width and height is greater than some threshold, we discard the contour
    # This is done to discard the contours whose, height is very higher than the width or vice versa

    #we set the threshold to 0.6, i.e if the difference between height and width is greater than 60%. We are going to discard it
    if value > threshold: 
      continue
    else:
      final_contours.append(c)


  return final_contours



