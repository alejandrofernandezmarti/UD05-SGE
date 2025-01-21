from odoo import http
from odoo.http import request

class LigaEquipoController(http.Controller):
    @http.route('/visualitzaequip', type='http', auth='public', methods=['GET'], csrf=False)
    def visualitza_equip(self, nom=None, **kwargs):
        try:
            if not nom:
                return "Por favor, especifique el nombre del equipo como parámetro (?nom=nombre_del_equipo)."

            equipo = request.env['liga.equipo'].sudo().search([('nombre', '=', nom)], limit=1)
            
            if not equipo:
                return f"No se encontró ningún equipo con el nombre: {nom}"

            datos = {
                'nombre': equipo.nombre,
                'descripcion': equipo.descripcion or 'Sin descripción',
                'fecha_fundacion': equipo.fecha_fundacion or 'No especificado',
                'escudo': f"<img src='data:image/png;base64,{equipo.escudo.decode('utf-8')}'/>" if equipo.escudo else ''
            }

            html = f"""
            <html>
                <head>
                    <title>Información del Equipo</title>
                </head>
                <body>
                    <h1>Información del Equipo: {datos['nombre']}</h1>
                    <p><strong>Descripción:</strong> {datos['descripcion']}</p>
                    <p><strong>Año de Fundación:</strong> {datos['fecha_fundacion']}</p>
                    <p><strong>Escudo:</strong></p>
                    {datos['escudo']}
                </body>
            </html>
            """
            return html
        except Exception as e:
            return f"Se produjo un error: {str(e)}"
