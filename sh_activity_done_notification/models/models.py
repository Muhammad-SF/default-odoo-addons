# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from collections import defaultdict
from odoo import api, fields, models, _
import html2text

class MailActivity(models.Model):
    _inherit='mail.activity'
    
    def get_feedback(self):
        h = html2text.HTML2Text()
        feedback = ''
        if self.feedback:
            feedback = h.handle(self.feedback)
        return feedback
    
    def get_note(self):
        h = html2text.HTML2Text()
        note = ''
        if self.note:
            note = h.handle(self.note)
        return note
    
    @api.multi
    def write(self, values):
        res = super(MailActivity, self.sudo()).write(values)
        if not values.get('is_done_activity',False) and not values.get('feedback',False) and self.user_id != self.create_user_id:
            template = self.env.ref('sh_activity_done_notification.send_done_notification_assigned_user')
            if template:
                # Send out the e-mail template to the user
                self.env['mail.template'].sudo().browse(template.id).with_context(edit_activity=True,user=self.env.user.name).send_mail(self.id, force_send=True)
        return res
    
    @api.multi
    def unlink(self):
        for activity in self:
            if 'done_act' not in self._context and self.user_id != self.create_user_id:
                template = self.env.ref('sh_activity_done_notification.send_done_notification_assigned_user')
                if template:
                    # Send out the e-mail template to the user
                    self.env['mail.template'].sudo().browse(template.id).with_context(unlink_activity=True,user=self.env.user.name).send_mail(activity.id, force_send=True)
        return super(MailActivity, self.sudo()).unlink()
    
    def action_feedback(self, feedback=False):
        message = self.env['mail.message']
        if feedback:
            self.write(dict(feedback=feedback))

        # Search for all attachments linked to the activities we are about to unlink. This way, we
        # can link them to the message posted and prevent their deletion.
        attachments = self.env['ir.attachment'].search_read([
            ('res_model', '=', self._name),
            ('res_id', 'in', self.ids),
        ], ['id', 'res_id'])

        activity_attachments = defaultdict(list)
        for attachment in attachments:
            activity_id = attachment['res_id']
            activity_attachments[activity_id].append(attachment['id'])

        for activity in self:
            record = self.env[activity.res_model].browse(activity.res_id)
            record.message_post_with_view(
                'mail.message_activity_done',
                values={'activity': activity},
                subtype_id=self.env['ir.model.data'].xmlid_to_res_id('mail.mt_activities'),
                mail_activity_type_id=activity.activity_type_id.id,
            )

            # Moving the attachments in the message
            # TODO: Fix void res_id on attachment when you create an activity with an image
            # directly, see route /web_editor/attachment/add
            activity_message = record.message_ids[0]
            message_attachments = self.env['ir.attachment'].browse(activity_attachments[activity.id])
            if message_attachments:
                message_attachments.write({
                    'res_id': activity_message.id,
                    'res_model': activity_message._name,
                })
                activity_message.attachment_ids = message_attachments
            message |= activity_message

         
        self.write({'is_done_activity':True})
        template = self.env.ref('sh_activity_done_notification.send_done_notification_assigned_user')
        # Send out the e-mail template to the user
        if self.user_id != self.create_user_id:
            self.env['mail.template'].sudo().browse(template.id).with_context(done_activity=True,user=self.env.user.name).send_mail(self.id, force_send=True)
            
        self.with_context(done_act=True).unlink()
        
        return message.ids and message.ids[0] or False
    
    
