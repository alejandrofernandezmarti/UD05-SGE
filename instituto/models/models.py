from odoo import models, fields, api
from odoo.exceptions import AccessError

class FormacioAlumne(models.Model):
    _name = 'formacio.alumne'
    _description = 'Alumne'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email") 
    modul_ids = fields.One2many('formacio.modul', 'professor_id', string="Mòduls")
    role = fields.Selection([
        ('alumne', 'Alumne'),
        ('professor', 'Professor')
    ], string="Rol", default='alumne', required=True)

class FormacioCicle(models.Model):
    _name = 'formacio.cicle'
    _description = 'Cicle Formatiu'
    _rec_name = 'name'

    name = fields.Char(string="Nom", required=True)
    moduls_ids = fields.One2many('formacio.modul', 'cicle_id', string="Mòduls")
    
class FormacioModul(models.Model):
    _name = 'formacio.modul'
    _description = 'Mòdul Formatiu'

    name = fields.Char(string="Nom", required=True)
    cicle_id = fields.Many2one('formacio.cicle', string="Cicle Formatiu")
    professor_id = fields.Many2one('formacio.professor', string="Professor")  # Relación Many2one

    


class FormacioProfessor(models.Model):
    _name = 'formacio.professor'
    _description = 'Professor'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email")  # Campo email añadido
    modul_ids = fields.Many2many('formacio.modul', string="Mòduls")
    role = fields.Selection([
        ('professor', 'Professor')
    ], string="Rol", default='professor', required=True)

    @api.model
    def create(self, vals):
        if not self.env.user.has_group('instituto.group_director'):
            raise AccessError("Només els Directors poden crear registres.")
        return super().create(vals)

    def write(self, vals):
        if not self.env.user.has_group('instituto.group_director'):
            raise AccessError("Només els Directors poden modificar registres.")
        return super().write(vals)

    def unlink(self):
        if not self.env.user.has_group('instituto.group_director'):
            raise AccessError("Només els Directors poden eliminar registres.")
        return super().unlink()

