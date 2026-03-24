# 🚀 FastAPI JWT Authentication API and integration between DATABASE.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Project Description 

This is a production-style backend API built using **FastAPI + MySQL + JWT Authentication + Python**.

The project includes:

* User Registration
* Login with password hashing
* JWT Token Authentication
* Protected Routes
* MySQL Database connection
* SQLAlchemy ORM
* Clean project structure

This project is created for learning **real backend development** and follows a professional API structure.

---

## 🛠 Tech Stack

* Python 3.11+
* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)
* Python-JOSE (JWT)
* Uvicorn

---

## 📂 Project Structure

```
FASTAPI-PYTHON/
│
├── app/
│   ├── main.py
│   ├── database.py
│
│   ├── models/
│   │   └── user.py
│
│   ├── schemas/
│   │   └── user.py
│
│   ├── routes/
│   │   └── user.py
│
│   ├── utils/
│   │   ├── hash.py
│   │   └── jwt.py
│
├── requirements.txt
├── README.md
└── venv/
```

---

## ⚙️ Installation

## Create EC2 instance/server on AWS (OS-linux/ubuntu)
## Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```
## Install dependencies
## Setup MySQL Database
## Create database in MySQL
## Update database URL in

Example:

```
mysql+pymysql://root:password@localhost/fastapi_db
```

## Run server

```
venv\Scripts\activate
python -m uvicorn app.main:app --reload
uvicorn app.main:app --reload
```

## Open Swagger UI

```
http://127.0.0.1:8000/docs
```

## 🔐 Features

* ✅ Register User API
* ✅ Login API
* ✅ Password Hashing (bcrypt)
* ✅ JWT Token Authentication
* ✅ Authentication & Authorization
* ✅ Protected Routes
* ✅ MySQL Integration
* ✅ SQLAlchemy ORM
* ✅ FastAPI Docs (Swagger)

---


## 📌 API Endpoints

| Method | Endpoint      | Description   | Auth Required    |
| ------ | ------------- | ------------- | -----------------|
| POST   | /db/user      | Register User |  Yes             |
| POST   | /login        | Login User    |  Yes             |
| GET    | /profile      | Get Profile   |  Yes (JWT Token) |
| PUT    | /db/user/{id} | Update User   |  Yes (JWT Token) |
| DELETE | /db/user/{id} | Delete User   |  Yes (JWT Token) |
| GET    | /docs         | Swagger UI    |  Yes             |

---

## 🔐 Authentication

Protected routes require JWT token in header.

Example header:

```
token: your_jwt_token_here
```

Flow:

```
Register → Login → JWT Token → Protected API → Update → Delete
```


---

## 🔑 Authentication Flow

```
Register → Hash Password → Login → JWT Token → Protected API
```

---

## 🧪 Testing

Use Swagger UI

```
http://127.0.0.1:8000/docs
```

Or use Postman.

---

## 📌 Future Improvements

*  Role based auth
* Refresh token
* Email login
* Docker support
* Deployment on AWS / VPS
  

---

## 👨‍💻 Author

Your Name
Shubham Nitin Ahire
FastAPI | Python | MySQL | JWT | AWS DEVOPS 

GitHub: https://github.com/shubhamahire9168
