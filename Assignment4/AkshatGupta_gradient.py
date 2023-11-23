import numpy as np
import matplotlib.pyplot as plt

# input data
X = np.arange(-20, 20, 0.1)
np.random.shuffle(X)

## noise
eps = np.random.rand(400) * 10

## actual output
y_true = 23 * X + 43 + eps

## include bias as part of the weight matrix
## consider all X[0] = 1 for the bias 
X_bias = np.vstack([np.ones(len(X)), X]).T

## initialize all weights
weights = np.random.rand(2)
learning_rate = 0.005
num_iterations = 100

## gradient descent for 100 iterations
for iteration in range(num_iterations):
    ## y_pred and error calculation
    y_pred = np.dot(X_bias, weights)
    error = y_pred - y_true

    ## updatuion of weights
    gradient = 2*(np.dot(X_bias.T, error)/len(X))
    weights -= learning_rate * gradient

    ## calculate loss = MSE
    mse = np.mean((error)**2)
    print(f"Iteration #{iteration + 1}/{num_iterations}, Loss = {mse}")

## final weight and bias
print(f"w = {weights[1]}, b = {weights[0]}")

## visualize the original data and the regression line
plt.scatter(X, y_true, label='Actual Output')
plt.plot(X, y_pred, color='red', label='Predicted Output')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()