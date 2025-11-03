# Linear regression model using TensorFlow 2.0 to model a line
# Ref: https://heartbeat.fritz.ai/linear-regression-using-tensorflow-2-0-1cd51e211e1f
# Ref2: Giancarlo Zaccone, Getting Started with TensorFlow - Packt Publishing (2016)
# Chapter 3: Linear Regression Algorithm

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Create points in the range of 0 to 3, with equispaced ((1/120)*3 = 0.025)
x = np.linspace(0, 3, 120)

# Shuffle the values to guarantee they're not in order
np.random.shuffle(x)

# Random noise with the same shape as x
noise = np.random.randn(*x.shape) * 0.3

# Generate y for each of the x values, with added noise to the line function
# This avoids overfitting by the model
y = 2 * x + 0.9 + noise
print('Shape of y:', y.shape)

# Scatter plot of the input dataset
fig = plt.figure()
plt.scatter(x, y, label='Input data set')
plt.legend()
plt.show()

# Save the figure
fig.savefig('xdat.png', bbox_inches='tight')


# Define a linear model class
class LinearModel:
    def __init__(self):
        self.Weight = tf.Variable(11.0)
        self.Bias = tf.Variable(12.0)

    def __call__(self, x):
        return self.Weight * x + self.Bias


# Define loss function (Mean Squared Error)
def loss(y, pred):
    return tf.reduce_mean(tf.square(y - pred))


# Define the training function
def train(linear_model, x, y, lr=0.12):
    with tf.GradientTape() as tape:
        current_loss = loss(y, linear_model(x))
    lr_weight, lr_bias = tape.gradient(current_loss, [linear_model.Weight, linear_model.Bias])
    linear_model.Weight.assign_sub(lr * lr_weight)
    linear_model.Bias.assign_sub(lr * lr_bias)
    return current_loss


# Initialize model
linear_model = LinearModel()

# Track weights and biases during training
Weights, Biases = [], []
epochs = 200

# Initial loss
loss_val = loss(y, linear_model(x))
print('Shape of x, y, and loss_val:', x.shape, y.shape, loss_val.shape)

# Training loop
for epoch_count in range(epochs):
    Weights.append(linear_model.Weight.numpy())
    Biases.append(linear_model.Bias.numpy())
    current_loss = train(linear_model, x, y)
    print(f"Epoch {epoch_count}: Current loss = {current_loss.numpy()}")

print('Weights after training:', Weights)
print('Biases after training:', Biases)

# Final trained parameters
print('Trained Weight:', linear_model.Weight.numpy())
print('Trained Bias:', linear_model.Bias.numpy())

# Compute RMSE
RMSE = loss(y, linear_model(x))
print('RMSE:', RMSE.numpy())

# Predicted values
y_pred = linear_model(x)
print('Predicted line equation after training:')
print('y =', linear_model.Weight.numpy(), 'x +', linear_model.Bias.numpy())

# Plot actual vs predicted
fig = plt.figure()
plt.clf()
plt.title('Comparison of Actual and Predicted Values with the Trained Model')
plt.plot(x, y, 'b.', label='Actual')
plt.plot(x, y_pred, 'r.', label='Predicted')
plt.legend()
plt.show()

# Save the output figure
fig.savefig('output.png', bbox_inches='tight')
