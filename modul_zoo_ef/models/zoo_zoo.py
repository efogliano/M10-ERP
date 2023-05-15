from odoo import models, fields
class zoo_zoo(models.Model):
    id = fields.Integer('Codi', required=True)
    grandaria = fields.Integer('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')