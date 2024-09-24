# Python API with MongoDB and Docker

## Project Overview

This project is a simple RESTful API built with **Flask** that connects to a **MongoDB** database. The project is containerized using **Docker**.

The API supports basic operations such as retrieving and adding users. It connects to a MongoDB Atlas database (cloud-based) and can be run locally using Docker.

## Features

- **GET /users**: Fetch all users from the MongoDB collection.
- **POST /users**: Add a new user to the MongoDB collection.
- Containerized using **Docker** for easy setup and portability.

## Prerequisites

Before running this project, you need to have the following installed:

- **Docker** and **Docker Compose**
- A **MongoDB Atlas account** (or a local MongoDB instance)
- **Postman** (optional, for API testing)


## Project Structure
/PythonAPIF2024
│
├── Dockerfile               # Dockerfile to build the Flask app
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          # Python dependencies
├── app.py                    # Flask API code
├── README.md                 # Project README
└── .gitignore                # Git ignore file

# API Endpoints:
## GET /users:
Retrieves all users from the Users collection in MongoDB.

Example request:
### GET http://localhost:5000/users


## POST /users:
Adds a new user to the Users collection in MongoDB.

Example request:
### POST http://localhost:5000/users


JSON Body:

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}