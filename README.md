# Test Authentication API

This is a test repository for evaluating AI code quality tools (Qodo, Cursor, etc.).

## Purpose

Testing if AI tools can:
1. Read Jira ticket requirements (QCA-1)
2. Identify missing implementations
3. Validate code against acceptance criteria
4. Provide context-aware suggestions

## QCA-1 Requirements

This repo implements (intentionally incomplete) the requirements from Jira ticket **QCA-1**: 
"Implement secure user authentication endpoint with rate limiting"

## Known Issues (Intentional)

The `/api/auth/login` endpoint is deliberately incomplete to test AI code review capabilities:

- ❌ Missing input validation
- ❌ Missing rate limiting  
- ❌ Missing audit logging
- ❌ Hardcoded secret key
- ❌ No token expiry
- ❌ Plain text password comparison
- ❌ Missing security headers
- ❌ No error handling

## Setup
```bash
pip install -r requirements.txt
python backend/api/auth.py
```

## Testing
```bash
# Test login endpoint
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

## Related Tickets

- QCA-1: User authentication endpoint (this implementation)
- QCA-2: Password reset (planned)
- QCA-3: User profile update (planned)
