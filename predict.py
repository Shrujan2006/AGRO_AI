import os
import tensorflow as tf
import numpy as np
import cv2

# Suppress TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load trained model
model = tf.keras.models.load_model("model/crop_disease_model.h5")

# Class names
class_names = ['Apple___Black_rot',
               'Corn_(maize)___Common_rust_',
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
               'Potato__Early_blight',
               'Potato__Healthy',
               'Strawberry___Leaf_scorch',
               'Tomato___Early_blight',
               'Tomato___Healthy',
               'Tomato___Late_blight',
               'Tomato___Leaf_Mold',
               'Tomato___Septoria_leaf_spot']

# Folder containing test images
test_folder = "test_images"

print("Files found:", os.listdir(test_folder))

for filename in os.listdir(test_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(test_folder, filename)

        img = cv2.imread(img_path)
        if img is None:
            print("Could not read:", filename)
            continue

        img = cv2.resize(img, (128,128))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        class_index = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        print("\nImage:", filename)
        print("Predicted Disease:", class_names[class_index])
        print("Confidence:", round(confidence, 2), "%")
