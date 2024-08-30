from image_processing import image_preprocessing, get_final_contours
import cv2 as cv
import tensorflow as tf
from utils import list_of_character_classes



model  = tf.keras.models.load_model('model.h5')

def prediction(image_array):
    prediction = model.predict(image_array)
    predicted_class = tf.argmax(prediction[0]).numpy()
    index = list(list_of_character_classes.values())[predicted_class]
    return index



def adjust_size(image_path = None, image = None):
  if image_path is not None:
    image_array = tf.keras.preprocessing.image.load_img(image_path)
  else:
    image_array = image
  image_array = tf.keras.preprocessing.image.img_to_array(image_array)
  image_array = tf.expand_dims(image_array, 0)
  return image_array


def get_prediction(image_array):

  processed_image, resized_image_original, contrast_image = image_preprocessing(image= image_array)

  cropped_image_copy = resized_image_original.copy()

  # find all the contours from the image
  cont, _ = cv.findContours(processed_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  #extract contours based on some threshold and rule
  final_contours = get_final_contours(cont)


  word = []

  for contour in final_contours:

    #finding the 
    x, y, w, h = cv.boundingRect(contour)

    final_x = abs(x - 2)
    final_y = abs(y - 2)
    final_w = w + 4
    final_h = h + 4

    print(final_x, final_y)

    cv.rectangle(resized_image_original, (final_x, final_y), (x + w + 4, y + h + 4), (0,255,0), 2)
    crop = cropped_image_copy[final_y:final_y+h + 4, final_x: final_x+w + 4]

    # print(crop)


    resized_image = cv.resize(crop, (32,32))
    preprocessed_image = adjust_size(image = resized_image)
    index = prediction(preprocessed_image)
    word.append(index)


  return (' '.join(word), resized_image_original, contrast_image)


  