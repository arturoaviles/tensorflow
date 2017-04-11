import tensorflow as tf
import matplotlib.pyplot as plt

norm =  tf.random_normal([100], mean=0, stddev=2)

with tf.Session() as sess:
	print norm.eval()
	plt.hist(norm.eval(), normed=True)
	plt.show()