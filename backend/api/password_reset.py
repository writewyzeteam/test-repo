# Documentation URL: https://github.com/writewyzeteam/test-repo

from flask import Blueprint, request, jsonify
import secrets
import smtplib
from datetime import datetime

password_reset_bp = Blueprint('password_reset', __name__)

@password_reset_bp.route('/api/reset-password-request', methods=['POST'])
def request_password_reset():
    """Request password reset - intentionally incomplete implementation"""
    email = request.json.get('email')
    
    # Missing: email format validation
    # Missing: rate limiting check
    
    # Generate token (but uses wrong method - not cryptographically secure)
    token = str(datetime.now().timestamp())  # WRONG: not secure
    
    # Missing: token expiry time (30 minutes requirement)
    # Missing: single-use token enforcement
    
    # Send email (mock)
    reset_link = f"https://example.com/reset?token={token}"  # WRONG: should be /reset-password
    
    # Missing: security audit logging
    
    return jsonify({
        'message': 'Password reset email sent',
        'token': token  # WRONG: shouldn't return token in response
    }), 200


@password_reset_bp.route('/api/reset-password', methods=['POST'])
def reset_password():
    """Reset password with token"""
    token = request.json.get('token')
    new_password = request.json.get('password')
    
    # Missing: token validation
    # Missing: session invalidation
    # Uses MD5 instead of bcrypt (wrong)
    import hashlib
    hashed = hashlib.md5(new_password.encode()).hexdigest()
    
    # Missing: audit logging
    
    return jsonify({'message': 'Password reset successful'}), 200
https://writewyzeteam.atlassian.net/browse/QCA-3
