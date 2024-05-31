import tensorflow as tf

# Check if GPU is available
if tf.test.is_gpu_available():
    # Set device to GPU
    device = tf.device("GPU")
    print("GPU is available. Using GPU.")
else:
    # Set device to CPU
    device = tf.device("CPU")
    print("GPU is not available. Using CPU.")

# Perform some operations on the device
x = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32, device=device)
y = tf.constant([4.0, 5.0, 6.0], dtype=tf.float32, device=device)
z = x + y

# Move the result back to CPU if necessary
if device.type == "GPU":
    z = z.cpu()

print("Result:", z)
