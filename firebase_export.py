# A script which uses a credentials file to export the contents of a Firebase Realtime Database

import firebase_admin
from firebase_admin import credentials, db
import json
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the service account credentials file
cred_path = os.path.join(current_dir, 'cultureimagerproject-firebase-adminsdk-fbsvc-a85bf7756b.json')

# Initialize Firebase Admin SDK with the relative path to the service account credentials
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cultureimagerproject-default-rtdb.firebaseio.com/'
})

# Function to fetch data from Firebase Realtime Database and save to a text file
def save_data_to_file():
    try:
        # Reference to the Firebase Realtime Database root
        ref = db.reference('/')

        # Fetch data from the database
        data = ref.get()

        # Open a text file to save the data
        with open('firebase_data.txt', 'w') as file:
            # Convert data to JSON format and write it to the file
            json.dump(data, file, indent=4)

        print("Data successfully saved to firebase_data.txt")

        # Clear the demonstration database after the data has been exported
        ref.delete()
        print("Realtime Database has been deleted.")

    except Exception as e:
        print(f"Error saving data: {e}")

# Call the function to save data
save_data_to_file()
