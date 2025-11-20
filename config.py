
[200~"""
Configuration settings for the authentication API
QCA-1 related configuration
"""

import os

class Config:
    """Application configuration"""
    
    # QCA-1 requires environment-based secret key
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'hardcoded-secret-key-123')
    
    # QCA-1 requires 24 hour token expiry
    JWT_EXPIRY_HOURS = 24
    
    # QCA-1 requires rate limiting
    RATE_LIMIT_PER_MINUTE = 5
    
    # QCA-1 requires Redis for rate limiting
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
EOF~
