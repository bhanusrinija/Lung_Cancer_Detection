# Lung Cancer Detection and Classification

![Lung Cancer Detection]

## Overview
Lung Cancer Detection and Classification is a deep learning-based project aimed at assisting in the early detection and classification of lung cancer from medical images. Leveraging a convolutional neural network (CNN) architecture pretrained on InceptionV3 and fine-tuned on a diverse dataset of lung images, the system provides an intuitive graphical user interface (GUI) for seamless interaction. Users can upload medical images, such as X-rays or CT scans, for real-time analysis. Through image preprocessing techniques including rescaling, shearing, and flipping, the model enhances robustness for accurate detection. The system evaluates model performance using metrics such as accuracy and loss, visualized through Matplotlib-generated plots. Classification results include indication of cancer presence and type, aiding healthcare professionals in diagnosis and treatment planning. With the ability to save and load trained models, the project facilitates easy deployment and scalability. Contributions are welcome to further enhance the project's capabilities, ensuring its utility in improving patient outcomes and combating lung cancer, a leading cause of cancer-related deaths worldwide.

## Key Features
- **Graphical User Interface (GUI)**: The project includes a user-friendly GUI built using Tkinter, allowing users to interact with the system seamlessly.
- **Deep Learning Model**: Utilizes a convolutional neural network (CNN) architecture for image classification, pretrained on the InceptionV3 model and fine-tuned on a dataset of lung images.
- **Image Preprocessing**: Implements image preprocessing techniques such as rescaling, shearing, zooming, and horizontal flipping to enhance the robustness of the model.
- **Model Evaluation**: Evaluates the model's performance using metrics such as accuracy and loss, visualized through plots generated using Matplotlib.
- **Inference**: Provides functionality for real-time inference on user-provided medical images to detect the presence and type of lung cancer.
- **Save and Load Model**: Allows saving and loading of the trained model for future use without the need for retraining.

## Usage
1. **Clone the Repository**: Clone this repository to your local machine using Git.
    ```
    git clone https://github.com/your_username/lung-cancer-detection.git
    ```

2. **Install Dependencies**: Install the required Python dependencies using pip.
    ```
    pip install -r requirements.txt
    ```

3. **Run the GUI Application**: Launch the GUI application by running the `app.py` script.
    ```
    python app.py
    ```

4. **Upload Images**: Click on the "Check for Lung Cancer" button in the GUI to select and upload medical images (e.g., X-rays, CT scans) for analysis.

5. **View Results**: The system will provide the classification results, indicating whether lung cancer is present and, if so, the type of cancer detected.

## Directory Structure
lung-cancer-detection/
│
├── data/
│ ├── train/
│ └── test/
├── models/
│ └── inception_chest.h5
├── app.py
├── inference.py
├── model_training.py
├── requirements.txt
└── README.md


## Dataset
The dataset used in this project is available on Kaggle: [Chest CT-Scan Images Dataset](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images).

## Contribution
Contributions to the project are welcome! If you have suggestions for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Credits
- Developed by Bhanu Srinija Pasupuleti
- Dataset: [Mohamed Hany](https://www.kaggle.com/mohamedhanyyy)
- Trained Model: inception_chest.h5
