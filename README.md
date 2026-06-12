# DecodeLabs_AI_Intern
# AI Internship Tasks

## Overview

This repository contains two beginner-level Python tasks completed as part of an AI Development internship. The tasks demonstrate fundamental programming concepts, user interaction, data preprocessing, machine learning model training, and evaluation.

---

# Task 1: Rule-Based Chatbot

## Description

A simple command-line chatbot that responds to predefined user questions using a Python dictionary. The chatbot continuously accepts user input until the user enters `"bye"`.

## Features

* Greets users with predefined responses.
* Answers basic questions about the developer and internship.
* Handles unknown questions with a default response.
* Terminates the conversation when the user types `"bye"`.

## Technologies Used

* Python
* Dictionary Data Structure
* Loops and Conditional Statements

## Sample Interaction

```text
Program Started ...

How can I help you: hello
Hi there!

How can I help you: who are you
My name is Youssef Ghanem

How can I help you: bye
Goodbye!
```

## Learning Outcomes

* Working with dictionaries.
* Handling user input.
* Implementing loops and conditions.
* Building a basic rule-based conversational system.

---

# Task 2: Iris Flower Classification Using KNN

## Description

This project uses the famous Iris dataset to build a machine learning model capable of classifying iris flowers into their respective species using the K-Nearest Neighbors (KNN) algorithm.

## Dataset

The Iris dataset contains:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target Classes:

* Setosa
* Versicolor
* Virginica

## Workflow

### 1. Data Loading

The Iris dataset is loaded using Scikit-learn and converted into a Pandas DataFrame.

### 2. Data Exploration

* Display first few rows of the dataset.
* Check dataset structure.
* Verify missing values.

### 3. Data Preparation

* Separate features and target labels.
* Split data into training and testing sets.
* Standardize feature values using StandardScaler.

### 4. Model Training

Train a K-Nearest Neighbors classifier with:

```python
KNeighborsClassifier(n_neighbors=3)
```

### 5. Model Evaluation

Evaluate the model using:

* F1 Score
* Confusion Matrix

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Libraries Required

Install the dependencies using:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Expected Output

```text
Environment setup successful!
Model training complete!

--- Model Evaluation Results ---
F1-Score: 1.0000

Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```

(Note: Results may vary slightly depending on dataset split and model parameters.)

## Learning Outcomes

* Data preprocessing and cleaning.
* Feature scaling.
* Train-test splitting.
* Machine learning model training.
* Performance evaluation using classification metrics.

---

# Author

**Youssef Ghanem**


 
