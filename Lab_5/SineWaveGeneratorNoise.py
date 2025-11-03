# Import Libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
from tensorflow.keras import layers

# Configuration and Constants

SAMPLES = 1000  # Total sample points
SEED = 1337     # Random seed for reproducibility

# Set seeds for consistent results
tf.random.set_seed(SEED)
np.random.seed(SEED)

# Data Generation
# Generate uniformly distributed random numbers between 0 and 2π
x_values = np.random.uniform(low=0, high=2 * math.pi, size=SAMPLES)
np.random.shuffle(x_values)  # Shuffle to ensure randomness

# Generate corresponding sine values
y_values = np.sin(x_values)

# Plot the initial sine wave data
plt.plot(x_values, y_values, 'b.')
plt.title("Sine Function Data (Without Noise)")
plt.xlabel("x values")
plt.ylabel("sin(x)")
plt.show()

# Add small random noise to y values
y_values += 0.1 * np.random.randn(*y_values.shape)

# Plot the noisy sine wave
plt.plot(x_values, y_values, 'b.')
plt.title("Sine Function Data (With Noise)")
plt.xlabel("x values")
plt.ylabel("sin(x) + noise")
plt.show()

# Data Splitting
TRAIN_SPLIT = int(0.6 * SAMPLES)
TEST_SPLIT = int(0.2 * SAMPLES + TRAIN_SPLIT)

x_train, x_validate, x_test = np.split(x_values, [TRAIN_SPLIT, TEST_SPLIT])
y_train, y_validate, y_test = np.split(y_values, [TRAIN_SPLIT, TEST_SPLIT])

# Check splits
assert (x_train.size + x_validate.size + x_test.size) == SAMPLES

# Plot splits
plt.plot(x_train, y_train, 'b.', label="Train")
plt.plot(x_validate, y_validate, 'y.', label="Validate")
plt.plot(x_test, y_test, 'r.', label="Test")
plt.title("Data Splits")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.show()

# Model Definition
def relu(input):
    return max(0.0, input)

model_1 = tf.keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(1,)),  # Hidden layer
    layers.Dense(1)  # Output layer
])

model_1.compile(
    optimizer='rmsprop',
    loss='mse',
    metrics=['mae']
)

model_1.summary()

# Model Training
history_1 = model_1.fit(
    x_train, y_train,
    epochs=500,
    batch_size=16,
    validation_data=(x_validate, y_validate),
    verbose=1
)

# Loss Visualization
loss = history_1.history['loss']
val_loss = history_1.history['val_loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'g.', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Skip the first few epochs for clarity
SKIP = 100
plt.plot(epochs[SKIP:], loss[SKIP:], 'g.', label='Training Loss')
plt.plot(epochs[SKIP:], val_loss[SKIP:], 'b.', label='Validation Loss')
plt.title('Training and Validation Loss (After Warm-up)')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Mean Absolute Error Visualization
mae = history_1.history['mae']
val_mae = history_1.history['val_mae']

plt.plot(epochs[SKIP:], mae[SKIP:], 'g.', label='Training MAE')
plt.plot(epochs[SKIP:], val_mae[SKIP:], 'b.', label='Validation MAE')
plt.title('Training and Validation Mean Absolute Error')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show()

# Predictions and Visualization
predictions = model_1.predict(x_train)

plt.clf()
plt.title('Training Data: Predicted vs Actual Values')
plt.plot(x_test, y_test, 'b.', label='Actual')
plt.plot(x_train, predictions, 'r.', label='Predicted')
plt.xlabel("x values")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
