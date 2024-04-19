import sys
sys.path.append('/Users/rochellekaper/Desktop/AdaCog/MastersProject/Tensorflow/marblejarparadigm/')
import vae
from vae import *
# import train
# from train import *
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image

# vae = tf.keras.models.load_model("vae_model.keras")
# encoder = vae.build_encoder
# decoder = vae.build_decoder

vae.encoder

keras.utils.plot_model(vae.encoder, "vae_encoder_diagram.pdf", show_shapes = True)
keras.utils.plot_model(vae.decoder, "vae_decoder_diagram.pdf", show_shapes = True)

dataset = keras.utils.image_dataset_from_directory(
   # "./img/",
   "./resized_images/",
    labels = None,
    image_size = (64, 64),
    color_mode = "rgb",
    batch_size = 128)

normalization_layer = keras.layers.Rescaling(1.0/255)
def change_inputs(images):
  x = normalization_layer(images)
  return x
normalized_dataset = dataset.map(change_inputs)

#filepath = "./out/"
filepath = "./resized_images_out/"
for batch in normalized_dataset.take(1):
    for i, x in enumerate(batch):
      input_np = np.asarray(x) * 255
      image_in = Image.fromarray(input_np.astype('uint8'), 'RGB')
      new_img_name = str(i + 1).zfill(6) + "_in.png"
      image_in.save(filepath + new_img_name)

      x = np.asarray(x).reshape((1, 64, 64, 3))
      z_mean, z_log_var, z = vae.encoder(x)
      reconstruction = vae.decoder(z)

      new_img_name = str(i + 1).zfill(6) + "_out.png"
      result_np = reconstruction[0].numpy().reshape((64, 64, 3)) * 255
      image = Image.fromarray(result_np.astype('uint8'), 'RGB')
      image.save(filepath + new_img_name)