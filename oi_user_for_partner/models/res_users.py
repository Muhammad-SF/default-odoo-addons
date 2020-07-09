'''
Created on Nov 27, 2018

@author: Zuhair Hammadi
'''
from odoo import models, api

class Users(models.Model):
    _inherit = "res.users"

    @api.model_create_multi
    @api.returns('self', lambda value: value.id)
    def create(self, vals_list):        
        records = super(Users, self).create(vals_list)
        for user, vals in zip(records, vals_list):
            if 'partner_id' in vals:
                employee = self.env['hr.employee'].search([('address_home_id','=', vals['partner_id'])], limit = 1)
                if employee and not employee.user_id:
                    employee.user_id = user
        return records