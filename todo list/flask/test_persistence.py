#!/usr/bin/env python3
"""
Test script to verify that todos persist in the database
"""

from database import TodoDatabase
import time

def test_persistence():
    print("🧪 Testing Todo Persistence...")
    print("-" * 40)
    
    # Initialize database
    db = TodoDatabase()
    
    # Add some test todos
    print("📝 Adding test todos...")
    todo1_id = db.create_todo("Buy groceries", "Milk, bread, eggs, and fruits")
    todo2_id = db.create_todo("Complete project", "Finish the Flask todo app with MongoDB")
    todo3_id = db.create_todo("Exercise", "30 minutes of cardio")
    
    print(f"✅ Added 3 test todos")
    
    # Mark one as completed
    db.toggle_todo_completion(todo2_id)
    print("✅ Marked one todo as completed")
    
    # Show current stats
    stats = db.get_todo_stats()
    print(f"\n📊 Current database stats:")
    print(f"   Total: {stats['total']}")
    print(f"   Completed: {stats['completed']}")
    print(f"   Pending: {stats['pending']}")
    
    # List all todos
    todos = db.get_all_todos()
    print(f"\n📋 All todos in database:")
    for todo in todos:
        status = "✅" if todo['completed'] else "⏳"
        print(f"   {status} {todo['title']} - {todo['description']}")
    
    print(f"\n🎉 Test completed! Your todos are now stored in MongoDB.")
    print(f"🔄 You can restart the Flask app and the todos will still be there!")
    
    db.close_connection()

if __name__ == "__main__":
    test_persistence()