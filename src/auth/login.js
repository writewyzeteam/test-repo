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
