# 📊 Customer Churn Prediction App

This repository contains a Streamlit application that predicts whether a customer is likely to churn based on various customer details. The prediction model is a Logistic Regression trained on a customer dataset.

## 📁 Project Structure

* `app.py`: The main Streamlit application script.

* `churn_model.pkl`: The trained Logistic Regression model saved using `pickle`.

* `scaler.pkl`: The `StandardScaler` object used for feature scaling, also saved using `pickle`.

* `columns.pkl`: A list of column names in the order expected by the model, saved using `pickle`.

* `customerChurn.csv`: The dataset used for training the model.

* `Churn_Prediction.ipynb`: A Jupyter Notebook detailing the data preprocessing, model training, and evaluation steps.

* `requirements.txt`: A list of Python dependencies required to run the application.

## 🚀 How to Run the Application

Follow these steps to get the application up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**

* **pip** (Python package installer)

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
```

**Note:** Replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub username and repository name.

### 2. Create a Virtual Environment (Recommended)

It's highly recommended to create a virtual environment to manage dependencies:

### 2. Create a Virtual Environment

```bash
# Create environment with Python 3.10
conda create --name plant_env python=3.10

# Activate the environment
conda activate plant_env
```

### 4. Install Dependencies

Once your environment is active, install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

After installing all dependencies, you can run the Streamlit application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser. If it doesn't open automatically, you can access it by navigating to the local URL displayed in your terminal (usually `http://localhost:8501`).

## 📈 Usage

On the Streamlit application page, you will see various input fields corresponding to customer details. Fill in the information for the customer you want to predict.

Click the "Predict Churn" button, and the application will display whether the customer is likely to churn or stay.

## 📊 Model Details

The `Churn_Prediction.ipynb` notebook provides a detailed walkthrough of the model development process, including:

* Data loading and initial exploration.

* Handling missing values and data type conversions.

* One-hot encoding of categorical features.

* Feature scaling using `StandardScaler`.

* Splitting data into training and testing sets.

* Training a Logistic Regression model.

* Evaluating the model's performance (accuracy, classification report).

## 🤝 Contributing

Feel free to fork this repository, make improvements, and submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
