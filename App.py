# Import necessary modules and libraries
import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from hashlib import sha256  # Import the hashlib module for password hashing
import os
from MongoDB import *  # Import custom module MongoDB.py
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree

# Define a class for the Titanic Survivor Classifier
class TitanicSurvivorClassifier:
    def __init__(self):
        # Initialize the application
        self.style = Style(theme='darkly')
        self.login_window = tk.Tk()  # Create the main login window
        self.login_window.title("Login Form")
        self.login_window.geometry("300x250")
        self.setup_login_ui()  # Set up the login user interface

    def setup_login_ui(self):
        # Set up the login UI with labels, input fields, and buttons
        self.username_label = tk.Label(self.login_window, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_window, width=30)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_window, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_window, show="*", width=30)
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_window, text="Login", command=self.login)
        self.login_button.pack()

        self.login_error_label = tk.Label(self.login_window, text="", fg="red")
        self.login_error_label.pack()

        self.register_button = tk.Button(self.login_window, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        # Function to handle user login
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Connect to MongoDB
        mongo_uri = 'mongodb://<MirzaRiyasatAli>:<23177487>@localhost:27017/'
        client = MongoClient(mongo_uri)
        db_name = 'Assessment'
        collection_name = 'Login'
        db = client[db_name]
        collection = db[collection_name]

        # Search for a document with the entered username
        query = {"username": username}
        result = collection.find_one(query)

        if result:
            stored_password = result["password"]
            entered_password_hash = self.hash_password(password)

            if stored_password == entered_password_hash:
                self.login_window.destroy()  # Close the login window
                self.open_main_form()  # Open the main form
            else:
                self.login_error_label.config(text="Invalid password")
        else:
            self.login_error_label.config(text="Invalid username")

    def register(self):
        # Function to handle user registration
        registration_window = tk.Tk()
        registration_window.title("Registration Form")
        registration_window.geometry("300x200")

        new_username_label = tk.Label(registration_window, text="New Username")
        new_username_label.pack()
        new_username_entry = tk.Entry(registration_window, width=30)
        new_username_entry.pack()

        new_password_label = tk.Label(registration_window, text="New Password")
        new_password_label.pack()
        new_password_entry = tk.Entry(registration_window, show="*", width=30)
        new_password_entry.pack()

        def save_new_user():
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()

            # Hash the password
            hashed_password = self.hash_password(new_password)

            # Save the username and hashed password to MongoDB
            self.save_new_user_to_mongodb(new_username, hashed_password)
            registration_window.destroy()

        register_button = tk.Button(registration_window, text="Register", command=save_new_user)
        register_button.pack()

    def hash_password(self, password):
        # Hash the password using SHA-256
        password_hash = sha256(password.encode()).hexdigest()
        return password_hash

    def save_new_user_to_mongodb(self, new_username, hashed_password):
        # Function to save a new user's data to MongoDB
        # Connect to MongoDB and the 'Assessment' database and 'Login' collection
        mongo_uri = 'mongodb://<MirzaRiyasatAli>:<23177487>@localhost:27017/'
        client = MongoClient(mongo_uri)
        db_name = 'Assessment'
        collection_name = 'Login'
        db = client[db_name]
        collection = db[collection_name]

        query = {"username": new_username}
        existing_user = collection.find_one(query)

        if existing_user:
            messagebox.showerror("Registration Error", "Username already exists. Please choose a different username.")
        else:
            # Store the username and hashed password in the database
            user_data = {"username": new_username, "password": hashed_password}
            collection.insert_one(user_data)
            messagebox.showinfo("Registration", "Registration successful. You can now log in with the new user.")

    # Function to open the main form after a successful login
    def open_main_form(self):
        main_form = tk.Tk()
        main_form.title("Decision Tree Algorithm for Classification of Survivors from Titanic Sinking")
        main_form.geometry("1300x780")

        # Load and display the Titanic image
        titanic_image = Image.open("Data/Theme.jpg")
        titanic_photo = ImageTk.PhotoImage(titanic_image)
        titanic_label = tk.Label(main_form, image=titanic_photo)
        titanic_label.photo = titanic_photo
        titanic_label.grid(row=0, column=0, rowspan=9, padx=20, pady=20)

        # Define a function to open the decision tree image
        def open_image():
            image_path = 'decision_tree.png'
            if os.path.exists(image_path):
                os.system(f'start {image_path}')
            else:
                label.config(text="Image not found")

        # Create "Show Decision Tree" button
        show_decision_tree_button = tk.Button(main_form, text="Show Decision Tree", command=open_image)
        show_decision_tree_button.grid(row=9, column=0, pady=10)

        # Create a "Predict" button
        # predict_button = tk.Button(main_form, text="Predict", width=30)
        # predict_button.grid(row=10, column=1, pady=10)

        # Create a dictionary to store the entry labels and their corresponding data types
        entry_data = {
            "Sex": ["Male", "Female"],
            "Age": "Number",
            "Sibsp (Number of siblings/spouses on Titanic)": "Number",
            "Parch (Number of parents/children on Titanic)": "Number",
            "Fare": "Number",
            "Embarked (Port of Embarkation)": ["Cherbourg", "Queenstown", "Southampton"],
            "Class": ["First", "Second", "Third"],
            "Who": ["Child", "Man", "Woman"],
            "Alone": [True, False]
        }

        entry_widgets = {}  # Dictionary to store the entry widgets

        for row, label in enumerate([
            "Sex", "Age", "Sibsp (Number of siblings/spouses on Titanic)",
            "Parch (Number of parents/children on Titanic)", "Fare", "Embarked (Port of Embarkation)", "Class", "Who",
            "Alone"
        ], start=1):
            data_type = entry_data[label]
            label_widget = tk.Label(main_form, text=label)
            label_widget.grid(row=row, column=1)

            if isinstance(data_type, list):
                # Create a dropdown menu for entries with multiple options
                var = tk.StringVar(main_form)
                var.set(data_type[0])  # Set the default value
                dropdown = tk.OptionMenu(main_form, var, *data_type)
                dropdown.grid(row=row, column=2)
                entry_widgets[label] = var

            elif data_type == "Number":
                # Create an entry field for numeric values
                text_box = tk.Entry(main_form, width=10)
                text_box.grid(row=row, column=2)
                entry_widgets[label] = text_box

        # Create a label to display the prediction result
        prediction_result_label = tk.Label(main_form, text="", fg="blue")
        prediction_result_label.grid(row=7, column=0, pady=10)

        # Define a function to get user data and make predictions
        def get_data():
            data_array = [0] * 16  # Initialize the data_array with zeros

            for label, widget in entry_widgets.items():
                if label == 'Alone':
                    # Handle Alone separately
                    alone_value = int(widget.get())
                    data_array[4] = alone_value
                elif isinstance(widget, tk.StringVar):
                    # Handle dropdown menus
                    selected_option = widget.get()
                    if label == "Sex":
                        if selected_option == "Female":
                            data_array[5] = 1
                        elif selected_option == "Male":
                            data_array[6] = 1
                    elif label == "Embarked (Port of Embarkation)":
                        if selected_option == "Cherbourg":
                            data_array[7] = 1
                        elif selected_option == "Queenstown":
                            data_array[8] = 1
                        elif selected_option == "Southampton":
                            data_array[9] = 1
                    elif label == "Class":
                        if selected_option == "First":
                            data_array[10] = 1
                        elif selected_option == "Second":
                            data_array[11] = 1
                        elif selected_option == "Third":
                            data_array[12] = 1
                    elif label == "Who":
                        if selected_option == "Child":
                            data_array[13] = 1
                        elif selected_option == "Man":
                            data_array[14] = 1
                        elif selected_option == "Woman":
                            data_array[15] = 1
                elif isinstance(widget, tk.Entry):
                    # Handle numeric entry fields
                    value = float(widget.get())
                    if label == 'Age':
                        data_array[0] = value
                    elif label == 'Sibsp (Number of siblings/spouses on Titanic)':
                        data_array[1] = value
                    elif label == 'Parch (Number of parents/children on Titanic)':
                        data_array[2] = value
                    elif label == 'Fare':
                        data_array[3] = value

            print(data_array)  # Replace this with your desired processing

            # Now, after collecting the data, you can proceed to get the prediction
            new_data = np.array([data_array])
            new_data = new_data.reshape(1, -1)  # Reshape the array to match the input shape of the model

            prediction = model.predict(new_data)

            if prediction[0] == 0:
                prediction_result_label.config(text="This passenger is dead")
            elif prediction[0] == 1:
                prediction_result_label.config(text="This passenger survived")

        # Create a "Predict" button
        predict_button = tk.Button(main_form, text="Predict", command=get_data, width=30)
        predict_button.grid(row=10, column=1, pady=10)

        # Create "Submit" button
        # submit_button = tk.Button(main_form, text="Submit", command=get_data, width=30)
        # submit_button.grid(row=10, column=2, pady=10)

        # Connect to MongoDB to retrieve data
        mongo_uri = 'mongodb://<MirzaRiyasatAli>:<23177487>@localhost:27017/'
        db_name = 'Assessment'
        collection_name = 'Titanic'

        data = load_dataframe_from_mongodb(db_name, collection_name, mongo_uri)
        # Remove the '_id' column
        data = data.drop(['_id'], axis=1)

        titanic_data = data
        # Preprocess the dataset
        # Fill the missing values in the “age” and “embarked” columns of the titanic_data DataFrame.
        titanic_data['age'] = titanic_data['age'].fillna(titanic_data['age'].median())
        titanic_data['embarked'] = titanic_data['embarked'].fillna(titanic_data['embarked'].mode()[0])

        # convert categorical variables into numerical variables using one-hot encoding.
        titanic_data = pd.get_dummies(titanic_data, columns=['sex', 'embarked', 'class', 'who'])

        # Split the dataset (Now, we will split the dataset into training and testing sets)
        X = titanic_data.drop('survived', axis=1)
        y = titanic_data['survived']

        # 20% of the data is reserved for testing, and the remaining 80% is used for training.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the decision tree model
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        # Extract feature names from the DataFrameq
        features = X.columns

        # Plot the decision tree as an image
        plt.figure(figsize=(12, 8), dpi=2000)
        tree.plot_tree(model, feature_names=features, filled=True, class_names=['Not Survived', 'Survived'])
        plt.savefig('decision_tree.png', format='png')
        # plt.show()

        # Evaluate the performance of the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print('Accuracy:', accuracy)

        # Create an accuracy label
        accuracy_label = tk.Label(main_form, text="Accuracy:")
        accuracy_label.grid(row=10, column=0, pady=10)

        # Create a StringVar to update accuracy dynamically
        accuracy_var = tk.StringVar()
        accuracy_var.set("Accuracy: -")  # You can initialize it with a default value

        # Create a label to display the accuracy value
        accuracy_display_label = tk.Label(main_form, textvariable=accuracy_var)
        accuracy_display_label.grid(row=10, column=0, pady=10)

        # Calculate and update the accuracy value
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_var.set(f"Accuracy: {accuracy * 100:.2f}%")

        # Start the main loop
        main_form.mainloop()

# Check if the script is being run as the main program
if __name__ == "__main__":
    app = TitanicSurvivorClassifier()
    app.login_window.mainloop()
