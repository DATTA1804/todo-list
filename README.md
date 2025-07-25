# 📝 Todo List App with Flask & MongoDB

A modern, responsive and full-featured todo list web application built with **Flask** for the backend and **MongoDB** for persistent storage.

---

## 🚀 Features

- ✅ Add, edit, delete todo tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Store data persistently with MongoDB
- ✅ View todo stats (total, completed, pending)
- ✅ Flash messages for user feedback
- ✅ Timestamps for created and updated todos
- ✅ Beautiful responsive UI (HTML templates required in `templates/`)
- ✅ Clean modular code with database abstraction

---

## 📂 Project Structure

├── app.py # Main Flask application//
├── database.py # MongoDB operations encapsulated in a class
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── test_mongodb.py # MongoDB connection & operation tests
├── test_persistence.py # Persistence check for todo items
├── templates/ # HTML templates (not included here)
└── static/ # Static assets like CSS (not included here)
