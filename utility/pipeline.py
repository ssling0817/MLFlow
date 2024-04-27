# This file is designed based on MlFlow tutorial
# https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import pandas as pd

def data_preprocessing()-> tuple[np.ndarray]:
    """Generate IRIS dataset's train and test dataset

    Returns:
        Tuple[np.ndarray]: X_train, X_test, y_train, y_test generated by sklearn
        train_test_split function.
    """
    # Load the Iris dataset
    X, y = datasets.load_iris(return_X_y=True)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

def train_logistic_regression(
    X_train:np.ndarray, 
    y_train:np.ndarray,
    params: dict,
    ) -> LogisticRegression:
    """Function that generates a trained logistic regression model
    based on the training dataset and hyperparameters.

    Args:
        X_train (np.ndarray): Training dataset of shape (data point num, feature dim)
        X_test (np.ndarray): Test dataset of shape (data point num, 1)

    Returns:
        LogisticRegres# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

    # Infer the model signature
    signature = infer_signature(X_train, lr.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="iris_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="tracking-quickstart",
    )sion: Trained sklearn logistic regression model
    """
    # Train the model
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)
    return lr

def evaluation(
    model: LogisticRegression,
    X_test:np.ndarray, 
    y_test:np.ndarray,
) -> float:
    """evaluate the accuracy of the trained model

    Args:
        model (LogisticRegression): trained model object
        y_train (np.ndarray): test features
        y_test (np.ndarray): test labels

    Returns:
        float: accuracy of the trained model
    """
    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

    