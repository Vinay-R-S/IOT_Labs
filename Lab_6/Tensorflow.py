import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam, SGD
import matplotlib.pyplot as plt

# --- 1. Define the XOR Dataset ---
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype="float32")
Y = np.array([[0], [1], [1], [0]], dtype="float32")


# --- 2. Define the Neural Network Architecture ---
def create_model(optimizer):
    model = Sequential([
        # Hidden layer: 4 neurons, 'relu' activation for non-linearity
        Dense(4, input_dim=2, activation='relu', name='hidden_layer'),
        # Output layer: 1 neuron, 'sigmoid' for binary classification output
        Dense(1, activation='sigmoid', name='output_layer')
    ])

    model.compile(
        loss='binary_crossentropy',
        optimizer=optimizer,
        metrics=['accuracy']
    )
    return model


# --- 3. Implement and Compare Optimizers (500 Epochs) ---
epochs = 500
batch_size = 4


# Adam Training
adam_model = create_model(optimizer=Adam(learning_rate=0.01))
adam_history = adam_model.fit(X, Y, epochs=epochs, batch_size=batch_size, verbose=0)
adam_model.evaluate(X, Y, verbose=0)


# SGD Training
sgd_model = create_model(optimizer=SGD(learning_rate=0.1))
sgd_history = sgd_model.fit(X, Y, epochs=epochs, batch_size=batch_size, verbose=0)
sgd_model.evaluate(X, Y, verbose=0)


# --- 4. Visualize Results (Loss) ---
plt.figure(figsize=(10, 6))
plt.plot(adam_history.history['loss'], label='Adam Loss', color='blue')
plt.plot(sgd_history.history['loss'], label='SGD Loss', color='red')
plt.title('XOR Neural Network Training Loss: Adam vs. SGD')
plt.xlabel('Epoch')
plt.ylabel('Binary Crossentropy Loss')
plt.legend()
plt.grid(True)
plt.savefig('convergence_path_comparison.png')

# Optional: Display the plot if running in an interactive environment
plt.show()
