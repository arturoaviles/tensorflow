import matplotlib.image as mp_image
filename = "5. machineLearning.jpg"
input_image = mp_image.imread(filename)

print "input dim = {}".format(input_image.ndim)
print "input shape = {}".format(input_image.shape)
print "(pixels high, pixels wide, colors deep)"

import matplotlib.pyplot as plt
#plt.imshow(input_image)
#plt.show()

import tensorflow as tf
#my_image = tf.placeholder("uint8", [None, None, 3])
#slice = tf.slice(my_image, [10, 0, 0], [16, -1, -1])
x = tf.Variable(input_image, name='x')
model = tf.global_variables_initializer()

with tf.Session() as sess:
	x = tf.transpose(x, perm=[1, 0, 2])
	sess.run(model)
	result = sess.run(x)

plt.imshow(result)
plt.show()