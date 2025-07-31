import numpy as np

class DummyNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        # Forward pass
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        output = self.sigmoid(self.z2)
        return output

if __name__ == "__main__":
    # Example usage
    nn = DummyNeuralNetwork(input_size=3, hidden_size=5, output_size=1)
    X_dummy = np.array([[0.1, 0.2, 0.3]])
    output = nn.forward(X_dummy)
    print("Dummy output:", output)