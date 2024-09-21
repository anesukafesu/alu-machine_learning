#!/usr/bin/env python3
""" Implements train
"""
import tensorflow as tf


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, 
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """ Creates and trains a neural network based on the passed in parameters
    Args:
        X_train (numpy.ndarray) the training X data for which the model will
            make predictions.
        Y_train (numpy.ndarray) the training Y data with the correct labels
            for X_train data.
        X_valid (numpy.ndarray) the validation X data
        Y_valid (numpy.ndarray) the validation Y data
        layer_sizes (List(int)) a list of ints where each int represents the
        number of nodes in a hidden layer
        activations (List(functions)) a list of functions corresponding to the
        activation function to be used for each layer
        alpha (float) the learning rate for the network
        iterations (int) the number of iterations to make
        save_path (string) the path to the file in which the model will be saved
    Returns
        save_path (string) the path where the model was saved
    """

    nx = X_train.shape[1]
    n_classes = Y_train.shape[1]

    x, y = create_placeholders(nx, n_classes)
    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)

    y_pred = forward_prop(x, layer_sizes, activations)
    tf.add_to_collection('y_pred', y_pred)

    loss = calculate_loss(y, y_pred)
    tf.add_to_collection('loss', loss)

    accuracy = calculate_accuracy(y, y_pred)
    tf.add_to_collection('accuracy', accuracy)

    training_op = create_train_op(loss, alpha)
    tf.add_to_collection('training_op', training_op)

    saver = tf.train.Saver()
    init = tf.global_variables_initializer()

    with tf.Session() as session:
        sess.run(init)

        for i in range(iterations + 1):
            loss_train = sess.run(loss, feed_dict={ x: X_train, y: Y_train })
            accuracy_train = sess.run(accuracy, feed_dict={ x: X_train, y: Y_train })
            loss_valid = sess.run(loss, feed_dict={ x: X_valid, y: Y_valid })
            accuracy_valid = sess.run(accuracy, feed_dict={ x: X_valid, y: Y_valid })

            if i % 100 == 0:
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(loss_train))
                print("\tTraining Accuracy: {}".format(accuracy_train))
                print("\tValidation Cost: {}".format(loss_valid))
                print("\tValidation Accuracy: {}".format(accuracy_valid))

            sess.run(train_op, feed_dict={ x: X_train, y: Y_train })

        return saver.save(sess, save_path)
