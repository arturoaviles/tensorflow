''' 
Tensorflow has functions to solve the derivate 
of y with respect to its exp x

Let us consider the math function: y = 2x^2. We want to compute 
the gradient di y with respect: x = 1
'''

import tensorflow as tf

x = tf.placeholder(tf.float32)

y = 2 * x * x

var_grad = tf.gradients(y, x)

with tf.Session() as sess:
	var_grad_val = sess.run(var_grad, feed_dict={x:1})

print(var_grad_val)