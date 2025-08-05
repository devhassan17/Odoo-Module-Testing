{
    'name': 'Monta_Connector',
    'version': '1.0',
    'summary': 'Integrates Odoo v18 with Monta WMS',
    'author': 'Ali Hassan',
    'category': 'Inventory',
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/monta_config_view.xml',
    ],
    'installable': True,
    'application': True,
}
