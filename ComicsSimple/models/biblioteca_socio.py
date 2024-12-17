from odoo import models, fields, api

class biblioteca_socio(models.Model):
    
    _name = 'biblioteca.socio'
    _description = 'Socios de la biblioteca'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    identificador = fields.Char(string='Identificador', required=True, unique=True)

    _sql_constraints = [
        ('identificador_uniq', 'UNIQUE(identificador)', 'El identificador del socio debe ser único.'),
    ]
