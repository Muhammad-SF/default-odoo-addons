from odoo import fields, api, models, _


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def _update_tnd(self):
        tnd = self.env['res.currency'].search([('name', '=', 'TND')])
        tnd.currency_unit_label = "Dinars"