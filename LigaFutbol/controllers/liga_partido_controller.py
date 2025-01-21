from odoo import http
from odoo.http import request

class LigaPartidoController(http.Controller):
    @http.route('/eliminarempates', type='http', auth='public', methods=['GET'], csrf=False)
    def eliminar_empates(self, **kwargs):
        try:
            # Ejecutar una consulta SQL para obtener los IDs de partidos empatados
            request.env.cr.execute("""
                SELECT id FROM liga_partido
                WHERE goles_casa = goles_fuera
            """)
            # Obtener los IDs de los partidos empatados
            partidos_ids = [row[0] for row in request.env.cr.fetchall()]

            # Buscar y eliminar los partidos empatados
            partidos_empatados = request.env['liga.partido'].sudo().browse(partidos_ids)
            num_partidos = len(partidos_empatados)
            partidos_empatados.unlink()

            # Devolver el número de partidos eliminados
            return f"Se han eliminado {num_partidos} partidos empatados."
        except Exception as e:
            # Devuelve el error para depuración
            return f"Error: {str(e)}"
