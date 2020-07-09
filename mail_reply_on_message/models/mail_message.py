from odoo import models, fields, api, _


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.multi
    def reply_context(self):
        self.ensure_one()

        body = (_(
            "<br/><blockquote style='border-left-width:thin;border-left-style:solid;border-left-color:rgb(204, 204, 204);padding-left:1ex;'><div>On %s at %s, %s wrote:</div>%s</blockquote>") %
                (self.date.strftime("%d %b %Y"), self.date.strftime("%H:%M"), self.author_id.name, self.body))

        ctx = {
            'default_res_id': self.res_id,
            'default_parent_id': self.id,
            'default_model': self.model,
            'default_body': body,
            'default_m_id': self.id,
        }
        return ctx
