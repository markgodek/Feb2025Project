# Feb2025Project
The goal of the project is to simulate a source of streaming data which includes text and an image and process the data into a database which can be queried by an end user. The project will be containerized using Docker in order to be portable and run on any machine as a demonstration.

Data generator:
Create data with the following fields: ID, Timestamp, Cell line, Perturbation, Image File Name

Instructions:
1. Run docker-compose up on Feb2025Project\Mosquitto\docker-compose.yml
2. Run docker-compose up on Feb2025Project\ThingsBoard\docker-compose.yml
3. Connect to http://localhost:8080/ in a web browser
   Login: tenant@thingsboard.org
   Password: tenant
4. 