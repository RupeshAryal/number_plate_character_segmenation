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


  lab = cv.cvtColor(cropped_image, cv.COLOR_BGR2LAB)
  l_channel, a, b = cv.split(lab)

  clahe = cv.createCLAHE(clipLimit = 7.0, tileGridSize = (2,2))
  cl = clahe.apply(l_channel)

  contrast_image = cv.merge((cl, a, b))

  enhanced_image = cv.cvtColor(contrast_image, cv.COLOR_LAB2BGR)
  grey_scaled = cv.cvtColor(enhanced_image, cv.COLOR_BGR2GRAY)  



#   blurred_image = cv.GaussianBlur(grey_scaled, (5,5), 0)
  _, binary_image = cv.threshold(grey_scaled, 128, 255, cv.THRESH_BINARY)

  dilated_image = cv.dilate(binary_image, np.ones((2,2), np.uint8), iterations=1)
  eroded_image = cv.erode(dilated_image, np.ones((1,1), np.uint8), iterations=1)

  return eroded_image, cropped_image, binary_image



def get_x_from_countours(contours):
   x, y, w, h = cv.boundingRect(contours)
   return x



def get_percentage_diff(x, y):
  if x < 10 and y < 10:
    return 1

  try:
    return abs(x - y) / max(x, y)
  except ZeroDivisionError:
    return abs(x - y) / 1
  


def get_final_contours(contours):
  cont = sorted(contours, key=get_x_from_countours)
  final_contours = []

  for c in cont:
    x, y, w, h = cv.boundingRect(c)

    threshold = 0.5
    value = get_percentage_diff(w, h)

    if value > threshold:
      continue
    else:
      final_contours.append(c)


  return final_contours



