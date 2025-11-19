// Initial insecure authentication attempt
const express = require('express');
const router = express.Router();

router.post('/login', (req, res) => {
    const { username, password } = req.body;
    
    // Direct password comparison - security issue
    const user = users.find(u => u.username === username && u.password === password);
    
    if (user) {
        res.json({ success: true, token: generateToken(user) });
    } else {
        res.status(401).json({ success: false });
    }
});

module.exports = router;
```

### 4. Commit the file
1. Scroll down to "Commit new file" section
2. Commit message: `Add user login endpoint`
3. Make sure "Commit directly to the feature/insecure-auth-v1 branch" is selected
4. Click "Commit new file"

### 5. Create the Pull Request
1. You should see a yellow banner at the top saying "feature/insecure-auth-v1 had recent pushes" 
2. Click the green "Compare & pull request" button

**If you don't see the banner:**
1. Click "Pull requests" tab
2. Click "New pull request" 
3. Change "compare:" dropdown to `feature/insecure-auth-v1`
4. Click "Create pull request"

### 6. Fill in PR details

**Title:**
```
Add user login endpoint
```

**Description (paste this in the comment box):**
```
Implements basic user authentication for the login endpoint.

Changes:
- Added POST /login route
- Returns JWT token on successful auth
- Returns 401 on failed auth
```

### 7. Click "Create pull request"

### 8. Wait for automated tool reviews
- Give it 1-2 minutes
- You should see comments appear from Qodo, CodeRabbit, Greptile, etc.
- Take screenshots of what each tool says

### 9. Add your human reviewer feedback

**Method 1 - Add review comment on specific line:**
1. Click "Files changed" tab at the top of the PR
2. Find line 9 (the line with `const user = users.find...`)
3. Hover your mouse over the line number
4. Click the blue "+" icon that appears
5. Paste this comment:
```
❌ REJECTED: Direct password comparison is a security vulnerability.

Our security policy requires:
1. Passwords must be hashed using bcrypt (min 12 rounds)
2. Use timing-safe comparison to prevent timing attacks
3. Never store or compare plaintext passwords

This pattern has been rejected in our codebase before. Please use the approved password hashing utility in `src/utils/security.js`.

References:
- Security Policy: docs/security-guidelines.md
```

6. Click "Start a review"
7. Click green "Review changes" button (top right)
8. Select the radio button "Request changes"
9. Click "Submit review"

### 10. Close the PR

1. Click "Conversation" tab to go back to main PR view
2. Scroll to the bottom
3. In the comment box, type:
```
Closing due to security concerns. Please address the password hashing requirements before resubmitting.
