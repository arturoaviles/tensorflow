import tensorflow as tf
import matplotlib.pyplot as plt

uniform = tf.random_uniform([100], minval=0, maxval=1, dtype=tf.float32)

with tf.Session() as sess:
	print uniform.eval()
	plt.hist(uniform.eval(), normed=True)
	plt.show()