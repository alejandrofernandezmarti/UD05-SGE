{
    'name': 'Institut Module',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestió de cicles formatius en un institut',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/cicle_formatiu_views.xml',
        'views/modul_views.xml',
        'views/usuaris_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
