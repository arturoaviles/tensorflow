import numpy as np
tensor3d = np.array([
	[[1,2],[3,4]],
	[[5,6],[7,8]]
])

print "Tensor = ", 
print tensor3d
print "Tensor[plane,row,col] "
print "Tensor[0] = ", tensor3d[0]
print "Tensor[0, 0] = ", tensor3d[0, 0]
print "Tensor[0, 0, 0] = ", tensor3d[0, 0, 0]
print "Rank: ", tensor3d.ndim # Rank
print "Shape: ", tensor3d.shape # Shape
print "Data Type: ", tensor3d.dtype # Data Type

print "Converting 3D Array to Tensor"
# Transforming Numpy Array to TensorFlow tensor:
'''
import tensorflow as tf

tf_tensor = tf.convert_to_tensor(tensor3d, dtype=tf.float64)

with tf.Session() as sess:
	print sess.run(tf_tensor)
	print sess.run(tf_tensor[3][3])
	print sess.run(tf_tensor[0:2][0:2])
'''
