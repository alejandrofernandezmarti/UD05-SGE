{
    'name': "Biblioteca de Comics",
    'summary': "Gestión de cómics, socios y ejemplares para préstamos.",
    'description': "Un módulo para gestionar cómics, socios y préstamos en una biblioteca.",
    'author': "Tu Nombre",
    'category': 'Library Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml',
        'views/biblioteca_ejemplar.xml',
        'views/biblioteca_socio.xml',
    ],
    'application': True,
}
