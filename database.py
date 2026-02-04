import sqlite3
import datetime

# This will create a file named 'farm_data.db' in your folder automatically
DB_NAME = "farm_data.db"

# --- 1. SETUP TABLES ---
def create_tables():
    """Creates the necessary tables if they don't exist yet."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # USERS TABLE (Stores Login Info)
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        email TEXT,
        full_name TEXT,
        phone TEXT,
        joined_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # SCANS TABLE (Stores AI Doctor History)
    c.execute('''CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        crop_type TEXT,
        diagnosis TEXT,
        confidence REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        image_data BLOB,
        FOREIGN KEY(username) REFERENCES users(username)
    )''')
    
    conn.commit()
    conn.close()

# --- 2. AUTHENTICATION FUNCTIONS ---
def add_user(username, password, email):
    """Registers a new user. Returns True if successful, False if username exists."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                  (username, password, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # This happens if username already exists
    finally:
        conn.close()

def get_user(username):
    """Fetches user details for login."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    conn.close()
    return data

# --- 3. PROFILE FUNCTIONS ---
def update_profile_info(username, full_name, phone):
    """Updates user profile details."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET full_name=?, phone=? WHERE username=?", 
              (full_name, phone, username))
    conn.commit()
    conn.close()