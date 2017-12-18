import tensorflow as tf
a=tf.constant(10)
b=tf.constant(32)
sess=tf.Session()
print(sess.run(a+b))
