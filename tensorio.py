import os
import tensorflow as tf
import tensorflow_io as tfio
import matplotlib.pyplot as plt

os.system("clear")

image = tf.image.decode_jpeg(tf.io.read_file('sample.jpg'))

print(image.shape, image.dtype)
plt.figure()
plt.imshow(image)
plt.axis('off')
plt.show()

