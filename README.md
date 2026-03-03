💰 Finance API Backend

A RESTful backend API built using Flask and MongoDB to manage structured personal finance data.
This project is designed to practice full CRUD operations using complex nested JSON datasets.

📌 Project Overview

This backend system simulates real-world personal finance management data, including:

Transaction Categories

Transactions

Monthly Budgets

Financial Goals

Alerts

The API allows creating, reading, updating, and deleting financial records stored in MongoDB.

🛠 Tech Stack

Python

Flask

MongoDB

PyMongo

Postman

🗂 Dataset Structure

Each user document contains nested financial data:

{
  "user_id": 1,
  "name": "John",
  "categories": [],
  "expenses": [],
  "monthly_budgets": [],
  "alerts": []
}

The dataset is generated using a custom Python script to simulate realistic financial activity.

🚀 Features

RESTful API design

Pagination support

Nested JSON handling

MongoDB document storage

Error handling

Localhost testing with Postman

🔌 API Endpoints
Get All Users
GET /api/users?pn=1&ps=10
Get One User
GET /api/users/<mongo_id>
Add User
POST /api/users
Update User
PUT /api/users/<mongo_id>
Delete User
DELETE /api/users/<mongo_id>
▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/finance-api-backend.git
cd finance-api-backend
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment (Windows)
.\venv\Scripts\Activate
4️⃣ Install Dependencies
pip install flask pymongo
5️⃣ Run the Server
python app.py

Server will run at:

http://127.0.0.1:5001
📬 Testing

Use Postman to test endpoints locally.

🎯 Purpose of This Project

This project was built to strengthen backend development skills, including:

API design

MongoDB data modeling

Nested JSON handling

CRUD implementation

Backend debugging
