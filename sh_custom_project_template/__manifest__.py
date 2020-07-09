# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Project Custom Task Template",
    
    "author": "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",
        
    "support": "info@softhealer.com",   

    "version": "12.0.1",
    
    "category": "Project",
    
    "summary": "This module is very useful for generating repeated task.",
        
    "description": """This module is useful to generate repeated task. First need to create template for repeated task. Select template in project and easily generate task on fire.""",
     
    "depends": ['project'],
    
    "data": [
        'security/ir.model.access.csv',
        'views/project_template.xml',
    ],    
    
    "images": ["static/description/background.png",],
                 
    "installable": True,
    "auto_install": False,
    "application": True,  
      
    "price": "15",
    "currency": "EUR"          
}
