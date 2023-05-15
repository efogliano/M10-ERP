from odoo import models, fields
class plane_vol(models.Model):
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Date('Data Sortida')
    dataArrivada = fields.Date('Data Arrivada')