# https://keras.io/examples/generative/vae/

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

# ********************************************************************************
# Sampling layer

#@keras.saving.register_keras_serializable()
class Sampling(layers.Layer):
    """Uses (z_mean, z_log_var) to sample a latent variable representation."""

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)

    def call(self, inputs):
        z_mean, z_log_var = inputs
        batch = tf.shape(z_mean)[0]
        dim = tf.shape(z_mean)[1]
        epsilon = tf.random.normal(shape=(batch, dim))
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon

# ********************************************************************************
# Encoder

def build_encoder(latent_dim):
    encoder_inputs = keras.Input(shape = (64, 64, 3), name = "encoder_input")
    conv_1 = layers.Conv2D(
        filters = 32, kernel_size = (4, 4), strides = 2, 
        padding = "same", activation = "relu")(encoder_inputs)
    conv_2 = layers.Conv2D(
        filters = 32, kernel_size = (4, 4), strides = 2,
        padding = "same", activation = "relu")(conv_1)
    conv_3 = layers.Conv2D(
        filters = 64, kernel_size = (4, 4), strides = 2,
        padding = "same", activation = "relu")(conv_2)
    conv_4 = layers.Conv2D(
        filters = 64, kernel_size = (4, 4), strides = 2,
        padding = "same", activation = "relu")(conv_3)
    dense_1 = layers.Dense(256, activation = "relu")(layers.Flatten()(conv_4))
    z_mean = layers.Dense(latent_dim)(dense_1)
    z_logvar = layers.Dense(latent_dim)(dense_1)
    z = Sampling()([z_mean, z_logvar])
    encoder = keras.Model(encoder_inputs, [z_mean, z_logvar, z], name="encoder")

    return encoder

# ********************************************************************************
# Decoder

def build_decoder(latent_dim):
    decoder_inputs = keras.Input(shape=(latent_dim,), name="decoder_input")
    dense_1 = layers.Dense(units=4 * 4 * 64, activation="relu")(decoder_inputs)
    x = layers.Reshape((4, 4, 64))(dense_1)
    conv_1 = layers.Conv2DTranspose(
        filters=64, kernel_size=(4, 4), strides=2, padding="same", activation="relu"
    )(x)
    conv_2 = layers.Conv2DTranspose(
        filters=64, kernel_size=(4, 4), strides=2, padding="same", activation="relu"
    )(conv_1)
    conv_3 = layers.Conv2DTranspose(
        filters=32, kernel_size=(4, 4), strides=2, padding="same", activation="relu"
    )(conv_2)
    conv_4 = layers.Conv2DTranspose(
        filters=3, kernel_size=(4, 4), strides=2, padding="same", activation="sigmoid"
    )(conv_3)

    marble_layers = [
        layers.Dense(units=3, activation="softmax", name=f"marble_{i + 1}")(decoder_inputs)
        for i in range(9)
    ]

    decoder = keras.Model(decoder_inputs, [conv_4] + marble_layers, name="decoder")
    return decoder


# ********************************************************************************
# Custom class to implement a combined VAE

