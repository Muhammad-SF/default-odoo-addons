# -*- coding: utf-8 -*-
{
    'name': "Custom Invoice PDF Form for Tunisia",

    'summary': """Custom Invoice PDF Form for Tunisia""",
    'author': "Kirill Sudnikovich",
    'website': "https://sntch.dev",
    'category': 'Uncategorized',
    'version': '12.0.00.1',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'views/templates.xml',
    ],
    'post_init_hook': '_initial_setup',
}