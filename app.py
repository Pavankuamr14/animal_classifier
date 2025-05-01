# import streamlit as st
# import tensorflow as tf
# import numpy as np
# from PIL import Image


# # Load the model
# @st.cache_resource
# def load_model():
#     model = tf.keras.models.load_model("animal_classifier.h5")
#     return model


# model = load_model()

# # Define class labels (Replace with your actual class labels)
# CLASS_NAMES = [
#     "antelope",
#     "badger",
#     "bat",
#     "bear",
#     "bee",
#     "beetle",
#     "bison",
#     "boar",
#     "butterfly",
#     "cat",
#     "caterpillar",
#     "chimpanzee",
#     "cockroach",
#     "cow",
#     "coyote",
#     "crab",
#     "crow",
#     "deer",
#     "dog",
#     "dolphin",
#     "donkey",
#     "dragonfly",
#     "duck",
#     "eagle",
#     "elephant",
#     "flamingo",
#     "fly",
#     "fox",
#     "goat",
#     "goldfish",
#     "goose",
#     "gorilla",
#     "grasshopper",
#     "hamster",
#     "hare",
#     "hedgehog",
#     "hippopotamus",
#     "hornbill",
#     "horse",
#     "hummingbird",
#     "hyena",
#     "jellyfish",
#     "kangaroo",
#     "koala",
#     "ladybugs",
#     "leopard",
#     "lion",
#     "lizard",
#     "lobster",
#     "mosquito",
#     "moth",
#     "mouse",
#     "octopus",
#     "okapi",
#     "orangutan",
#     "otter",
#     "owl",
#     "ox",
#     "oyster",
#     "panda",
#     "parrot",
#     "pelecaniformes",
#     "penguin",
#     "pig",
#     "pigeon",
#     "porcupine",
#     "possum",
#     "raccoon",
#     "rat",
#     "reindeer",
#     "rhinoceros",
#     "sandpiper",
#     "seahorse",
#     "seal",
#     "shark",
#     "sheep",
#     "snake",
#     "sparrow",
#     "squid",
#     "squirrel",
#     "starfish",
#     "swan",
#     "tiger",
#     "turkey",
#     "turtle",
#     "whale",
#     "wolf",
#     "wombat",
#     "woodpecker",
#     "zebra",
# ]


# # Image preprocessing
# def preprocess_image(image):
#     image = image.resize((224, 224))  # Resize to match EfficientNet input size
#     image = np.array(image) / 255.0  # Normalize
#     image = np.expand_dims(image, axis=0)  # Add batch dimension
#     return image


# # Streamlit UI
# st.title("Animal Classification using EfficientNet")
# st.write("Upload an animal image and the model will predict its species.")

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     processed_image = preprocess_image(image)
#     prediction = model.predict(processed_image)

#     predicted_class = CLASS_NAMES[np.argmax(prediction)]
#     confidence = np.max(prediction) * 100

#     st.write(f"### Prediction: {predicted_class} ({confidence:.2f}%)")
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("animal_classifier.h5")
    return model

model = load_model()

# Define class labels
CLASS_NAMES = [
    "antelope", "badger", "bat", "bear", "bee", "beetle", "bison", "boar", "butterfly",
    "cat", "caterpillar", "chimpanzee", "cockroach", "cow", "coyote", "crab", "crow",
    "deer", "dog", "dolphin", "donkey", "dragonfly", "duck", "eagle", "elephant",
    "flamingo", "fly", "fox", "goat", "goldfish", "goose", "gorilla", "grasshopper",
    "hamster", "hare", "hedgehog", "hippopotamus", "hornbill", "horse", "hummingbird",
    "hyena", "jellyfish", "kangaroo", "koala", "ladybugs", "leopard", "lion", "lizard",
    "lobster", "mosquito", "moth", "mouse", "octopus", "okapi", "orangutan", "otter",
    "owl", "ox", "oyster", "panda", "parrot", "pelecaniformes", "penguin", "pig",
    "pigeon", "porcupine", "possum", "raccoon", "rat", "reindeer", "rhinoceros",
    "sandpiper", "seahorse", "seal", "shark", "sheep", "snake", "sparrow", "squid",
    "squirrel", "starfish", "swan", "tiger", "turkey", "turtle", "whale", "wolf",
    "wombat", "woodpecker", "zebra"
]

# Image preprocessing
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to match EfficientNet input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("Animal Classification using EfficientNet")
st.write("Upload an animal image and the model will predict its species.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    if confidence >= 97:
        st.write(f"### Prediction: {predicted_class} ({confidence:.2f}%)")
    else:
        st.warning("⚠️ Please upload a clear animal image or note that the model is not trained on this animal.")
        st.markdown("#### The model currently supports the following animal classes:")
        st.markdown(", ".join(CLASS_NAMES))
