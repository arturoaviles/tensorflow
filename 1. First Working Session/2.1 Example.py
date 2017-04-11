import tensorflow as tf

pi = tf.constant(3.14, name='pi')
my_age_plus_pi = tf.Variable(pi+22, name='my_age_plus_pi')

model = tf.global_variables_initializer()

with tf.Session() as session:
	session.run(model)
	print(session.run(my_age_plus_pi))
