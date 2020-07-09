# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Activity Notification",
    
    "author": "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",
        
    "version": "12.0.4",
	
    "support": "support@softhealer.com",
    
    "category": "Extra Tools",
    
    "summary": """
	The main purpose of the activity notification is to announce the arrival of the meeting time. another purpose of this module to make one aware of facts or occurrences before the due date. 
""",
        
    "description": """
	The main purpose of the activity notification is to announce the arrival of the meeting time. another purpose of this module to make one aware of facts or occurrences before the due date. This module will help to send a notification before and after the activity due date. You can notify your salesperson/customer before or after the activity is done. Suppose you want to notify your salesperson for a meeting before the due date of the meeting so you can set a schedule into 'schedule activity' in the chatter of any form of view.
Activity Notification Odoo
 Activity Notifier Module, Send Salesperson Notification Before Activity, Send Customer Notification After Activity, Notify Customer For Activity Due Date, Reminder For Activity Odoo.
 Activity Notifier Module, Salesperson Activity Notification, Customer Activity Notification Module,Activity Due Date Notify, Activity Reminder Odoo.
""",
     
    "depends": ['crm','mail'],
    
    "data": [
        'data/data_sales_activity_notification.xml',
        'data/sales_activity_email_template.xml',
        'views/sale_activity.xml',
    ],    
    
    "images": ["static/description/background.png",],
    "installable": True,
    "auto_install": False,
    "application": True,  
    "price": "35",
    "currency": "EUR"          
}