#@keras.saving.register_keras_serializable()
class VAE(keras.Model):
    def __init__(self, encoder, decoder, beta, **kwargs):
        super().__init__(**kwargs)

        self.encoder = encoder
        self.decoder = decoder
        self.beta = beta
        
        self.total_loss_tracker = keras.metrics.Mean(name="total_loss")
        self.reconstruction_loss_tracker = keras.metrics.Mean(
            name="reconstruction_loss")
        self.categorical_loss_tracker = keras.metrics.Mean(
            name="categorical_loss")
        self.kl_loss_tracker = keras.metrics.Mean(name="kl_loss")

    def get_config(self):
        base_config = super().get_config()
        config = {
            "encoder": self.encoder,
            "decoder": self.decoder,
            "beta": self.beta
        }
        return {**base_config, **config}
    
    @classmethod
    def from_config(cls, config):
        config["encoder"] = keras.layers.deserialize(config["encoder"])
        config["decoder"] = keras.layers.deserialize(config["decoder"])
        return cls(**config)
    
    @property
    def metrics(self):
        return [
            self.total_loss_tracker,
            self.reconstruction_loss_tracker,
            self.categorical_loss_tracker,
            self.kl_loss_tracker,
        ]
    
    def call(self, inputs):
        #inputs will be a list of images and list of one-hot encoded values 
        z_mean, z_log_var, z = self.encoder(inputs)
        combined_output = self.decoder(z)  #reconstruction and marbles 1:9
        #need to return reconstructed images + probability of color for marbles 1:9 
        return [z, combined_output]

    def train_step(self, data):
        with tf.GradientTape() as tape:
            images, target = data 
            print("target shape", target.shape)
            z_mean, z_log_var, z = self.encoder(images)
            combined_output = self.decoder(z)
            reconstruction = combined_output[0]
            marble_1, marble_2, marble_3, marble_4, marble_5, marble_6, marble_7, marble_8, marble_9 = combined_output[1:10]


            reconstruction_loss = tf.reduce_mean(
                tf.reduce_sum(keras.losses.binary_crossentropy(images, reconstruction), axis=(1, 2))) 
            
            #categorical cross entropy computes distance between one hot encoded values and the probabilties for each marble color computed by the model 
           
            categorical_loss = tf.reduce_mean(
            keras.losses.categorical_crossentropy(target[:, 0], marble_1) + 
            keras.losses.categorical_crossentropy(target[:, 1], marble_2) +
            keras.losses.categorical_crossentropy(target[:, 2], marble_3) + 
            keras.losses.categorical_crossentropy(target[:, 3], marble_4) +
            keras.losses.categorical_crossentropy(target[:, 4], marble_5) + 
            keras.losses.categorical_crossentropy(target[:, 5], marble_6) +
            keras.losses.categorical_crossentropy(target[:, 6], marble_7) + 
            keras.losses.categorical_crossentropy(target[:, 7], marble_8) + 
            keras.losses.categorical_crossentropy(target[:, 8], marble_9))

            categorical_loss = tf.reduce_sum(categorical_loss)

            # categorical_loss = tf.reduce_mean(
            #     tf.reduce_sum(keras.losses.categorical_crossentropy([1,0,0], marble_1) + keras.losses.categorical_crossentropy([1,0,0], marble_2) +
            # keras.losses.categorical_crossentropy([1,0,0], marble_3) + keras.losses.categorical_crossentropy([1,0,0], marble_4) +
            # keras.losses.categorical_crossentropy([1,0,0], marble_5) + keras.losses.categorical_crossentropy([1,0,0], marble_6) +
            # keras.losses.categorical_crossentropy([1,0,0], marble_7) + keras.losses.categorical_crossentropy([1,0,0], marble_8) + keras.losses.categorical_crossentropy([1,0,0], marble_9)))

            
            categorical_loss = categorical_loss * 0.1 #set weights to 0 to get a normal beta-VAE. 
            ''' Once this works, introduce a numerical value and play around with it to 
            see how it changes quality of reconstructions. Save examples of reconstructions in a word doc to get qualitatively 
            how reconstruction changes '''
            
            kl_loss = -0.5 * (1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
            kl_loss = tf.reduce_mean(tf.reduce_sum(kl_loss, axis=1))
            total_loss = reconstruction_loss + categorical_loss + self.beta * kl_loss #loss for reconstruction error + output for supervised error (one hot encoding labels)
        #eventually will add parameter to control weight of categorical loss 
        
        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        self.total_loss_tracker.update_state(total_loss)
        self.reconstruction_loss_tracker.update_state(reconstruction_loss)
        self.categorical_loss_tracker.update_state(categorical_loss)
        self.kl_loss_tracker.update_state(kl_loss)
        return {
            "loss": self.total_loss_tracker.result(),
            "reconstruction_loss": self.reconstruction_loss_tracker.result(),
            "categorical_loss": self.categorical_loss_tracker.result(),
            "kl_loss": self.kl_loss_tracker.result()
        }

