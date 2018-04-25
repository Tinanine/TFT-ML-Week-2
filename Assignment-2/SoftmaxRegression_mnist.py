# ----------------------------------------------------------------
 #  Author:        TFT
 #  Written:       4/23/2018
 #  Last updated:  4/25/2018
 #
 #  Execution:     python3 SoftmaxRegression_mnist.py
 #
 #  TFT Machine Learning
 #  Assignment  Week 2-2
 #
 #  Complete your code between "YOUR CODE HERE" and "END CODE".
 #  Donn't modify other code!
 #  % python3 SoftmaxRegression_mnist.py
 #  the accuracy will reach 90% after about 1000 steps of training
 #----------------------------------------------------------------

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os

# if you don't have GPU support, comment the following two lines
# if you have multiple GPUs, be free to use more than one for speeding up
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# load the dataset
mnist = input_data.read_data_sets("data", one_hot = True) # labels are "one-hot vectors"

# parameters
################################################################################
### YOUR CODE HERE: 2 lines
### Hint: What data type should we use here? What dimension should W and b have?
W =
b =
### END CODE
################################################################################
learning_rate = 0.1
momentum = 0.9
batch_size = 64
max_iter = 1000

# inputs & target outputs
################################################################################
### YOUR CODE HERE: 2 lines
### Hint: What data type should we use here? What dimension should x and y_ have?
x = ?
y_ = ?
### END CODE
################################################################################

# creat model
################################################################################
### YOUR CODE HERE: 1 line
y = ?
### END CODE
################################################################################

# loss function
################################################################################
### YOUR CODE HERE: 1 line
### Hint: look up "softmax_cross_entropy_with_logits" in Tensorflow official documation
cross_entropy = ?
### END CODE
################################################################################

# optimizer
optimizer = tf.train.MomentumOptimizer(learning_rate, momentum)
train_step = optimizer.minimize(cross_entropy)

# accuracy test
################################################################################
### YOUR CODE HERE: 1 line
### Hint: look up "tf.argmax" in Tensorflow official documation
correct_prediction = ?
accuracy = ?
### END CODE
################################################################################

# training
### Hint: remember to initialze Variables; remember to feed placeholders
with tf.Session() as sess:
    ################################################
    ### YOUR CODE HERE: 1 line
    sess.run(?)
    ### END CODE
    ################################################
    for iter in range(1000):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        test_x = mnist.test.images
        test_y = mnist.test.labels
        #########################################
        ### YOUR CODE HERE: 1 line
        sess.run(?) # run optimizer for one step
        ### END CODE
        #########################################
        if iter%10 == 0:
            #########################################
            ### YOUR CODE HERE: 3 lines
            ### Hint:
            ## 1. valuse of loss function on current training batch
            ## 2. accuracy on current training batch
            ## 3. accuracy on test data
            train_loss = ?
            train_accuracy = ?
            test_accuracy = ?
            ### END CODE
            #########################################
            print("iter step %d, training batch loss %f, training batch accuracy %f, test accuracy %f" %
                (iter,train_loss,train_accuracy,test_accuracy))
