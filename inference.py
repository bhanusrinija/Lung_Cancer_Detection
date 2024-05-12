import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Define the classes
classes = [
    "AdenocarcinomaChest Lung Cancer",
    "Large cell carcinoma Lung Cancer",
    "NO Lung Cancer/ NORMAL",
    "Squamous cell carcinoma Lung Cancer"
]

def load_model_and_predict(image_path):
    # Load the pre-trained model
    model = tf.keras.models.load_model('inception_chest.h5')

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255
    x = np.expand_dims(x, axis=0)

    # Make predictions
    predictions = model.predict(x)
    if np.argmax(predictions) in [0, 1, 3]:
        is_cancerous = "Cancerous"
        cancer_type = classes[np.argmax(predictions)]
    else:
        is_cancerous = "NO Lung Cancer/ NORMAL"
        cancer_type = ""

    # Return the result indicating whether cancerous and the cancer type
    return f"{is_cancerous}|{cancer_type}"
