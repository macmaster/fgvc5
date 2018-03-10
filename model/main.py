import tensorflow as tf
hello = tf.constant("Hello Tensorflow!")
session = tf.Session()
print(session.run(hello))
