class InstanceNormalization(layers.Layer):
  """Instance Normalization layer"""
  def __init__(self, epsilon= 1e-5):
    super(InstanceNormalization, self).__init__()
    self.epsilon= epsilon

  def build(self, input_shape):
    self.scale = self.add_weight(name= 'scale', shape= input_shape[-1:], initializer= tf.random_normal_initializer(1, 0.02), trainable= True)
    self.offset = self.add_weight(name='offset', shape= input_shape[-1:], initializer= 'zeros', trainable= True)

  def call(self, x):
    mean, variance = tf.nn.moments(x, axes=[1,2], keepdims=True)
    inv = tf.math.rsqrt(variance + self.epsilon)
    normalized= (x-mean)*inv
    return self.scale*normalized + self.offset