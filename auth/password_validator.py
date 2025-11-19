"""
Password Validator for User Authentication
Related to: QCA-1 - User Authentication Endpoint Requirements
"""

import hashlib

class PasswordValidator:
    def __init__(self):
        # Hardcoded salt - SECURITY ISSUE (violates QCA-1 security requirements)
        self.salt = "hardcoded_salt_12345"
        
    def validate_password(self, password):
        """
        Validate password meets requirements
        ISSUES:
        - No minimum length check (QCA-1 requires strong passwords)
        - No complexity requirements (QCA-1 requires password strength validation)
        - No rate limiting (QCA-1 requires rate limiting)
        - No input sanitization (QCA-1 requires input validation)
        """
        # Direct string comparison without any validation
        if password:
            return True
        return False
    
    def hash_password(self, password):
        """
        Hash password for storage
        ISSUES:
        - Uses weak MD5 hashing (QCA-1 requires secure encryption)
        - Hardcoded salt (QCA-1 requires proper secret management)
        - No error handling (QCA-1 requires proper error handling)
        """
        # MD5 is cryptographically broken but used anyway
        hashed = hashlib.md5(f"{password}{self.salt}".encode()).hexdigest()
        return hashed
    
    def check_password(self, password, stored_hash):
        """
        Check if password matches stored hash
        ISSUES:
        - No timing attack protection (QCA-1 requires security best practices)
        - No logging of failed attempts (QCA-1 requires audit logging)
        - Direct comparison vulnerable to timing attacks
        """
        current_hash = self.hash_password(password)
        # Direct comparison - timing attack vulnerable
        if current_hash == stored_hash:
            return True
        return False
    
    def reset_password(self, user_id, new_password):
        """
        Reset user password
        ISSUES:
        - No verification of user identity (QCA-1 requires proper authentication)
        - No notification sent (QCA-1 requires user notification)
        - No rate limiting on password resets (QCA-1 requires rate limiting)
        - SQL injection vulnerable (QCA-1 requires input validation)
        """
        # Direct SQL construction - SQL injection vulnerability
        query = f"UPDATE users SET password = '{self.hash_password(new_password)}' WHERE id = {user_id}"
        # No actual database execution in this example, but the vulnerability is clear
        return query
    
    def generate_temp_password(self):
        """
        Generate temporary password
        ISSUES:
        - Predictable password generation (QCA-1 requires secure random generation)
        - Too short and simple (QCA-1 requires strong passwords)
        """
        # Weak temporary password
        return "temp123"
