# Lung_Cancer_Detection
Detect lung cancer from images with deep learning. GUI for user-friendly interaction. Accurate classification results. Open for contributions.
Lung Cancer Detection and Classification

**Overview**
Lung Cancer Detection and Classification is a deep learning-based project aimed at assisting in the early detection and classification of lung cancer from medical images. Lung cancer is one of the leading causes of cancer-related deaths worldwide, and early detection plays a crucial role in improving patient outcomes. This project leverages state-of-the-art deep learning techniques to analyze lung images and provide insights into the presence and type of lung cancer.

**Key Features**
**Graphical User Interface (GUI):** The project includes a user-friendly GUI built using Tkinter, allowing users to interact with the system seamlessly.
**Deep Learning Model:** Utilizes a convolutional neural network (CNN) architecture for image classification, pretrained on the InceptionV3 model and fine-tuned on a dataset of lung images.
**Image Preprocessing:** Implements image preprocessing techniques such as rescaling, shearing, zooming, and horizontal flipping to enhance the robustness of the model.
**Model Evaluation:** Evaluates the model's performance using metrics such as accuracy and loss, visualized through plots generated using Matplotlib.
**Inference:** Provides functionality for real-time inference on user-provided medical images to detect the presence and type of lung cancer.
**Save and Load Model:** Allows saving and loading of the trained model for future use without the need for retraining.


**Usage**
**Download Dataset from Kaggle:**
https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images
**Clone the Repository:** Clone this repository to your local machine using Git.

git clone https://github.com/your_username/lung-cancer-detection.git

**Install Dependencies:** Install the required Python dependencies using pip.
pip install -r requirements.txt

**Run the GUI Application: **Launch the GUI application by running the app.py script.
python app.py

**Upload Images:** Click on the "Check for Lung Cancer" button in the GUI to select and upload medical images (e.g., X-rays, CT scans) for analysis.

**View Results:** The system will provide the classification results, indicating whether lung cancer is present and, if so, the type of cancer detected.

**Credits**
**Developed by **Bhanu Srinija Pasupuleti
**Dataset:** Chest CT-Scan images Dataset
**Trained Model:** inception_chest.h5
