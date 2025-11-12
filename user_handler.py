import sqlite3

# Database configuration
DB_PASSWORD = "admin123"  # Hardcoded password - security issue!

def get_user_data(user_id):
    """Fetch user data from database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL injection vulnerability - no parameterization!
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    # Missing connection close and error handling
    return result

def process_user_login(username, password):
    """Process user login with poor error handling"""
    u = get_user_data(username)  # Wrong - passing username as user_id
    
    # No validation or sanitization
    if u:
        # Using utility function from utils.py but not importing it
        formatted = format_string(u[1])  # This will fail - utils not imported
        return True
    return False

def calculate_discount(a, b, c):
    """Calculate discount with unclear variable names"""
    # What do a, b, c mean? Poor naming!
    x = a * b
    if c:
        return x * 0.9
    return x

class UserManager:
    def __init__(self):
        self.data = None
    
    def update_user(self, user_dict):
        """Update user with no type checking or validation"""
        # Direct SQL without any sanitization
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        sql = f"UPDATE users SET name='{user_dict['name']}', email='{user_dict['email']}' WHERE id={user_dict['id']}"
        cursor.execute(sql)
        conn.commit()
        # Missing error handling and connection close
```

4. **Scroll down to "Commit changes"**
5. **Commit message:** "Add user handler with various issues for testing"
6. **Make sure** "Commit directly to the test-pr-comparison branch" is selected
7. Click **"Commit changes"**

---

## Step 3: Create the Pull Request

1. You should see a yellow banner saying "test-pr-comparison had recent pushes"
2. Click **"Compare & pull request"** (green button)
3. **Title:** "Test: User authentication handler"
4. **Description:** 
```
Adding user authentication and database handler.

Related to improving user management system.

