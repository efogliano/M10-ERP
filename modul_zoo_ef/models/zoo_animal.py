from odoo import models, fields
class zoo_animal(models.Model):
    id = fields.Integer('Codi', required=True)
    continentOrigen = fields.Char('Continent Origen')
    dataNaix = fields.Date('Data de naixament')
    paisOrigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')