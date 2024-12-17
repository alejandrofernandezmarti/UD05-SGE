{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage patients, doctors, and diagnoses in a hospital.',
    'description': """
        A module to manage hospital operations, including:
        - Patient records
        - Doctor records
        - Diagnoses and patient-doctor interactions
    """,
    'author': 'Alejandro',
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_diagnosis_views.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}