from odoo import models, fields
class plane_avio(models.Model):
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Velocitat Maxima')