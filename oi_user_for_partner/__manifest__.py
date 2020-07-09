# -*- coding: utf-8 -*-

{
    'name': "Create User for existing partner / employee",

    'summary': """
            Create User for existing partner  / employee
        """,

    'description': """
        Create User for existing partner
    """,

    'category': 'Extra Tools',    
    "version": "12.0.1.1.0",
    "author": "Openinside",
    "website": "https://www.open-inside.com",
    "license": "OPL-1",
    "price" : 0,
    "currency": 'EUR',
   
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'oi_partner_employee'],

    # always loaded
    'data': [
        'view/res_users.xml'
    ],
    
    'qweb' : [
            
        ],
    'odoo-apps' : True           

      
}