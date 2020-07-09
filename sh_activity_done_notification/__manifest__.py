# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Send notification on activity done",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",    
    "category": "Accounting",
    "summary": "Send notification on Done Activity",
    "description": """
Send notification on Done Activity
                    """,    
    "version":"12.0.4",
    "depends" : [
                
                "base",
                "mail",
                "web",
                "sh_acitivity_notification"
            ],
    "application" : True,
    "data" : [
        
            "data/mail_data.xml",          
            
            ],    
    'external_dependencies': {
        'python': [
            'html2text',
        ],
    },        
    "images": ["static/description/background.png",],              
    "auto_install":False,
    "installable" : True,
    "price": 30,
    "currency": "EUR"   
}
