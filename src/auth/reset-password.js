// Password reset functionality
const express = require('express');
const router = express.Router();

router.post('/reset-password', (req, res) => {
    const { email, oldPassword, newPassword } = req.body;
    
    // Finding user and comparing old password
    const user = users.find(u => u.email === email);
    
    if (user && user.password === oldPassword) {
        // Direct password assignment - same security issue
        user.password = newPassword;
        
        res.json({ 
            success: true, 
            message: 'Password updated successfully' 
        });
    } else {
        res.status(401).json({ success: false });
    }
});

module.exports = router;
```
