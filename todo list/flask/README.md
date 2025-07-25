# Todo List App with MongoDB

A modern, responsive todo list application built with Flask and MongoDB.

## Features

- ✅ **Add new todos** with title and optional description
- ✅ **Mark todos as complete/incomplete** 
- ✅ **Edit existing todos**
- ✅ **Delete todos** with confirmation
- ✅ **View todo statistics** (total, completed, pending)
- ✅ **Persistent storage** with MongoDB
- ✅ **Responsive design** that works on mobile and desktop
- ✅ **Beautiful UI** with modern styling
- ✅ **Flash messages** for user feedback
- ✅ **Timestamps** for creation and updates

## Prerequisites

### Option 1: Local MongoDB Installation
1. **Install MongoDB Community Server**
   - Download from: https://www.mongodb.com/try/download/community
   - Follow the installation guide for your operating system
   - Start MongoDB service

### Option 2: MongoDB Atlas (Cloud)
1. **Create a free MongoDB Atlas account**
   - Go to: https://www.mongodb.com/atlas
   - Create a free cluster
   - Get your connection string
   - Update the `MONGODB_URI` environment variable or modify `database.py`

## Installation

1. **Clone or download this project**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB connection (if using Atlas)**
   ```bash
   # Windows
   set MONGODB_URI=your_mongodb_atlas_connection_string
   
   # Linux/Mac
   export MONGODB_URI=your_mongodb_atlas_connection_string
   ```

## Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to**
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```
flask/
├── app.py              # Main Flask application
├── database.py         # MongoDB database operations
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/         # HTML templates
│   ├── index.html     # Main todo list page
│   └── edit.html      # Edit todo page
└── static/           # Static files
    └── style.css     # CSS styling
```

## Database Schema

### Todo Document Structure
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## API Endpoints

- `GET /` - Display all todos
- `POST /add` - Add a new todo
- `GET /complete/<todo_id>` - Toggle todo completion status
- `GET /delete/<todo_id>` - Delete a todo
- `GET /edit/<todo_id>` - Display edit form
- `POST /edit/<todo_id>` - Update a todo

## Configuration

### Environment Variables
- `MONGODB_URI` - MongoDB connection string (default: `mongodb://localhost:27017/`)

### Security
- Change the `secret_key` in `app.py` for production use
- Use environment variables for sensitive configuration

## Troubleshooting

### MongoDB Connection Issues
1. **Local MongoDB not running**
   - Start MongoDB service
   - Check if MongoDB is listening on port 27017

2. **MongoDB Atlas connection issues**
   - Verify your connection string
   - Check network access settings in Atlas
   - Ensure your IP is whitelisted

3. **Permission errors**
   - Check MongoDB user permissions
   - Verify database access rights

### Common Error Messages
- `Failed to connect to MongoDB` - Check MongoDB installation/service
- `Database connection failed` - Verify connection string and network access

## Development

### Adding New Features
1. Database operations go in `database.py`
2. Routes and logic go in `app.py`
3. HTML templates go in `templates/`
4. CSS styling goes in `static/style.css`

### Testing
- Add sample todos to test functionality
- Test on different screen sizes for responsiveness
- Verify MongoDB operations in MongoDB Compass or shell

## Production Deployment

1. **Set environment variables**
   - `MONGODB_URI` for database connection
   - `SECRET_KEY` for Flask sessions

2. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Configure reverse proxy** (nginx, Apache)

4. **Enable HTTPS** for secure connections

## License

This project is open source and available under the MIT License.