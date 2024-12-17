# -*- coding: utf-8 -*-
{
    'name': "lista_tareas",

    'summary': "Sencilla lista de tareas new",

    'description': """
Sencilla lista de tareas utilizadas para crear un nuevo módulo con
un nuevo modelo de datos
    """,

    'author': "Alejandro Fernandez",
    'website': "https://www.yourcompany.com",
    
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/kanban_views.xml',
        'views/calendar_views.xml',
        'views/views.xml',
    ],
    
}

