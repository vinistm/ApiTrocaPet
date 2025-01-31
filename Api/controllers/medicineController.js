const Medicine = require('../models/Medicine');

exports.createMedicine = async (req, res) => {
    const { name, quantity, expirationDate, animalType } = req.body;
    const owner = req.user.id;

    try {
        const medicine = new Medicine({ name, quantity, expirationDate, animalType, owner });
        await medicine.save();
        res.status(201).json(medicine);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao criar medicamento.' });
    }
};

exports.getMedicines = async (req, res) => {
    try {
        const medicines = await Medicine.find().populate('owner', 'name phone');
        res.json(medicines);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao buscar medicamentos.' });
    }
};

exports.updateMedicine = async (req, res) => {
    const { id } = req.params;
    const { name, quantity, expirationDate, animalType } = req.body;

    try {
        const medicine = await Medicine.findByIdAndUpdate(id, { name, quantity, expirationDate, animalType }, { new: true });
        res.json(medicine);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao atualizar medicamento.' });
    }
};

exports.deleteMedicine = async (req, res) => {
    const { id } = req.params;

    try {
        await Medicine.findByIdAndDelete(id);
        res.json({ message: 'Medicamento deletado com sucesso.' });
    } catch (error) {
        res.status(500).json({ message: 'Erro ao deletar medicamento.' });
    }
};