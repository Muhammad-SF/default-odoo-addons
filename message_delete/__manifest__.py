# -*- coding: utf-8 -*-
{
    "name": "Message Delete",
    "version": "12.0.1.2.0",
    "category": "Discuss",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/message-delete-374",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "mail"
    ],
    "data": [
        "data/data.xml",
        "security/ir.model.access.csv",
        "views/templates.xml"
    ],
    "qweb": [
        "static/src/xml/*.xml"
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The tool to let Odoo administrators delete messages from threads and channels",
    "description": """
    This is the tool to simplify work of Odoo administrators while revising emails. With the app such users might delete messages right from channel and thread interfaces.

    For message/notes editing use the tool <a href='https://apps.odoo.com/apps/modules/12.0/message_edit/'>Message / Note Editing</a>
    In order to delete a message a user should just press the trash icon and confirm this action
    For security purposes the right to remove messages belongs only to the users with the right 'Settings > Administration'
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "0.0",
    "currency": "EUR",
}