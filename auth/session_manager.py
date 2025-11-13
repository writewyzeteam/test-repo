"""
Session Manager for User Authentication
Related to: QCA-1 - User Authentication Endpoint Requirements
"""

import time
import secrets

class SessionManager:
    def __init__(self):
        # Hardcoded session secret - SECURITY ISSUE (violates QCA-1)
        self.session_secret = "super_secret_key_123"
        self.sessions = {}
        
    def create_session(self, user_id):
        """
        Create a new session for user
        ISSUES:
        - No session expiration (QCA-1 requires proper session management)
        - Predictable session IDs (QCA-1 requires secure random generation)
        - No rate limiting (QCA-1 requires rate limiting)
        """
        # Predictable session ID - just incrementing counter
        session_id = f"session_{len(self.sessions) + 1}"
        self.sessions[session_id] = {
            'user_id': user_id,
            'created_at': time.time()
        }
        return session_id
    
    def validate_session(self, session_id):
        """
        Validate if session is active
        ISSUES:
        - No expiration check (QCA-1 requires session timeout)
        - No logging of validation attempts (QCA-1 requires audit logging)
        - Sessions never expire (QCA-1 requires proper security controls)
        """
        # Just check if session exists, no expiration logic
        return session_id in self.sessions
    
    def get_user_from_session(self, session_id):
        """
        Get user ID from session
        ISSUES:
        - No input validation (QCA-1 requires input validation)
        - No error handling (QCA-1 requires proper error handling)
        """
        # Direct dictionary access without validation
        return self.sessions[session_id]['user_id']
