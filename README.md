# 📝 Task Manager API

A simple RESTful backend API for managing tasks using Flask, JWT authentication, and SQLite.  
This project includes user registration/login, token-based authentication, and full CRUD operations for tasks.

---

## 🚀 Live Demo

> 🌐 [Here](https://task-management-mh6r.onrender.com/api/tasks)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
```bash
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
DATABASE_URI=sqlite:///data.db
```

### 5. Run the Server
```bash
python run.py
```

## 👨‍💻 Author
Built by Anmol