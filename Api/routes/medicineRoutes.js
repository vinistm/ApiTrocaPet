const express = require('express');
const { authenticate } = require('../middleware/authMiddleware');
const { createMedicine, getMedicines, updateMedicine, deleteMedicine } = require('../controllers/medicineController');

const router = express.Router();

router.post('/', authenticate, createMedicine);
router.get('/', getMedicines);
router.put('/:id', authenticate, updateMedicine);
router.delete('/:id', authenticate, deleteMedicine);

module.exports = router;