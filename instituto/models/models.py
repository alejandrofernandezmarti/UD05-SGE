from odoo import models, fields

class FormacioCicle(models.Model):
    _name = 'formacio.cicle'
    _description = 'Cicle Formatiu'

    name = fields.Char(string="Nom del Cicle", required=True)
    modul_ids = fields.One2many('formacio.modul', 'cicle_id', string="Mòduls Associats")


class FormacioModul(models.Model):
    _name = 'formacio.modul'
    _description = 'Mòdul'

    name = fields.Char(string="Nom del Mòdul", required=True)
    cicle_id = fields.Many2one('formacio.cicle', string="Cicle Formatiu")
    professor_id = fields.Many2one('formacio.professor', string="Professor")
    alumne_ids = fields.Many2many('formacio.alumne', string="Alumnes Matriculats")


class FormacioAlumne(models.Model):
    _name = 'formacio.alumne'
    _description = 'Alumne'

    name = fields.Char(string="Nom de l'Alumne", required=True)
    email = fields.Char(string="Email")
    modul_ids = fields.Many2many('formacio.modul', string="Mòduls Matriculats")


class FormacioProfessor(models.Model):
    _name = 'formacio.professor'
    _description = 'Professor'

    name = fields.Char(string="Nom del Professor", required=True)
    modul_ids = fields.One2many('formacio.modul', 'professor_id', string="Mòduls Impartits")
