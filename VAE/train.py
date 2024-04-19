import tensorflow as tf
from tensorflow import keras
import vae
from vae import *
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os 
import numpy as np
from PIL import Image
import ast

# ********************************************************************************
# Create the model

load_model = False

if not load_model:
    latent_dim = 128
    #beta = 1.0
    beta = 0.01
    encoder = build_encoder(latent_dim)
    decoder = build_decoder(latent_dim)
    vae = VAE(encoder, decoder, beta)
    vae.compile(optimizer=keras.optimizers.Adam())

else:
    vae = tf.keras.models.load_model("vae_model.keras")

# ********************************************************************************
# Train the model

marble_color_labels = pd.read_csv('./resized_images/green_orange_purple_resized/green_orange_purple.csv')

# Preprocess color vectors
marble_color_labels['colors_vectors'] = marble_color_labels['colors_vectors'].apply(ast.literal_eval)
marble_color_labels['colors_vectors'] = marble_color_labels['colors_vectors'].apply(lambda x: np.array(x) / 255.0)

# Create ImageDataGenerator
datagen = ImageDataGenerator(rescale=1./255.)

# Create a flow from DataFrame
dataset = datagen.flow_from_dataframe(
    dataframe=marble_color_labels,
    directory="./resized_images/green_orange_purple_resized/",
    x_col="image_path",
    y_col="colors_vectors",
    seed=42,
    class_mode="raw",
    target_size=(64,64),
    color_mode="rgb",
    batch_size=128
)
# for images, labels in dataset:
#     print(labels)

# Get a batch of data
images, labels = next(dataset)

# Assuming each label contains 9 color vectors
num_color_vectors = 9

# Verify the structure of the labels array
for label in labels:
    assert len(label) == num_color_vectors, "Each label should contain 9 color vectors."

# Flatten the list of color vectors for each label
#flattened_labels = np.array([np.concatenate(label) for label in labels], dtype=np.float32)

# Verify the shape of the flattened labels array
#print("Shape of flattened labels array:", flattened_labels.shape)

labels = list(labels)
# print("Labels data type:", labels.dtype)


#labels = tf.convert_to_tensor(labels, np.float32)

#convert each individual marble into a tensor (for loop)
converted_labels = [tf.convert_to_tensor(label, np.float32) for label in labels]


for i in converted_labels:
    if len(i) != 9:
        print("not 9")

print("Shape of images:", images.shape)
print("Shape of converted_labels:", len(converted_labels))
# # Create a folder to save the images and labels
# output_folder = "./saved_images_and_labels/"
# os.makedirs(output_folder, exist_ok=True)

# # Define the number of images to save
# num_images_to_save = 3

# # Iterate through the dataset
# for i, (images, labels) in enumerate(dataset):
#     # Iterate through the batch
#     for j in range(min(num_images_to_save, images.shape[0])):
#         # Extract the image and label
#         image = images[j]
#         label = labels[j]
        
#         # Save the image
#         image_path = os.path.join(output_folder, f"image_{i * dataset.batch_size + j}.jpg")
#         image = Image.fromarray((image * 255).astype(np.uint8))  # Convert back to uint8
#         image.save(image_path)
        
#         # Save the label
#         label_path = os.path.join(output_folder, f"label_{i * dataset.batch_size + j}.txt")
#         np.savetxt(label_path, label)
        
#         # Print progress
#         print(f"Saved image {i * dataset.batch_size + j + 1}/{num_images_to_save}")
    
#     # Break the loop if the desired number of images has been saved
#     if i * dataset.batch_size + j >= num_images_to_save - 1:
#         break


converted_labels_tensor = tf.stack(converted_labels, axis=0)  # Convert the list of tensors to a single tensor and stack 
print("Shape of converted_labels_tensor:", converted_labels_tensor.shape)
print("Sample of converted_labels_tensor:", converted_labels_tensor[0])  # Print the first sample


if not load_model:
    vae = VAE(encoder, decoder, beta)
    vae.compile(optimizer=keras.optimizers.Adam(), loss=vae.train_step)
    vae.fit(x=images, y = converted_labels_tensor, epochs=100)
    # vae.save("vae_model.keras")
# else:
#     vae = tf.keras.models.load_model("vae_model.keras")


vae.summary()
# vae.encoder

### --------- Visualize ---------  ###
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