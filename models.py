from database import get_connection

def get_all_tasks():
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    return [dict(t) for t in tasks]

def add_task(title):
    conn = get_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()

def delete_task(task_id):
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def mark_done(task_id):
    conn = get_connection()
    conn.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))
    conn.commit()