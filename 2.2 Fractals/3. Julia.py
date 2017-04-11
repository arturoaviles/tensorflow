import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Mandelbrot Set
Y, X = np.mgrid[-2:2:0.005, -2:2:0.005]

Z = X+1j*Y
c = complex(0.0, 0.75)

zs = tf.Variable(Z) #Var on which we will iterate
ns = tf.Variable(tf.zeros_like(Z, tf.float32))

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

# Compute the new values of z: z^2 - x
zs_ = zs * zs - c

# Have we diverged with this new value?
not_diverged = tf.abs(zs_) < 4 #Stop condition of the iteration

step = tf.group(zs.assign(zs_),\
	ns.assign_add(tf.cast(not_diverged, tf.float32)))

for i in range(200): step.run()

plt.imshow(ns.eval())
plt.show()