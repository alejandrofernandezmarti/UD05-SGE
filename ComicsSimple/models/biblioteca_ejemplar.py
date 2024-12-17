from odoo import models, fields, api

class bibliotecar_ejemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de cómic para préstamo'

    comic_id = fields.Many2one('biblioteca.comic', string='Cómic', required=True)
    socio_id = fields.Many2one('biblioteca.socio', string='Prestado a', ondelete='set null')
    fecha_prestamo = fields.Date(string='Fecha de préstamo')
    fecha_devolucion = fields.Date(string='Fecha prevista de devolución')

    @api.constrains('fecha_prestamo', 'fecha_devolucion')
    def _check_fechas(self):
        for record in self:
            if record.fecha_prestamo and record.fecha_prestamo > fields.Date.today():
                raise ValidationError('La fecha de préstamo no puede ser posterior al día de hoy.')
            if record.fecha_devolucion and record.fecha_devolucion < fields.Date.today():
                raise ValidationError('La fecha prevista de devolución no puede ser anterior al día de hoy.')
