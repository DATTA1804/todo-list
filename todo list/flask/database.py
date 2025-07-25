from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os

class TodoDatabase:
    def __init__(self):
        # MongoDB connection string - you can modify this for your setup
        # For local MongoDB: mongodb://localhost:27017/
        # For MongoDB Atlas: use your connection string
        self.connection_string = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
        self.database_name = 'todo_app'
        self.collection_name = 'todos'
        
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]
            
            # Test the connection
            self.client.admin.command('ping')
            print("✅ Connected to MongoDB successfully!")
            
        except Exception as e:
            print(f"❌ Failed to connect to MongoDB: {e}")
            print("📝 Make sure MongoDB is running on your system")
            print("   - Install MongoDB Community Server from: https://www.mongodb.com/try/download/community")
            print("   - Or use MongoDB Atlas (cloud): https://www.mongodb.com/atlas")
            raise e
    
    def create_todo(self, title, description=""):
        """Create a new todo item"""
        todo = {
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        
        result = self.collection.insert_one(todo)
        return str(result.inserted_id)
    
    def get_all_todos(self):
        """Get all todos, sorted by creation date (newest first)"""
        todos = list(self.collection.find().sort('created_at', -1))
        
        # Convert ObjectId to string for JSON serialization
        for todo in todos:
            todo['_id'] = str(todo['_id'])
            # Format dates for display
            todo['created_at_formatted'] = todo['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            todo['updated_at_formatted'] = todo['updated_at'].strftime('%Y-%m-%d %H:%M:%S')
        
        return todos
    
    def get_todo_by_id(self, todo_id):
        """Get a specific todo by ID"""
        try:
            todo = self.collection.find_one({'_id': ObjectId(todo_id)})
            if todo:
                todo['_id'] = str(todo['_id'])
                todo['created_at_formatted'] = todo['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                todo['updated_at_formatted'] = todo['updated_at'].strftime('%Y-%m-%d %H:%M:%S')
            return todo
        except Exception as e:
            print(f"Error getting todo: {e}")
            return None
    
    def update_todo(self, todo_id, title, description=""):
        """Update a todo item"""
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(todo_id)},
                {
                    '$set': {
                        'title': title,
                        'description': description,
                        'updated_at': datetime.now()
                    }
                }
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating todo: {e}")
            return False
    
    def toggle_todo_completion(self, todo_id):
        """Toggle the completion status of a todo"""
        try:
            todo = self.collection.find_one({'_id': ObjectId(todo_id)})
            if todo:
                new_status = not todo['completed']
                result = self.collection.update_one(
                    {'_id': ObjectId(todo_id)},
                    {
                        '$set': {
                            'completed': new_status,
                            'updated_at': datetime.now()
                        }
                    }
                )
                return result.modified_count > 0, new_status
            return False, False
        except Exception as e:
            print(f"Error toggling todo: {e}")
            return False, False
    
    def delete_todo(self, todo_id):
        """Delete a todo item"""
        try:
            result = self.collection.delete_one({'_id': ObjectId(todo_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting todo: {e}")
            return False
    
    def get_todo_stats(self):
        """Get statistics about todos"""
        total = self.collection.count_documents({})
        completed = self.collection.count_documents({'completed': True})
        pending = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending
        }
    
    def close_connection(self):
        """Close the database connection"""
        if hasattr(self, 'client'):
            self.client.close()
            print("🔌 MongoDB connection closed")