# Quadratic Equation using Keras + TensorFlow
# Equation: y = 5x² + 4x + 3 + Gaussian Noise
# Goal: Learn coefficients a, b, c using a simple neural network

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import math

# --- Generate synthetic dataset ---
np.random.seed(42)
tf.random.set_seed(42)

# Input x values between [-5, 4]
n_samples = 120
x = np.linspace(-5, 4, n_samples)
np.random.shuffle(x)  # shuffle for randomness

# True quadratic relationship
true_a, true_b, true_c = 5.0, 4.0, 3.0

# Add Gaussian noise to make it realistic
noise = np.random.normal(0, 2.0, n_samples)
y = true_a * x**2 + true_b * x + true_c + noise

# Reshape for Keras
x_train = x.reshape(-1, 1).astype(np.float32)
y_train = y.reshape(-1, 1).astype(np.float32)

# --- Build the model ---
# We'll manually create polynomial features: [x², x, 1]
def poly_features(x):
    x2 = tf.math.square(x)
    ones = tf.ones_like(x)
    return tf.concat([x2, x, ones], axis=1)  # shape -> (batch, 3)

# Model definition
inputs = keras.Input(shape=(1,), name="input_x")
poly = layers.Lambda(poly_features, name="poly_features")(inputs)
output = layers.Dense(1, use_bias=False, name="poly_dense")(poly)  # bias already in features
model = keras.Model(inputs, output)

# Summary of model (should show 3 weights: a, b, c)
model.summary()

# --- Compile the model ---
learning_rate = 0.05
optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='mse')

# --- Train the model ---
callbacks = [
    keras.callbacks.EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
]

history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=1000,
    batch_size=16,
    callbacks=callbacks,
    verbose=0
)

# --- Extract learned coefficients ---
weights = model.get_layer("poly_dense").get_weights()[0].flatten()
learned_a, learned_b, learned_c = weights

# --- Evaluate performance ---
y_pred = model.predict(x_train).flatten()
rmse = math.sqrt(mean_squared_error(y_train.flatten(), y_pred))

print("\nTrue Equation:     y = 5x² + 4x + 3")
print(f"Learned Equation:  y = {learned_a:.4f}x² + {learned_b:.4f}x + {learned_c:.4f}")
print(f"RMSE: {rmse:.6f}")
print(f"Epochs Trained: {len(history.history['loss'])}")

# --- Plot results ---
# Sort for smooth plotting
idx = np.argsort(x_train.flatten())
x_sorted = x_train.flatten()[idx]
y_sorted = y_train.flatten()[idx]
y_pred_sorted = y_pred[idx]

# Input data
plt.figure(figsize=(6, 4))
plt.scatter(x_train, y_train, label='Input data set', s=12)
plt.title("Input Data Set")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Actual vs Predicted
plt.figure(figsize=(6, 4))
plt.scatter(x_sorted, y_sorted, label='Actual', s=10)
plt.plot(x_sorted, y_pred_sorted, label='Predicted', color='red')
plt.title(f"Comparison of Actual vs Predicted Values\nModel: y={learned_a:.2f}x² + {learned_b:.2f}x + {learned_c:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# --- Summary ---
print("\nSummary:")
print(f"- Learning rate: {learning_rate}")
print(f"- Total weights: {model.count_params()} (a, b, c)")
print(f"- RMSE: {rmse:.6f} → Lower is better")
print("Try tweaking learning rate or noise scale to get even better convergence!")
