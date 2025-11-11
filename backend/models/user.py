"""
User model for the authentication system.
This would normally connect to a database, but for testing purposes,
we'll use a simple in-memory store.
"""

class User:
    """User model with basic authentication fields"""
    
    # In-memory user store for testing
    _users = [
        {
            'id': 1,
            'email': 'test@example.com',
            'name': 'Test User',
            'password_hash': '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYfYC.5N6jO',  # "password123"
            'is_active': True
        },
        {
            'id': 2,
            'email': 'admin@example.com',
            'name': 'Admin User',
            'password_hash': '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYfYC.5N6jO',  # "password123"
            'is_active': True
        }
    ]
    
    @classmethod
    def find_by_email(cls, email):
        """Find user by email address"""
        for user in cls._users:
            if user['email'] == email:
                return user
        return None
    
    @classmethod
    def get_by_id(cls, user_id):
        """Get user by ID"""
        for user in cls._users:
            if user['id'] == user_id:
                return user
        return None
