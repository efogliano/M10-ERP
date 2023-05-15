from odoo import models, fields
class plane_pilot(models.Model):
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognom')
    nif = fields.Char('NIF')
    telf = fields.Char('Numero de telefon')
    email = fields.Char('Correu electronic')