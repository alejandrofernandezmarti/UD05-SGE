from odoo import models, fields, api

class LigaPartidoWizard(models.TransientModel):  # Debe heredar de TransientModel
    _name = 'liga.partido.wizard'
    _description = 'Wizard para crear un nuevo partido'

    equipo_casa = fields.Many2one('liga.equipo', string="Equipo Local", required=True)
    equipo_fuera = fields.Many2one('liga.equipo', string="Equipo Visitante", required=True)
    goles_casa = fields.Integer(string="Goles Local", default=0)
    goles_fuera = fields.Integer(string="Goles Visitante", default=0)

    def crear_partido(self):
        """Crea un nuevo partido con los datos del wizard."""
        self.env['liga.partido'].create({
            'equipo_casa': self.equipo_casa.id,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_casa': self.goles_casa,
            'goles_fuera': self.goles_fuera,
        })
