import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
#from keras.preprocessing.image import array_to_img, img_to_array, load_img
from tensorflow.keras.utils import img_to_array, load_img

def predict(image):
  print("Loading images...")
  #imagePaths = list(paths.list_images(r"/content/drive/MyDrive/Thesis Group/ML2/CXR Dataset"))
  data = []
  #labels = []
  dim = (224, 224)

  path = './images/' + image
  #path = 'images/COVID-725.png'
  #path = 'test/negative/Normal-424.png'
  print(path)
  temp_img = load_img(path,color_mode="grayscale",target_size=(dim))
  temp_img_array = img_to_array(temp_img) /255
  list_normal = []
  list_normal.append(temp_img_array)
  list_normal = np.array(list_normal)
  list_normal2 = list_normal.reshape(-1,50176)
  df_normal=pd.DataFrame(list_normal2)
  df_normal = df_normal.values.reshape(-1,224,224,1)

  #image.show()
  # img = cv2.imread(path)
  # print('image loaded')
  # img = cv2.resize(img, dim)
  # data.append(img)
  # data = np.array(data) / 255.0
  # print('image transformed')
  #print(data)
  # x = img_to_array(load_img(path,color_mode="grayscale", target_size=(224,224)))
  # x = np.array(x) / 255.0
  print('loading model')
  model = tf.keras.models.load_model('vgg.h5')
  print('predicting')
  print(df_normal.shape)
  print('************************')
  #prediction = model.predict(data)
  preds = model.predict(df_normal)
  return (np.argmax(preds, axis=-1))
  

#predict()