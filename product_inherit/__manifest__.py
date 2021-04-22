{
    'name' : 'Product Inharit',
    'version' : '1.0',
    'sequence' : 4,
    'description' : 'Two New Menu',
    'depends' : ['base', 'sale', 'purchase', 'sale_management', 'stock'],
    'data' : [
        "views/product_n_dealer_views.xml",
        "views/barcode_to_product_views.xml",
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
