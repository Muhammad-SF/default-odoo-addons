# -*- coding: utf-8 -*-
{
    'name': 'Employee Events',
	'category': 'General',
    'author':'Arun Reghu Kumar',
	'license': "AGPL-3",
    'version': '1.0', 
    'description': """    
    
        * Employee Events Module : This module will show all the upcoming events in Employee form view in Upcoming Events tab.
        * Upcoming Events like leaves, calendar events, scheduled activities will list down in One2Many field.
        * Each events will display in different colour (one2many javascript).

    """,
    'maintainer': 'Arun Reghu Kumar',
    'depends': ['hr'],
    'data': [        
        'security/ir.model.access.csv',       
        'views/employee_view.xml',
        'views/template_js.xml',
    ],
    'qweb': [
       # 'static/src/xml/*.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
