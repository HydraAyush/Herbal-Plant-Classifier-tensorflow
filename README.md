# Inception-Based Image Classification for 37 Classes

This project demonstrates the use of a Convolutional Neural Network (CNN) built upon the Inception architecture to classify images into 37 distinct categories. The model is trained using Keras with TensorFlow backend and utilizes data augmentation for improved generalization.

## 🧠 Model Overview

The neural network leverages:
- Inception base model for deep feature extraction
- Custom dense layers for classification
- `Softmax` activation for multi-class output

Loss function used: `categorical_crossentropy`  
Optimizer: `adam`  
Evaluation metric: `accuracy`

## 📁 Dataset

- The dataset consists of images organized into 37 labeled folders, representing each class.
- It is split into training and validation sets using `ImageDataGenerator`.

## 📊 Results

- Accuracy and loss are visualized across epochs.
- The final model summary and accuracy plots are included.
- Metrics saved:
  - `AccVal_acc.png`
  - `LossVal_loss.png`

## 🧪 Requirements

Install the necessary packages using the included `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. Ensure your dataset is organized in 37 labeled folders.
2. Open the notebook in Google Colab or a Jupyter environment.
3. Run the cells sequentially to train and evaluate the model.
4. View plots for training and validation metrics.

---

### 📈 Sample Output

- Model accuracy and loss plotted using `matplotlib`.
- Classification using trained model on test data.

## 🤝 Credits

Developed by Ayush Shewale.  
Uses TensorFlow, Keras, and OpenCV for implementation.
