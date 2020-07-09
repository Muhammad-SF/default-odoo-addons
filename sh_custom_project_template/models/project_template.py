# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api
from odoo.exceptions import UserError

class ProjectTemplateTask(models.Model):
    _name = 'project.template.task'
    _description = 'Project Template Task'

    name = fields.Char(string="Task",required=True)    
    assigned_to = fields.Many2one("res.users",string="Assigned To")
    description = fields.Html("Description")

    project_template_id = fields.Many2one("project.template",string="Project Template Id")
    
class ProjectTemplate(models.Model):
    _name = 'project.template'
    _description = 'Project Template'
    
    name = fields.Char("Template",required=True)
    project_template_task_ids = fields.One2many("project.template.task","project_template_id",string="Project Template Task")
    templ_active = fields.Boolean("Active",default=True)

class ProjectProject(models.Model):
    _inherit = 'project.project'
     
    project_template_id = fields.Many2one("project.template",string="Project Template")
    
    @api.multi
    def btn_project_generate_task(self):
      
        if self.project_template_id:            

            for record in self.project_template_id.project_template_task_ids:                
                
                vals={'name':record.name,
                            'project_id':self.id,
                            'description':record.description,
                             }
                
                if record.assigned_to:                                    
                    vals.update({'user_id':record.assigned_to.id })

                task_obj = self.env['project.task'].sudo().create(vals)    
                 
            return { 'type': 'ir.actions.client','tag': 'reload'}

        else :
            raise UserError('Please Select Project Template.')

