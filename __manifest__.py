{
    'name': 'Hall Invoices',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Custom invoice type for hall rentals',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
} 