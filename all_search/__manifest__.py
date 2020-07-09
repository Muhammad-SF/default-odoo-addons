# -*- coding: utf-8 -*-
{
    'name': 'Odoo Easy Search, global search, quick search',
    'summary': 'Search any data in Odoo. quick and easy. all data search. global search. fast search ever. fast search easy search search quick search search any object global search odoo search all databse search all search search products search invoices search orders search vendors search customers search any data',
    'author': "Simple Apps",
    'license': 'OPL-1',
    'version': '12.0',
    'description': """
User can easily search any data or record from Odoo.
The entered query will be searched in all possible objects.  
fast search
easy search
search
quick search
search any object
global search
odoo search
all databse search
all search
search products
search invoices
search orders
search vendors
search customers
search any data
    """,
    'category': 'Tools',
    'depends': ['web'],
    'data': [
        'security/search_security.xml',
        'security/ir.model.access.csv',
        'views/search_views.xml',
        'views/all_search_template.xml',
    ],
    'qweb': [
        'static/src/xml/all_search.xml'
    ],
    'images': ['static/description/screen1.png'],
    'price': 19.0,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False
}

