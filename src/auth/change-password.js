// Change password functionality (new developer attempt)
const express = require('express');
const router = express.Router();

router.post('/change-password', (req, res) => {
    const { userId, currentPassword, newPassword } = req.body;
    
    // Yet another plaintext password comparison
    const user = users.find(u => u.id === userId);
    
    if (user && user.password === currentPassword) {
        // Direct password update - same forbidden pattern
        user.password = newPassword;
        
        // Log the password change (another security issue)
        console.log(`User ${userId} changed password from ${currentPassword} to ${newPassword}`);
        
        res.json({ success: true });
    } else {
        res.status(401).json({ success: false });
    }
});

module.exports = router;
```
