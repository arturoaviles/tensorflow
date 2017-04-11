import numpy as np
tensor_2d = np.array([
	(1, 2, 3, 4),
	(5, 6, 7, 8),
	(9, 10, 11, 12),
	(13, 14, 15, 16)
])

print "Tensor = ", tensor_2d
print "Tensor[3,3] = ", tensor_2d[3][3]
print "Tensor[0:2,0:2] = ", tensor_2d[0:2, 0:2]
print "Rank: ", tensor_2d.ndim # Rank
print "Shape: ", tensor_2d.shape # Shape
print "Data Type: ", tensor_2d.dtype # Data Type

print "Converting 2D Array to Tensor"
# Transforming Numpy Array to TensorFlow tensor:
import tensorflow as tf

tf_tensor = tf.convert_to_tensor(tensor_2d, dtype=tf.float64)

with tf.Session() as sess:
	print sess.run(tf_tensor)
	print sess.run(tf_tensor[3][3])
	print sess.run(tf_tensor[0:2][0:2])