{
    'name': 'Instituto',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de cicles formatius en un instituto',
    'author': 'Alejandro',
    'depends': ['base', 'mail'], 
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/cicle_formatiu_views.xml',
        'views/modul_views.xml',
        'views/alumne_views.xml',
        'views/professor_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

