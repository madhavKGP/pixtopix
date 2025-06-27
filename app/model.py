from keras.models import load_model

# Load the Pix2Pix generator model
model = load_model("app/pix2pix_generator.h5", compile=False)

# Predict function
def predict(input_array):
    return model.predict(input_array)
