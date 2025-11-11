"""
Authentication API endpoints
QCA-1: Implement secure user authentication endpoint with rate limiting

INTENTIONAL ISSUES FOR TESTING:
- Missing input validation
- Missing rate limiting
- Missing audit logging
- Hardcoded secret key
- No security headers
- Missing error handling
- No token expiry
- Plain password comparison (should use bcrypt)
"""

from flask import Flask, request, jsonify
import jwt
from backend.models.user import User

app = Flask(__name__)

@app.route('/api/auth/login', methods=['POST'])
def login():
    """
    Login endpoint - INTENTIONALLY INCOMPLETE
    References: QCA-1
    
    This implementation is intentionally missing most requirements
    to test if Qodo flags them based on the Jira ticket.
    """
    
    # ISSUE 1: No input validation - will crash if fields missing
    email = request.json['email']
    password = request.json['password']
    
    # ISSUE 2: No email format validation (QCA-1 AC #1)
    # ISSUE 3: No password length check (QCA-1 AC #1)
    
    # ISSUE 4: Direct database query without any error handling
    user = User.find_by_email(email)
    
    # ISSUE 5: Plain text password comparison instead of bcrypt (QCA-1 AC #2)
    # ISSUE 6: Reveals if email exists (violates QCA-1 AC #2 security requirement)
    if user and user['password_hash'] == password:
        
        # ISSUE 7: Hardcoded secret key (violates QCA-1 AC #3)
        # ISSUE 8: No token expiry (violates QCA-1 AC #3)
        # ISSUE 9: Missing required token payload fields (violates QCA-1 AC #3)
        token = jwt.encode(
            {'user_id': user['id']},
            'hardcoded-secret-key-123',
            algorithm='HS256'
        )
        
        # ISSUE 10: No audit logging (violates QCA-1 AC #5)
        # ISSUE 11: No rate limiting (violates QCA-1 AC #4)
        # ISSUE 12: Missing security headers (violates QCA-1 AC #6)
        
        return jsonify({'token': token})
    
    # ISSUE 13: Generic error message is actually correct, but missing error_code field
    return jsonify({'error': 'Login failed'}), 401


@app.route('/api/auth/register', methods=['POST'])
def register():
    """Simple registration endpoint for testing"""
    return jsonify({'message': 'Registration not implemented yet'}), 501


if __name__ == '__main__':
    app.run(debug=True, port=5000)
