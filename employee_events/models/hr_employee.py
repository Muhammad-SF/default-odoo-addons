import datetime
from odoo import api, fields, models, _

# inherit employee module
class Employee(models.Model):
    _inherit = 'hr.employee'  
         
    event_ids = fields.One2many('upcoming.events', 'employee_id', string='Upcoming Events',copy=True)
    # creating upcoming events from Leaves,Calender and Activity
    # Function from  event_list.js
    @api.model
    def default_events(self,emp_id):          
        up_ev_data = []
        events_obj= self.env['upcoming.events']
        cal_obj= self.env['calendar.event']
        emp_obj= self.env['hr.employee']
        act_obj= self.env['mail.activity']
        leave_obj= self.env['hr.leave']
        if(emp_id):
            # Clearing existing upcoming event lines 
            self.env['upcoming.events'].search([('employee_id','=',emp_id)]).unlink()
            # creating upcoming events from Leaves  
            leaveline= leave_obj.search([('employee_id','=',emp_id),('state','=','validate'),('request_date_to','>',datetime.datetime.utcnow().date())])            
            for leave in leaveline:                
                vals={
                    'name' : leave.holiday_status_id.name,
                    'employee_id': leave.employee_id.id, 
                    'date_start': leave.request_date_from,
                    'date_end': leave.request_date_to,
                    'state':'validate',
                    'event_type':'leave',          
                }               
                up_ev_data.append(vals) 
            # creating upcoming events from Calendar events              
            employee= emp_obj.search([('id','=',emp_id)])
            if(employee):                
                event_line=cal_obj.search([('partner_ids','in',employee.user_id.partner_id.id),('privacy','=','public'),('stop_date','>=',datetime.datetime.utcnow().date())]) 
                for event in event_line:
                    vals={
                        'name' : event.name,
                        'employee_id': emp_id, 
                        'date_start': event.start_date,
                        'date_end': event.stop_date,
                        'state':'validate',
                        'event_type':'calendar',            
                    }
                    up_ev_data.append(vals)                   
            # creating upcoming events from Activity
            if(employee):               
                act_line=act_obj.search([('res_id','=',employee.id),('res_model_id','=','hr.employee'),('date_deadline','>=',datetime.datetime.utcnow().date())]) 
                for act in act_line:
                    vals={
                        'name' : act.summary,
                        'employee_id': emp_id, 
                        'date_start': act.date_deadline,
                        'date_end': act.date_deadline,
                        'state':'validate',
                        'event_type':'activity',            
                    }
                    up_ev_data.append(vals)
            # Sort based on the date                
            up_ev_data_new=sorted(up_ev_data, key = lambda i: i['date_start'])   
            # Creating upcoming event lines   
            events_obj.create(up_ev_data_new)            
        return up_ev_data        
   
   

# upcoming.events module
class UpcomingEvents(models.Model):
    _name = 'upcoming.events'
    name = fields.Char('Events')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    date_start = fields.Date('Start Date', default=fields.Date.today,
        help="Start date of the event.")
    date_end = fields.Date('End Date', default=fields.Date.today,
        help="End date of the event.")
    event_type=fields.Selection([
            ('leave', 'Leave'),
            ('calendar', 'Calendar'),
            ('activity', 'Activity'),           
        ], string='Type', default='calendar')
    state = fields.Selection([
            ('draft', 'New'),
            ('confirm', 'Waiting Approval'),
            ('refuse', 'Refused'),
            ('validate1', 'Waiting Second Approval'),
            ('validate', 'Approved'),
            ('cancel', 'Cancelled')
        ], string='Status', default='draft')
