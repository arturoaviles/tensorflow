import numpy as np
tensor_1d = np.array([1.3, 1, 4.0, 23.99])

print "Tensor = ", tensor_1d
print "Tensor[0] = ", tensor_1d[0]
print "Tensor[2] = ", tensor_1d[2]
print "Rank: ", tensor_1d.ndim # Rank
print "Shape: ", tensor_1d.shape # Shape
print "Data Type: ", tensor_1d.dtype # Data Type

print "Converting 1D Array to Tensor"
# Transforming Numpy Array to TensorFlow tensor:
import tensorflow as tf

tf_tensor = tf.convert_to_tensor(tensor_1d, dtype=tf.float64)

with tf.Session() as sess:
	print sess.run(tf_tensor)
	print sess.run(tf_tensor[0])
	print sess.run(tf_tensor[2])