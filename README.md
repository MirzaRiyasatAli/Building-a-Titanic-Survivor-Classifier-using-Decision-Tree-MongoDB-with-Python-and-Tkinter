# Titanic Survivor Classifier

## Introduction

The tragic sinking of the Titanic in 1912 left an indelible mark on history, and the stories of its passengers have captivated our collective imagination for over a century. The Titanic Survivor Classifier, a Python application, delves into this historical tragedy through a data-driven lens, aiming to predict whether a passenger aboard the Titanic survived or not. In this in-depth exploration, we’ll venture into the intricacies of this code, its dependencies, data augmentation techniques, the use of MongoDB, program design, and how to interact with the application.

## Unveiling the Code: An Object-Oriented Approach

The Titanic Survivor Classifier is powered by a rich array of Python libraries and modules. These crucial dependencies include:

- **Tkinter**: Tkinter provides the graphical user interface for the application, allowing users to interact with the classifier.
- **Pillow (PIL)**: The Python Imaging Library (Pillow) is used for image handling, allowing the application to display the Titanic image and the decision tree image.
- **NumPy**: NumPy, the fundamental package for scientific computing in Python, is used for numerical operations.
- **pymongo**: This library enables the program to connect to a MongoDB database for data storage and retrieval.
- **hashlib**: hashlib helps in securing user passwords by applying the SHA-256 hashing algorithm.
- **DecisionTreeClassifier**: The DecisionTreeClassifier is part of scikit-learn, a powerful machine learning library in Python. It is used to build and train the decision tree model.
- **Matplotlib**: Matplotlib, a data visualization library, is employed to generate and display the decision tree as an image.

- ## How to Run

To experience the dashboard, follow these simple steps:

1. Ensure you have Python installed.

2. Install the required dependencies.

3. Run the following command:
    ```bash
    python run App.py
    ```

## The Heart of the Application

The core of this application is the `TitanicSurvivorClassifier` class. This class is responsible for orchestrating the entire application. It ensures that the user interface is set up, handles user authentication and registration, and conducts the prediction using a decision tree classifier. This application integrates a variety of components to ensure a robust and interactive user experience.

## Components of the Program

### Login Interface

The journey begins with a login interface where users must enter their usernames and passwords. This crucial authentication step ensures that only registered users can access the application.

If the Username is not registered in the database, it will show this error.

and if the username is correct but the password is wrong, then it will show this error.

### User Registration

For new users, the program offers a registration option to create a new account.

User registration data is securely stored in a MongoDB database and the passwords are encrypted.

If the new username is already exist in the database, then it shows this error.


### Main Form

After a successful login, users are presented with the main form. This form displays the iconic Titanic image and provides input fields for collecting passenger data for prediction, also it shows the confidence number of the model.

### Decision Tree Model

The heart of the program is a decision tree classification model. This model predicts whether a passenger survived or not based on their input data. It is trained on a dataset stored in a MongoDB collection.

For higher resolution, you can follow the link.

### User Interaction

Users can input passenger details, including age, sex, class, and more. By clicking the “Predict” button, users trigger the model, and the prediction result is displayed.

### Data Visualization

The decision tree used for classification is visualized as an image. Users can click the “Show Decision Tree” button to view this image.

### Performance Evaluation

The program evaluates the model’s performance and displays the accuracy of its predictions.

## Data Augmentation: Enhancing the Dataset

To improve the accuracy and reliability of our model, we employ a technique known as data augmentation. Data augmentation involves expanding the dataset by adding new records that are consistent with the original data. In the context of the Titanic dataset, this means generating additional passenger records based on the characteristics of the existing dataset.

Data augmentation is a powerful approach that can help address issues like data imbalance and overfitting. It provides the model with more diverse examples to learn from, ultimately resulting in a more robust and generalizable model.

## MongoDB Integration: Storing User Credentials and Data

MongoDB, a popular NoSQL database, plays a central role in our program. It is used to store both user credentials and the Titanic dataset. Here’s how MongoDB is integrated into the program:

### Database Structure

The program works with a MongoDB database named “Assessment,” which contains two collections:

- **Login Collection**: This collection is responsible for storing user credentials, including their usernames and encrypted passwords. Security is a primary concern here, and all passwords are hashed using SHA-256 before being stored.
- **Titanic Collection**: The Titanic dataset, containing passenger information, is stored in this collection. The data is formatted and structured to facilitate easy access and utilization.

### Security Measures

To enhance security, MongoDB is configured with user authentication and access control. User authentication ensures that only authorized users can access and modify the database. It adds an additional layer of protection to the stored data.

## Flowchart: Navigating the User Experience

To simplify the understanding of user interactions, we’ve designed a flowchart that depicts the login and registration process. This flowchart helps illustrate the sequence of steps a user follows to access the program, whether as a registered user or a newcomer.

The flowchart demonstrates how users choose between logging in with existing credentials or registering as new users.

This flowchart shows how user data is processed and authenticated.

## Conclusion: A Powerful and Versatile Application

In conclusion, the “Titanic Survivor Classifier” is a versatile and interactive desktop application that combines data science, machine learning, and database management to predict passenger survival on the Titanic. It offers an array of features, including user authentication, data augmentation, secure database storage, and a user-friendly graphical interface.

This program can serve as both a learning resource and a template for similar projects. You can extend its functionality or adapt it for different datasets and applications.

The sinking of the Titanic will always be a somber part of history, but our ability to analyze and understand the data related to this event empowers us to draw valuable insights and learn from the past. We hope this in-depth exploration of our program has shed light on the intricate workings of this multifaceted application.

  [Building a Titanic Survivor Classifier using Decision Tree, MongoDB, Python and Tkinter demonstration video] (https://drive.google.com/drive/folders/1ZERQ1c56_UifS0NJV6CnehL3y0isLAMb?usp=sharing)

- **Blog Post on Medium:**
  [Building a Titanic Survivor Classifier using Decision Tree, MongoDB, Python and Tkinter](https://medium.com/@mirzariyasatali1/building-a-titanic-survivor-classifier-using-decision-tree-mongodb-python-and-tkinter-47838ed324e9)


- **LinkedIn Post:**
  [LinkedIn Post](https://www.linkedin.com/posts/mirza-riyasat-ali-688a58150_datascience-machinelearning-python-activity-7124713908258357248-L085?utm_source=share&utm_medium=member_android))

Thank you for taking the time to delve into the world of data science, machine learning, and user interface design with us. We hope this journey has been as enlightening for you as it has been for us.
