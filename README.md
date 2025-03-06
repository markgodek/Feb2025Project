# Feb2025Project
The goal of the project is to simulate a source of streaming data (for example, a robot which takes photos of cell cultures) which includes text and an image and process the data into a database which can be queried by an end user. The project will be containerized using Docker in order to be portable and run on any machine as a demonstration.

## data_generator.py:
Generates random images and the following fields: ID, Timestamp, Cell line, Perturbation, Image File Name and sends the data to ThingsBoard using the MQTT messaging protocol

## firebase_export.py
A script which uses the Firebase Admin API to extract the database entries and export them to a local JSON file. The script then deletes the contents of the database so it is fresh for the next demonstration.

## ThingsBoard Container:
Sets up an instance of ThingsBoard, a GUI for managing IoT devices and their dataflows. In this demonstration, a ThingsBoard node checks an arbitrary metric of cell culture health and if the value is above 50, it is posted to a realtime database on Google Firebase and if the value is below 50, an alarm is created and posted to the same database.

## MQTT Container:
Sets up an instance of an MQTT broker which allows the python script to talk to the ThingsBoard instance via an MQTT client.

## Instructions:
1. Run docker-compose up on Feb2025Project\MQTT\docker-compose.yml
2. Run docker-compose up on Feb2025Project\ThingsBoard\docker-compose.yml
4. Wait a few moments to allow the ThingsBoard instance time to spin up
5. Connect to http://localhost:8080/ in a web browser with the following credentials:
   Login: tenant@thingsboard.org
   Password: tenant
6. Run data_generator.py using python 3.11
7. After the data generator script has run for a few moments, stop the script and run firebase_export.py to export the contents of the Realtime Database in JSON format
