{
    'name' : 'Purchase Extend',
    'version' : '1.1',
    'summary': 'Purchase New Features',
    'sequence': 3,
    'description': 'Some features added and some features removed.',
    'depends' : ['base', 'purchase', 'product_inherit', 'sale', 'sale_management'],
    'data': [
        'views/purchase_new_views.xml',
        'views/purchase_filter_views.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
