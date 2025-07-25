#!/usr/bin/env python3
"""
MongoDB Connection Test Script
Run this script to test your MongoDB connection before starting the Flask app.
"""

from database import TodoDatabase
import sys

def test_mongodb_connection():
    print("🔍 Testing MongoDB connection...")
    print("-" * 50)
    
    try:
        # Initialize database connection
        db = TodoDatabase()
        print("✅ Successfully connected to MongoDB!")
        
        # Test basic operations
        print("\n📊 Testing database operations...")
        
        # Get current stats
        stats = db.get_todo_stats()
        print(f"📈 Current todos in database: {stats['total']}")
        print(f"   - Completed: {stats['completed']}")
        print(f"   - Pending: {stats['pending']}")
        
        # Test creating a todo
        print("\n🆕 Testing todo creation...")
        test_id = db.create_todo("Test Todo", "This is a test todo created by the connection test script")
        print(f"✅ Created test todo with ID: {test_id}")
        
        # Test retrieving the todo
        print("\n📖 Testing todo retrieval...")
        test_todo = db.get_todo_by_id(test_id)
        if test_todo:
            print(f"✅ Retrieved todo: {test_todo['title']}")
        else:
            print("❌ Failed to retrieve test todo")
            
        # Test updating the todo
        print("\n✏️ Testing todo update...")
        update_success = db.update_todo(test_id, "Updated Test Todo", "This todo was updated by the test script")
        if update_success:
            print("✅ Successfully updated test todo")
        else:
            print("❌ Failed to update test todo")
            
        # Test toggling completion
        print("\n🔄 Testing completion toggle...")
        toggle_success, new_status = db.toggle_todo_completion(test_id)
        if toggle_success:
            print(f"✅ Successfully toggled completion status to: {new_status}")
        else:
            print("❌ Failed to toggle completion status")
            
        # Clean up - delete the test todo
        print("\n🗑️ Cleaning up test todo...")
        delete_success = db.delete_todo(test_id)
        if delete_success:
            print("✅ Successfully deleted test todo")
        else:
            print("❌ Failed to delete test todo")
            
        # Final stats
        final_stats = db.get_todo_stats()
        print(f"\n📊 Final stats - Total todos: {final_stats['total']}")
        
        # Close connection
        db.close_connection()
        
        print("\n" + "=" * 50)
        print("🎉 All tests passed! MongoDB is working correctly.")
        print("🚀 You can now run the Flask app with: python app.py")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection test failed!")
        print(f"Error: {str(e)}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Make sure MongoDB is installed and running")
        print("   - Local: Start MongoDB service")
        print("   - Atlas: Check your connection string")
        print("2. Verify your connection string in database.py")
        print("3. Check firewall and network settings")
        print("4. For Atlas: Ensure your IP is whitelisted")
        
        return False

if __name__ == "__main__":
    success = test_mongodb_connection()
    sys.exit(0 if success else 1)