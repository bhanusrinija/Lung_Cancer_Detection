import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from inference import load_model_and_predict

# Function to load and display an image
def load_image():
    file_path = filedialog.askopenfilename(title="Select Image",
                                           filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((224, 224))  # Resize image to match the model input size
        img = ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # Call your lung cancer detection function here
        predict_image(file_path)

# Function to predict lung cancer and display the result
def predict_image(image_path):
    # Use the function from inference.py to load model and predict
    result = load_model_and_predict(image_path)

    # Extract both whether cancer is detected and the type of cancer
    is_cancerous, cancer_type = result.split("|")

    result_label.config(text=f"Result: {is_cancerous}\nCancer Type: {cancer_type}")

# Create the main GUI window
root = tk.Tk()
root.title("Lung Cancer Detection")

# Create GUI components
canvas = tk.Canvas(root, width=224, height=224)
canvas.pack()

check_button = tk.Button(root, text="Check for Lung Cancer", command=load_image)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
