from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from database import TodoDatabase

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Initialize database connection
try:
    db = TodoDatabase()
    print("✅ Database initialized successfully!")
except Exception as e:
    print(f"❌ Failed to initialize database: {e}")
    db = None

@app.route("/")
def index():
    if db is None:
        flash('Database connection failed. Please check your MongoDB setup.', 'error')
        return render_template('index.html', todos=[])
    
    todos = db.get_all_todos()
    return render_template('index.html', todos=todos)

@app.route("/add", methods=['POST'])
def add_todo():
    if db is None:
        flash('Database connection failed. Cannot add todo.', 'error')
        return redirect(url_for('index'))
    
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('index'))
    
    try:
        todo_id = db.create_todo(title, description)
        flash('Todo added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route("/complete/<todo_id>")
def complete_todo(todo_id):
    if db is None:
        flash('Database connection failed. Cannot update todo.', 'error')
        return redirect(url_for('index'))
    
    try:
        success, new_status = db.toggle_todo_completion(todo_id)
        if success:
            status = 'completed' if new_status else 'uncompleted'
            flash(f'Todo marked as {status}!', 'success')
        else:
            flash('Todo not found or could not be updated.', 'error')
    except Exception as e:
        flash(f'Error updating todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route("/delete/<todo_id>")
def delete_todo(todo_id):
    if db is None:
        flash('Database connection failed. Cannot delete todo.', 'error')
        return redirect(url_for('index'))
    
    try:
        success = db.delete_todo(todo_id)
        if success:
            flash('Todo deleted successfully!', 'success')
        else:
            flash('Todo not found or could not be deleted.', 'error')
    except Exception as e:
        flash(f'Error deleting todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit_todo(todo_id):
    if db is None:
        flash('Database connection failed. Cannot edit todo.', 'error')
        return redirect(url_for('index'))
    
    try:
        todo = db.get_todo_by_id(todo_id)
        
        if not todo:
            flash('Todo not found!', 'error')
            return redirect(url_for('index'))
        
        if request.method == 'POST':
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            
            if not title:
                flash('Title is required!', 'error')
                return render_template('edit.html', todo=todo)
            
            success = db.update_todo(todo_id, title, description)
            if success:
                flash('Todo updated successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Failed to update todo.', 'error')
                return render_template('edit.html', todo=todo)
        
        return render_template('edit.html', todo=todo)
    
    except Exception as e:
        flash(f'Error editing todo: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
    