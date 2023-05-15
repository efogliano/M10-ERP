from odoo import models, fields
class zoo_especie(models.Model):
    id = fields.Integer('Codi', required=True)
    perill = fields.Char('Perill')
    nomVulgar = fields.Char('Nom Vulgar')
    nomCientific = fields.Char('Nom cientific')
    familia = fields.Char('Familia')