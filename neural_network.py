#!/usr/bin/env python
# -*- coding: utf-8 -*-
# August, 2019
# Perceptron neural network with backpropagation for synaptic weights

import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3,1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def train(self, training_inputs, training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
    
    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output
    
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)


if __name__=="__main__":
    neural_network = NeuralNetwork()
    print("Random synaptic weights: ")
    print(neural_network.synaptic_weights)
        
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])
    training_outputs = np.array([[0,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 10000)
    print("synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))
    print("New situation: input data = ", A, B, C)
    print("Output data: ")
    print(neural_network.think(np.array([A, B, C])))


    np.random.seed(1)

    synaptic_weights = 2 * np.random.random((3,1)) - 1

    print('Random starting synaptic weights: ')
    print(synaptic_weights)

    # main loop
    for iteration in range(20000):
        input_layer = training_inputs
        outputs = sigmoid(np.dot(input_layer, synaptic_weights))
        error = training_outputs - outputs
        adjustments = error * sigmoid_derivative(outputs)
        synaptic_weights += np.dot(input_layer.T, adjustments)    
        
    print('Synaptic weights after training')
    print(synaptic_weights)
        
    print('outputs after training: ')
    print(outputs)
        